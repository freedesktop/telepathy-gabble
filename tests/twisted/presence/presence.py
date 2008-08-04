
"""
Test basic roster functionality.
"""

import dbus

from twisted.words.xish import domish, xpath

from gabbletest import exec_test

def _expect_contact_list_channel(q, bus, conn, name, contacts):
    event = q.expect('dbus-signal', signal='NewChannel')
    path, type, handle_type, handle, suppress_handler = event.args

    assert type == u'org.freedesktop.Telepathy.Channel.Type.ContactList'
    assert conn.InspectHandles(handle_type, [handle])[0] == name
    chan = bus.get_object(conn.bus_name, path)
    group_iface = dbus.Interface(chan,
        u'org.freedesktop.Telepathy.Channel.Interface.Group')
    members = group_iface.GetMembers()
    assert conn.InspectHandles(1, members) == contacts

    # Exercise basic Channel Properties from spec 0.17.7
    channel_props = chan.GetAll(
            'org.freedesktop.Telepathy.Channel',
            dbus_interface='org.freedesktop.DBus.Properties')
    assert channel_props.get('TargetHandle') == handle,\
            (channel_props.get('TargetHandle'), handle)
    assert channel_props.get('TargetHandleType') == 3,\
            channel_props.get('TargetHandleType')
    assert channel_props.get('ChannelType') == \
            'org.freedesktop.Telepathy.Channel.Type.ContactList',\
            channel_props.get('ChannelType')
    assert 'org.freedesktop.Telepathy.Channel.Interface.Group' in \
            channel_props.get('Interfaces', ()), \
            channel_props.get('Interfaces')

    # Exercise FUTURE properties
    future_props = chan.GetAll(
            'org.freedesktop.Telepathy.Channel.FUTURE',
            dbus_interface='org.freedesktop.DBus.Properties')
    assert future_props['Requested'] == False
    assert future_props['TargetID'] == name
    assert future_props['InitiatorID'] == ''
    assert future_props['InitiatorHandle'] == 0

    # Exercise Group Properties from spec 0.17.6 (in a basic way)
    group_props = chan.GetAll(
            'org.freedesktop.Telepathy.Channel.Interface.Group',
            dbus_interface='org.freedesktop.DBus.Properties')
    assert 'HandleOwners' in group_props, group_props
    assert 'Members' in group_props, group_props
    assert group_props['Members'] == members, group_props['Members']
    assert 'LocalPendingMembers' in group_props, group_props
    assert group_props['LocalPendingMembers'] == []
    assert 'RemotePendingMembers' in group_props, group_props
    assert group_props['RemotePendingMembers'] == []
    assert 'GroupFlags' in group_props, group_props

def test(q, bus, conn, stream):
    conn.Connect()
    q.expect('dbus-signal', signal='StatusChanged', args=[0, 1])

    amy_handle = conn.RequestHandles(1, ['amy@foo.com'])[0]

    event = q.expect('stream-iq', query_ns='jabber:iq:roster')
    event.stanza['type'] = 'result'

    item = event.query.addElement('item')
    item['jid'] = 'amy@foo.com'
    item['subscription'] = 'both'

    stream.send(event.stanza)

    _expect_contact_list_channel(q, bus, conn, 'publish',
        ['amy@foo.com'])
    _expect_contact_list_channel(q, bus, conn, 'subscribe',
        ['amy@foo.com'])
    _expect_contact_list_channel(q, bus, conn, 'known',
        ['amy@foo.com'])

    presence = domish.Element((None, 'presence'))
    presence['from'] = 'amy@foo.com'
    show = presence.addElement((None, 'show'))
    show.addContent('away')
    status = presence.addElement((None, 'status'))
    status.addContent('At the pub')
    stream.send(presence)

    event = q.expect('dbus-signal', signal='PresencesChanged')
    assert event.args[0] == { amy_handle: (3, 'away', 'At the pub') }

    presence = domish.Element((None, 'presence'))
    presence['from'] = 'amy@foo.com'
    show = presence.addElement((None, 'show'))
    show.addContent('chat')
    status = presence.addElement((None, 'status'))
    status.addContent('I may have been drinking')
    stream.send(presence)

    event = q.expect('dbus-signal', signal='PresencesChanged')
    assert event.args[0] == { amy_handle: (2, 'chat', 'I may have been drinking') }

    conn.Disconnect()
    q.expect('dbus-signal', signal='StatusChanged', args=[2, 1])

if __name__ == '__main__':
    exec_test(test)

