"""
Some handy constants for other tests to share and enjoy.
"""

from dbus import PROPERTIES_IFACE

HT_NONE = 0
HT_CONTACT = 1
HT_ROOM = 2
HT_LIST = 3
HT_GROUP = 4

CHANNEL = "org.freedesktop.Telepathy.Channel"

CHANNEL_IFACE_CALL_STATE = CHANNEL + ".Interface.CallState"
CHANNEL_IFACE_CHAT_STATE = CHANNEL + '.Interface.ChatState'
CHANNEL_IFACE_DESTROYABLE = CHANNEL + ".Interface.Destroyable"
CHANNEL_IFACE_GROUP = CHANNEL + ".Interface.Group"
CHANNEL_IFACE_HOLD = CHANNEL + ".Interface.Hold"
CHANNEL_IFACE_MEDIA_SIGNALLING = CHANNEL + ".Interface.MediaSignalling"
CHANNEL_IFACE_MESSAGES = CHANNEL + ".Interface.Messages"
CHANNEL_IFACE_PASSWORD = CHANNEL + ".Interface.Password"
CHANNEL_IFACE_TUBE = CHANNEL + ".Interface.Tube.DRAFT"

CHANNEL_TYPE_CONTACT_LIST = CHANNEL + ".Type.ContactList"
CHANNEL_TYPE_TEXT = CHANNEL + ".Type.Text"
CHANNEL_TYPE_TUBES = CHANNEL + ".Type.Tubes"
CHANNEL_TYPE_STREAM_TUBE = CHANNEL + ".Type.StreamTube.DRAFT"
CHANNEL_TYPE_DBUS_TUBE = CHANNEL + ".Type.DBusTube.DRAFT"
CHANNEL_TYPE_STREAMED_MEDIA = CHANNEL + ".Type.StreamedMedia"
CHANNEL_TYPE_TEXT = CHANNEL + ".Type.Text"
CHANNEL_TYPE_FILE_TRANSFER = CHANNEL + ".Type.FileTransfer"

TP_AWKWARD_PROPERTIES = "org.freedesktop.Telepathy.Properties"
PROPERTY_FLAG_READ = 1
PROPERTY_FLAG_WRITE = 2

CHANNEL_TYPE = CHANNEL + '.ChannelType'
TARGET_HANDLE_TYPE = CHANNEL + '.TargetHandleType'
TARGET_HANDLE = CHANNEL + '.TargetHandle'
TARGET_ID = CHANNEL + '.TargetID'
REQUESTED = CHANNEL + '.Requested'
INITIATOR_HANDLE = CHANNEL + '.InitiatorHandle'
INITIATOR_ID = CHANNEL + '.InitiatorID'
INTERFACES = CHANNEL + '.Interfaces'

INITIAL_AUDIO = CHANNEL_TYPE_STREAMED_MEDIA + '.FUTURE.InitialAudio'
INITIAL_VIDEO = CHANNEL_TYPE_STREAMED_MEDIA + '.FUTURE.InitialVideo'

CONN = "org.freedesktop.Telepathy.Connection"
CONN_IFACE_AVATARS = CONN + '.Interface.Avatars'
CONN_IFACE_CAPS = CONN + '.Interface.Capabilities'
CONN_IFACE_CONTACTS = CONN + '.Interface.Contacts'
CONN_IFACE_CONTACT_CAPS = CONN + '.Interface.ContactCapabilities.DRAFT'
CONN_IFACE_SIMPLE_PRESENCE = CONN + '.Interface.SimplePresence'
CONN_IFACE_REQUESTS = CONN + '.Interface.Requests'

STREAM_HANDLER = 'org.freedesktop.Telepathy.Media.StreamHandler'

