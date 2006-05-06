/*
 * roster.h - Headers for Gabble roster helper
 *
 * Copyright (C) 2006 Collabora Ltd.
 * Copyright (C) 2006 Nokia Corporation
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

#ifndef __ROSTER_H__
#define __ROSTER_H__

#include <glib-object.h>

#include "gabble-types.h"

G_BEGIN_DECLS

typedef struct _GabbleRosterClass GabbleRosterClass;

GType gabble_roster_get_type(void);

/* TYPE MACROS */
#define GABBLE_TYPE_ROSTER \
  (gabble_roster_get_type())
#define GABBLE_ROSTER(obj) \
  (G_TYPE_CHECK_INSTANCE_CAST((obj), GABBLE_TYPE_ROSTER, GabbleRoster))
#define GABBLE_ROSTER_CLASS(klass) \
  (G_TYPE_CHECK_CLASS_CAST((klass), GABBLE_TYPE_ROSTER, GabbleRosterClass))
#define GABBLE_IS_ROSTER(obj) \
  (G_TYPE_CHECK_INSTANCE_TYPE((obj), GABBLE_TYPE_ROSTER))
#define GABBLE_IS_ROSTER_CLASS(klass) \
  (G_TYPE_CHECK_CLASS_TYPE((klass), GABBLE_TYPE_ROSTER))
#define GABBLE_ROSTER_GET_CLASS(obj) \
  (G_TYPE_INSTANCE_GET_CLASS ((obj), GABBLE_TYPE_ROSTER, GabbleRosterClass))

struct _GabbleRosterClass {
    GObjectClass parent_class;
};

struct _GabbleRoster {
    GObject parent;
    gpointer priv;
};

GabbleRoster *gabble_roster_new (GabbleConnection *);

G_END_DECLS

#endif /* __ROSTER_H__ */
