
#include <string.h>

#include <glib.h>

#include "gabble-presence.h"

G_DEFINE_TYPE (GabblePresence, gabble_presence, G_TYPE_OBJECT);

#define GABBLE_PRESENCE_PRIV(account) ((GabblePresencePrivate *)account->priv)

typedef struct _Resource Resource;

struct _Resource {
    gchar *name;
    GabblePresenceCapabilities caps;
    GabblePresenceId status;
    gchar *status_message;
    gchar *status_name;
};

typedef struct _GabblePresencePrivate GabblePresencePrivate;

struct _GabblePresencePrivate {
    GSList *resources;
};

static Resource *
_resource_new (gchar *name)
{
  Resource *new = g_new (Resource, 1);
  new->name = name;
  new->caps = CAP_NONE;
  new->status = GABBLE_PRESENCE_OFFLINE;
  new->status_message = NULL;
  return new;
}

/*
static void
_resource_free (Resource *resource)
{
  if (resource->status_message)
    g_free (resource->status_message);

  g_free (resource);
}
*/

static void
gabble_presence_class_init (GabblePresenceClass *klass)
{
  GObjectClass *object_class = G_OBJECT_CLASS (klass);
  g_type_class_add_private (object_class, sizeof (GabblePresencePrivate));
}

static void
gabble_presence_init (GabblePresence *self)
{
  self->priv = G_TYPE_INSTANCE_GET_PRIVATE (self,
      GABBLE_TYPE_PRESENCE, GabblePresencePrivate);
  ((GabblePresencePrivate *)self->priv)->resources = NULL;
}

GabblePresence*
gabble_presence_new (void)
{
  return g_object_new (GABBLE_TYPE_PRESENCE, NULL);
}

gboolean
gabble_presence_get_supports_voice (GabblePresence *presence)
{
  GabblePresencePrivate *priv = GABBLE_PRESENCE_PRIV (presence);
  GSList *i;

  for (i = priv->resources; NULL != i; i = i->next)
    {
      Resource *res = (Resource *) i->data;

      if (res->caps & CAP_VOICE)
        return TRUE;
    }

  return FALSE;
}

const gchar *
gabble_presence_pick_voice_resource (GabblePresence *presence)
{
  GabblePresencePrivate *priv = GABBLE_PRESENCE_PRIV (presence);
  GSList *i;

  for (i = priv->resources; NULL != i; i = i->next)
    {
      Resource *res = (Resource *) i->data;

      if (res->caps & CAP_VOICE)
        return res->name;
    }

  return NULL;
}

void
gabble_presence_set_capabilities (GabblePresence *presence, const gchar *resource, GabblePresenceCapabilities caps)
{
  GSList *i;
  GabblePresencePrivate *priv = GABBLE_PRESENCE_PRIV (presence);

  if (caps & CAP_VOICE)
    g_debug ("setting voice cap for resource %s", resource);

  for (i = priv->resources; NULL != i; i = i->next)
    {
      Resource *tmp = (Resource *) i->data;

      if (0 == strcmp (tmp->name, resource))
        {
          tmp->caps |= caps;
          break;
        }
    }
}

void
gabble_presence_update (GabblePresence *presence, const gchar *resource, GabblePresenceId status, const gchar *status_message)
{
  GSList *i;
  Resource *res = NULL;
  GabblePresencePrivate *priv = GABBLE_PRESENCE_PRIV (presence);

  g_assert (NULL != resource);
  g_debug ("UPDATE: %s/%d/%s", resource, status, status_message);

  for (i = priv->resources; NULL != i; i = i->next)
    {
      Resource *tmp = (Resource *) i->data;

      if (0 == strcmp (tmp->name, resource))
        {
          res = tmp;
          break;
        }
    }

  if (NULL == res)
    {
      res = _resource_new (g_strdup (resource));
      priv->resources = g_slist_append (priv->resources, res);
    }

  res->status = status;
  g_free (res->status_message);
  res->status_message = g_strdup (status_message);

  presence->status = res->status;
  presence->status_message = res->status_message;
}