ERROR = 'org.freedesktop.Telepathy.Error'
INVALID_ARGUMENT = ERROR + '.InvalidArgument'
NOT_IMPLEMENTED = ERROR + '.NotImplemented'
NOT_AVAILABLE = ERROR + '.NotAvailable'
PERMISSION_DENIED = ERROR + '.PermissionDenied'
OFFLINE = ERROR + '.Offline'
NOT_CAPABLE = ERROR + '.NotCapable'
CONNECTION_REFUSED = ERROR + '.ConnectionRefused'
CONNECTION_FAILED = ERROR + '.ConnectionFailed'
CONNECTION_LOST = ERROR + '.ConnectionLost'
CANCELLED = ERROR + '.Cancelled'

TUBE_PARAMETERS = CHANNEL_IFACE_TUBE + '.Parameters'
TUBE_STATE = CHANNEL_IFACE_TUBE + '.State'
STREAM_TUBE_SERVICE = CHANNEL_TYPE_STREAM_TUBE + '.Service'
DBUS_TUBE_SERVICE_NAME = CHANNEL_TYPE_DBUS_TUBE + '.ServiceName'
DBUS_TUBE_DBUS_NAMES = CHANNEL_TYPE_DBUS_TUBE + '.DBusNames'

TUBE_CHANNEL_STATE_LOCAL_PENDING = 0
TUBE_CHANNEL_STATE_REMOTE_PENDING = 1
TUBE_CHANNEL_STATE_OPEN = 2
TUBE_CHANNEL_STATE_NOT_OFFERED = 3

MEDIA_STREAM_TYPE_AUDIO = 0
MEDIA_STREAM_TYPE_VIDEO = 1

SOCKET_ADDRESS_TYPE_UNIX = 0
SOCKET_ADDRESS_TYPE_ABSTRACT_UNIX = 1
SOCKET_ADDRESS_TYPE_IPV4 = 2
SOCKET_ADDRESS_TYPE_IPV6 = 3

SOCKET_ACCESS_CONTROL_LOCALHOST = 0
SOCKET_ACCESS_CONTROL_PORT = 1
SOCKET_ACCESS_CONTROL_NETMASK = 2
SOCKET_ACCESS_CONTROL_CREDENTIALS = 3

TUBE_STATE_LOCAL_PENDING = 0
TUBE_STATE_REMOTE_PENDING = 1
TUBE_STATE_OPEN = 2
TUBE_STATE_NOT_OFFERED = 3

TUBE_TYPE_DBUS = 0
TUBE_TYPE_STREAM = 1

MEDIA_STREAM_DIRECTION_NONE = 0
MEDIA_STREAM_DIRECTION_SEND = 1
MEDIA_STREAM_DIRECTION_RECEIVE = 2
MEDIA_STREAM_DIRECTION_BIDIRECTIONAL = 3

MEDIA_STREAM_PENDING_LOCAL_SEND = 1
MEDIA_STREAM_PENDING_REMOTE_SEND = 2

MEDIA_STREAM_TYPE_AUDIO = 0
MEDIA_STREAM_TYPE_VIDEO = 1

MEDIA_STREAM_STATE_DISCONNECTED = 0
MEDIA_STREAM_STATE_CONNECTING = 1
MEDIA_STREAM_STATE_CONNECTED = 2

MEDIA_STREAM_DIRECTION_NONE = 0
MEDIA_STREAM_DIRECTION_SEND = 1
MEDIA_STREAM_DIRECTION_RECEIVE = 2
MEDIA_STREAM_DIRECTION_BIDIRECTIONAL = 3

FT_STATE_NONE = 0
FT_STATE_PENDING = 1
FT_STATE_ACCEPTED = 2
FT_STATE_OPEN = 3
FT_STATE_COMPLETED = 4
FT_STATE_CANCELLED = 5

FT_STATE_CHANGE_REASON_NONE = 0
FT_STATE_CHANGE_REASON_REQUESTED = 1
FT_STATE_CHANGE_REASON_LOCAL_STOPPED = 2
FT_STATE_CHANGE_REASON_REMOTE_STOPPED = 3
FT_STATE_CHANGE_REASON_LOCAL_ERROR = 4
FT_STATE_CHANGE_REASON_REMOTE_ERROR = 5

