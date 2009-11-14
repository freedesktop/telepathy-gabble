/*
 * gabble.h - entry point and utility functions for telepathy-gabble
 * Copyright (C) 2005 Collabora Ltd.
 * Copyright (C) 2005 Nokia Corporation
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation; either
 * version 2.1 of the License, or (at your option) any later version.
 *
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with this library; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
 */

#include "config.h"
#include "gabble.h"

#include <unistd.h>

#include <telepathy-glib/debug.h>
#include <telepathy-glib/debug-sender.h>
#include <telepathy-glib/run.h>
#include <telepathy-glib/util.h>
#include <wocky/wocky.h>
#include <wocky/wocky-debug.h>

#include "debug.h"
#include "connection-manager.h"
#include "plugin-loader.h"

static TpBaseConnectionManager *
construct_cm (void)
{
  return (TpBaseConnectionManager *) g_object_new (
      GABBLE_TYPE_CONNECTION_MANAGER, NULL);
}

#ifdef ENABLE_DEBUG
static TpDebugSender *debug_sender = NULL;

static void
log_to_debug_sender (const gchar *log_domain,
    GLogLevelFlags log_level,
    const gchar *string)
{
  GTimeVal now;

  g_return_if_fail (TP_IS_DEBUG_SENDER (debug_sender));

  g_get_current_time (&now);

  tp_debug_sender_add_message (debug_sender, &now, log_domain, log_level,
      string);
}

/* Whether we redirect all wocky log message purely to the debug sender */
static gboolean redirect_wocky = FALSE;
/* Whether to add a timestamp to the output messages */
static gboolean stamp_logs = FALSE;

static void
log_handler (const gchar *log_domain,
    GLogLevelFlags log_level,
    const gchar *message,
    gpointer user_data)
{
  if (!redirect_wocky || tp_strdiff (log_domain, "wocky"))
    {
      if (stamp_logs)
        {
          GTimeVal now;
          gchar now_str[32];
          gchar *tmp;
          struct tm tm;

          g_get_current_time (&now);
          localtime_r (&(now.tv_sec), &tm);
          strftime (now_str, 32, "%Y-%m-%d %H:%M:%S", &tm);
          tmp = g_strdup_printf ("%s.%06ld: %s",
            now_str, now.tv_usec, message);

          g_log_default_handler (log_domain, log_level, tmp, NULL);

          g_free (tmp);
        }
      else
        {
          g_log_default_handler (log_domain, log_level, message, NULL);
        }
    }

  /* Gabble messages are already sent to the debug sender in gabble_debug. */
  if (log_level != G_LOG_LEVEL_DEBUG || tp_strdiff (log_domain, G_LOG_DOMAIN))
    log_to_debug_sender (log_domain, log_level, message);
}

#endif


void
gabble_init (void)
{
  /* libsoup uses glib in multiple threads and don't have this, so we have to
   * enable it manually here */
  if (!g_thread_supported ())
    g_thread_init (NULL);

  g_type_init ();
  wocky_init ();
}

int
gabble_main (int argc,
    char **argv)
{
  int out;
  tp_debug_divert_messages (g_getenv ("GABBLE_LOGFILE"));

#ifdef ENABLE_DEBUG
  gabble_debug_set_flags_from_env ();

  stamp_logs = (g_getenv ("GABBLE_TIMING") != NULL);

  if (g_getenv ("WOCKY_DEBUG") == NULL)
    {
      redirect_wocky = TRUE;
      wocky_debug_set_flags (DEBUG_XMPP | DEBUG_SASL | DEBUG_PORTER);
    }

  debug_sender = tp_debug_sender_dup ();

  g_log_set_default_handler (log_handler, NULL);

  if (g_getenv ("GABBLE_PERSIST") != NULL)
    tp_debug_set_persistent (TRUE);
#endif

  gabble_plugin_loader_dup ();

  out = tp_run_connection_manager ("telepathy-gabble", VERSION,
      construct_cm, argc, argv);

#ifdef ENABLE_DEBUG
  g_object_unref (debug_sender);
#endif

  return out;
}
