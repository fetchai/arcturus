# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tendermint/p2p/types.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tendermint/p2p/types.proto',
  package='tendermint.p2p',
  syntax='proto3',
  serialized_options=b'Z5github.com/tendermint/tendermint/proto/tendermint/p2p',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1atendermint/p2p/types.proto\x12\x0etendermint.p2p\x1a\x14gogoproto/gogo.proto\"B\n\nNetAddress\x12\x12\n\x02id\x18\x01 \x01(\tB\x06\xe2\xde\x1f\x02ID\x12\x12\n\x02ip\x18\x02 \x01(\tB\x06\xe2\xde\x1f\x02IP\x12\x0c\n\x04port\x18\x03 \x01(\r\"C\n\x0fProtocolVersion\x12\x14\n\x03p2p\x18\x01 \x01(\x04\x42\x07\xe2\xde\x1f\x03P2P\x12\r\n\x05\x62lock\x18\x02 \x01(\x04\x12\x0b\n\x03\x61pp\x18\x03 \x01(\x04\"\x93\x02\n\x0f\x44\x65\x66\x61ultNodeInfo\x12?\n\x10protocol_version\x18\x01 \x01(\x0b\x32\x1f.tendermint.p2p.ProtocolVersionB\x04\xc8\xde\x1f\x00\x12*\n\x0f\x64\x65\x66\x61ult_node_id\x18\x02 \x01(\tB\x11\xe2\xde\x1f\rDefaultNodeID\x12\x13\n\x0blisten_addr\x18\x03 \x01(\t\x12\x0f\n\x07network\x18\x04 \x01(\t\x12\x0f\n\x07version\x18\x05 \x01(\t\x12\x10\n\x08\x63hannels\x18\x06 \x01(\x0c\x12\x0f\n\x07moniker\x18\x07 \x01(\t\x12\x39\n\x05other\x18\x08 \x01(\x0b\x32$.tendermint.p2p.DefaultNodeInfoOtherB\x04\xc8\xde\x1f\x00\"M\n\x14\x44\x65\x66\x61ultNodeInfoOther\x12\x10\n\x08tx_index\x18\x01 \x01(\t\x12#\n\x0brpc_address\x18\x02 \x01(\tB\x0e\xe2\xde\x1f\nRPCAddressB7Z5github.com/tendermint/tendermint/proto/tendermint/p2pb\x06proto3'
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,])




_NETADDRESS = _descriptor.Descriptor(
  name='NetAddress',
  full_name='tendermint.p2p.NetAddress',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='tendermint.p2p.NetAddress.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342\336\037\002ID', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ip', full_name='tendermint.p2p.NetAddress.ip', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342\336\037\002IP', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='port', full_name='tendermint.p2p.NetAddress.port', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=68,
  serialized_end=134,
)


_PROTOCOLVERSION = _descriptor.Descriptor(
  name='ProtocolVersion',
  full_name='tendermint.p2p.ProtocolVersion',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='p2p', full_name='tendermint.p2p.ProtocolVersion.p2p', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342\336\037\003P2P', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='block', full_name='tendermint.p2p.ProtocolVersion.block', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='app', full_name='tendermint.p2p.ProtocolVersion.app', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=136,
  serialized_end=203,
)


_DEFAULTNODEINFO = _descriptor.Descriptor(
  name='DefaultNodeInfo',
  full_name='tendermint.p2p.DefaultNodeInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='protocol_version', full_name='tendermint.p2p.DefaultNodeInfo.protocol_version', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='default_node_id', full_name='tendermint.p2p.DefaultNodeInfo.default_node_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342\336\037\rDefaultNodeID', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='listen_addr', full_name='tendermint.p2p.DefaultNodeInfo.listen_addr', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='network', full_name='tendermint.p2p.DefaultNodeInfo.network', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='version', full_name='tendermint.p2p.DefaultNodeInfo.version', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='channels', full_name='tendermint.p2p.DefaultNodeInfo.channels', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='moniker', full_name='tendermint.p2p.DefaultNodeInfo.moniker', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='other', full_name='tendermint.p2p.DefaultNodeInfo.other', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=206,
  serialized_end=481,
)


_DEFAULTNODEINFOOTHER = _descriptor.Descriptor(
  name='DefaultNodeInfoOther',
  full_name='tendermint.p2p.DefaultNodeInfoOther',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tx_index', full_name='tendermint.p2p.DefaultNodeInfoOther.tx_index', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rpc_address', full_name='tendermint.p2p.DefaultNodeInfoOther.rpc_address', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342\336\037\nRPCAddress', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=483,
  serialized_end=560,
)

_DEFAULTNODEINFO.fields_by_name['protocol_version'].message_type = _PROTOCOLVERSION
_DEFAULTNODEINFO.fields_by_name['other'].message_type = _DEFAULTNODEINFOOTHER
DESCRIPTOR.message_types_by_name['NetAddress'] = _NETADDRESS
DESCRIPTOR.message_types_by_name['ProtocolVersion'] = _PROTOCOLVERSION
DESCRIPTOR.message_types_by_name['DefaultNodeInfo'] = _DEFAULTNODEINFO
DESCRIPTOR.message_types_by_name['DefaultNodeInfoOther'] = _DEFAULTNODEINFOOTHER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NetAddress = _reflection.GeneratedProtocolMessageType('NetAddress', (_message.Message,), {
  'DESCRIPTOR' : _NETADDRESS,
  '__module__' : 'tendermint.p2p.types_pb2'
  # @@protoc_insertion_point(class_scope:tendermint.p2p.NetAddress)
  })
_sym_db.RegisterMessage(NetAddress)

ProtocolVersion = _reflection.GeneratedProtocolMessageType('ProtocolVersion', (_message.Message,), {
  'DESCRIPTOR' : _PROTOCOLVERSION,
  '__module__' : 'tendermint.p2p.types_pb2'
  # @@protoc_insertion_point(class_scope:tendermint.p2p.ProtocolVersion)
  })
_sym_db.RegisterMessage(ProtocolVersion)

DefaultNodeInfo = _reflection.GeneratedProtocolMessageType('DefaultNodeInfo', (_message.Message,), {
  'DESCRIPTOR' : _DEFAULTNODEINFO,
  '__module__' : 'tendermint.p2p.types_pb2'
  # @@protoc_insertion_point(class_scope:tendermint.p2p.DefaultNodeInfo)
  })
_sym_db.RegisterMessage(DefaultNodeInfo)

DefaultNodeInfoOther = _reflection.GeneratedProtocolMessageType('DefaultNodeInfoOther', (_message.Message,), {
  'DESCRIPTOR' : _DEFAULTNODEINFOOTHER,
  '__module__' : 'tendermint.p2p.types_pb2'
  # @@protoc_insertion_point(class_scope:tendermint.p2p.DefaultNodeInfoOther)
  })
_sym_db.RegisterMessage(DefaultNodeInfoOther)


DESCRIPTOR._options = None
_NETADDRESS.fields_by_name['id']._options = None
_NETADDRESS.fields_by_name['ip']._options = None
_PROTOCOLVERSION.fields_by_name['p2p']._options = None
_DEFAULTNODEINFO.fields_by_name['protocol_version']._options = None
_DEFAULTNODEINFO.fields_by_name['default_node_id']._options = None
_DEFAULTNODEINFO.fields_by_name['other']._options = None
_DEFAULTNODEINFOOTHER.fields_by_name['rpc_address']._options = None
# @@protoc_insertion_point(module_scope)