FILE_HASH_TYPE_NONE = 0
FILE_HASH_TYPE_MD5 = 1
FILE_HASH_TYPE_SHA1 = 2
FILE_HASH_TYPE_SHA256 = 3

FT_STATE = CHANNEL_TYPE_FILE_TRANSFER + '.State'
FT_CONTENT_TYPE = CHANNEL_TYPE_FILE_TRANSFER + '.ContentType'
FT_FILENAME = CHANNEL_TYPE_FILE_TRANSFER + '.Filename'
FT_SIZE = CHANNEL_TYPE_FILE_TRANSFER + '.Size'
FT_CONTENT_HASH_TYPE = CHANNEL_TYPE_FILE_TRANSFER + '.ContentHashType'
FT_CONTENT_HASH = CHANNEL_TYPE_FILE_TRANSFER + '.ContentHash'
FT_DESCRIPTION = CHANNEL_TYPE_FILE_TRANSFER + '.Description'
FT_DATE = CHANNEL_TYPE_FILE_TRANSFER + '.Date'
FT_AVAILABLE_SOCKET_TYPES = CHANNEL_TYPE_FILE_TRANSFER + '.AvailableSocketTypes'
FT_TRANSFERRED_BYTES = CHANNEL_TYPE_FILE_TRANSFER + '.TransferredBytes'
FT_INITIAL_OFFSET = CHANNEL_TYPE_FILE_TRANSFER + '.InitialOffset'

GF_CAN_ADD = 1
GF_CAN_REMOVE = 2
GF_CAN_RESCIND = 4
GF_MESSAGE_ADD = 8
GF_MESSAGE_REMOVE = 16
GF_MESSAGE_ACCEPT = 32
GF_MESSAGE_REJECT = 64
GF_MESSAGE_RESCIND = 128
GF_CHANNEL_SPECIFIC_HANDLES = 256
GF_ONLY_ONE_GROUP = 512
GF_HANDLE_OWNERS_NOT_AVAILABLE = 1024
GF_PROPERTIES = 2048
GF_MEMBERS_CHANGED_DETAILED = 4096

GC_REASON_NONE = 0
GC_REASON_OFFLINE = 1
GC_REASON_KICKED = 2
GC_REASON_BUSY = 3
GC_REASON_INVITED = 4
GC_REASON_BANNED = 5
GC_REASON_ERROR = 6
GC_REASON_INVALID_CONTACT = 7
GC_REASON_NO_ANSWER = 8
GC_REASON_RENAMED = 9
GC_REASON_PERMISSION_DENIED = 10
GC_REASON_SEPARATED = 11

HS_UNHELD = 0
HS_HELD = 1
HS_PENDING_HOLD = 2
HS_PENDING_UNHOLD = 3

HSR_NONE = 0
HSR_REQUESTED = 1
HSR_RESOURCE_NOT_AVAILABLE = 2

CALL_STATE_RINGING = 1
CALL_STATE_QUEUED = 2
CALL_STATE_HELD = 4
CALL_STATE_FORWARDED = 8

CONN_STATUS_CONNECTED = 0
CONN_STATUS_CONNECTING = 1
CONN_STATUS_DISCONNECTED = 2

CSR_NONE_SPECIFIED = 0
CSR_REQUESTED = 1
CSR_NETWORK_ERROR = 2
CSR_AUTHENTICATION_FAILED = 3
CSR_ENCRYPTION_ERROR = 4
CSR_NAME_IN_USE = 5
CSR_CERT_NOT_PROVIDED = 6
CSR_CERT_UNTRUSTED = 7
CSR_CERT_EXPIRED = 8
CSR_CERT_NOT_ACTIVATED = 9
CSR_CERT_HOSTNAME_MISMATCH = 10
CSR_CERT_FINGERPRINT_MISMATCH = 11
CSR_CERT_SELF_SIGNED = 12
CSR_CERT_OTHER_ERROR = 13

BUDDY_INFO = 'org.laptop.Telepathy.BuddyInfo'
ACTIVITY_PROPERTIES = 'org.laptop.Telepathy.ActivityProperties'
