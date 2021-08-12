# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ibc/core/channel/v1/channel.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ibc.core.client.v1 import client_pb2 as ibc_dot_core_dot_client_dot_v1_dot_client__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ibc/core/channel/v1/channel.proto',
  package='ibc.core.channel.v1',
  syntax='proto3',
  serialized_options=b'Z8github.com/cosmos/cosmos-sdk/x/ibc/core/04-channel/types',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n!ibc/core/channel/v1/channel.proto\x12\x13ibc.core.channel.v1\x1a\x14gogoproto/gogo.proto\x1a\x1fibc/core/client/v1/client.proto\"\xed\x01\n\x07\x43hannel\x12)\n\x05state\x18\x01 \x01(\x0e\x32\x1a.ibc.core.channel.v1.State\x12,\n\x08ordering\x18\x02 \x01(\x0e\x32\x1a.ibc.core.channel.v1.Order\x12=\n\x0c\x63ounterparty\x18\x03 \x01(\x0b\x32!.ibc.core.channel.v1.CounterpartyB\x04\xc8\xde\x1f\x00\x12\x33\n\x0f\x63onnection_hops\x18\x04 \x03(\tB\x1a\xf2\xde\x1f\x16yaml:\"connection_hops\"\x12\x0f\n\x07version\x18\x05 \x01(\t:\x04\x88\xa0\x1f\x00\"\x9c\x02\n\x11IdentifiedChannel\x12)\n\x05state\x18\x01 \x01(\x0e\x32\x1a.ibc.core.channel.v1.State\x12,\n\x08ordering\x18\x02 \x01(\x0e\x32\x1a.ibc.core.channel.v1.Order\x12=\n\x0c\x63ounterparty\x18\x03 \x01(\x0b\x32!.ibc.core.channel.v1.CounterpartyB\x04\xc8\xde\x1f\x00\x12\x33\n\x0f\x63onnection_hops\x18\x04 \x03(\tB\x1a\xf2\xde\x1f\x16yaml:\"connection_hops\"\x12\x0f\n\x07version\x18\x05 \x01(\t\x12\x0f\n\x07port_id\x18\x06 \x01(\t\x12\x12\n\nchannel_id\x18\x07 \x01(\t:\x04\x88\xa0\x1f\x00\"d\n\x0c\x43ounterparty\x12#\n\x07port_id\x18\x01 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:\"port_id\"\x12)\n\nchannel_id\x18\x02 \x01(\tB\x15\xf2\xde\x1f\x11yaml:\"channel_id\":\x04\x88\xa0\x1f\x00\"\x8e\x03\n\x06Packet\x12\x10\n\x08sequence\x18\x01 \x01(\x04\x12+\n\x0bsource_port\x18\x02 \x01(\tB\x16\xf2\xde\x1f\x12yaml:\"source_port\"\x12\x31\n\x0esource_channel\x18\x03 \x01(\tB\x19\xf2\xde\x1f\x15yaml:\"source_channel\"\x12\x35\n\x10\x64\x65stination_port\x18\x04 \x01(\tB\x1b\xf2\xde\x1f\x17yaml:\"destination_port\"\x12;\n\x13\x64\x65stination_channel\x18\x05 \x01(\tB\x1e\xf2\xde\x1f\x1ayaml:\"destination_channel\"\x12\x0c\n\x04\x64\x61ta\x18\x06 \x01(\x0c\x12Q\n\x0etimeout_height\x18\x07 \x01(\x0b\x32\x1a.ibc.core.client.v1.HeightB\x1d\xf2\xde\x1f\x15yaml:\"timeout_height\"\xc8\xde\x1f\x00\x12\x37\n\x11timeout_timestamp\x18\x08 \x01(\x04\x42\x1c\xf2\xde\x1f\x18yaml:\"timeout_timestamp\":\x04\x88\xa0\x1f\x00\"\x83\x01\n\x0bPacketState\x12#\n\x07port_id\x18\x01 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:\"port_id\"\x12)\n\nchannel_id\x18\x02 \x01(\tB\x15\xf2\xde\x1f\x11yaml:\"channel_id\"\x12\x10\n\x08sequence\x18\x03 \x01(\x04\x12\x0c\n\x04\x64\x61ta\x18\x04 \x01(\x0c:\x04\x88\xa0\x1f\x00\"@\n\x0f\x41\x63knowledgement\x12\x10\n\x06result\x18\x15 \x01(\x0cH\x00\x12\x0f\n\x05\x65rror\x18\x16 \x01(\tH\x00\x42\n\n\x08response*\xb7\x01\n\x05State\x12\x36\n\x1fSTATE_UNINITIALIZED_UNSPECIFIED\x10\x00\x1a\x11\x8a\x9d \rUNINITIALIZED\x12\x18\n\nSTATE_INIT\x10\x01\x1a\x08\x8a\x9d \x04INIT\x12\x1e\n\rSTATE_TRYOPEN\x10\x02\x1a\x0b\x8a\x9d \x07TRYOPEN\x12\x18\n\nSTATE_OPEN\x10\x03\x1a\x08\x8a\x9d \x04OPEN\x12\x1c\n\x0cSTATE_CLOSED\x10\x04\x1a\n\x8a\x9d \x06\x43LOSED\x1a\x04\x88\xa3\x1e\x00*w\n\x05Order\x12$\n\x16ORDER_NONE_UNSPECIFIED\x10\x00\x1a\x08\x8a\x9d \x04NONE\x12\"\n\x0fORDER_UNORDERED\x10\x01\x1a\r\x8a\x9d \tUNORDERED\x12\x1e\n\rORDER_ORDERED\x10\x02\x1a\x0b\x8a\x9d \x07ORDERED\x1a\x04\x88\xa3\x1e\x00\x42:Z8github.com/cosmos/cosmos-sdk/x/ibc/core/04-channel/typesb\x06proto3'
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,ibc_dot_core_dot_client_dot_v1_dot_client__pb2.DESCRIPTOR,])

_STATE = _descriptor.EnumDescriptor(
  name='State',
  full_name='ibc.core.channel.v1.State',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STATE_UNINITIALIZED_UNSPECIFIED', index=0, number=0,
      serialized_options=b'\212\235 \rUNINITIALIZED',
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STATE_INIT', index=1, number=1,
      serialized_options=b'\212\235 \004INIT',
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STATE_TRYOPEN', index=2, number=2,
      serialized_options=b'\212\235 \007TRYOPEN',
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STATE_OPEN', index=3, number=3,
      serialized_options=b'\212\235 \004OPEN',
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STATE_CLOSED', index=4, number=4,
      serialized_options=b'\212\235 \006CLOSED',
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=b'\210\243\036\000',
  serialized_start=1344,
  serialized_end=1527,
)
_sym_db.RegisterEnumDescriptor(_STATE)

State = enum_type_wrapper.EnumTypeWrapper(_STATE)
_ORDER = _descriptor.EnumDescriptor(
  name='Order',
  full_name='ibc.core.channel.v1.Order',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ORDER_NONE_UNSPECIFIED', index=0, number=0,
      serialized_options=b'\212\235 \004NONE',
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ORDER_UNORDERED', index=1, number=1,
      serialized_options=b'\212\235 \tUNORDERED',
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ORDER_ORDERED', index=2, number=2,
      serialized_options=b'\212\235 \007ORDERED',
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=b'\210\243\036\000',
  serialized_start=1529,
  serialized_end=1648,
)
_sym_db.RegisterEnumDescriptor(_ORDER)

Order = enum_type_wrapper.EnumTypeWrapper(_ORDER)
STATE_UNINITIALIZED_UNSPECIFIED = 0
STATE_INIT = 1
STATE_TRYOPEN = 2
STATE_OPEN = 3
STATE_CLOSED = 4
ORDER_NONE_UNSPECIFIED = 0
ORDER_UNORDERED = 1
ORDER_ORDERED = 2



_CHANNEL = _descriptor.Descriptor(
  name='Channel',
  full_name='ibc.core.channel.v1.Channel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='state', full_name='ibc.core.channel.v1.Channel.state', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ordering', full_name='ibc.core.channel.v1.Channel.ordering', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='counterparty', full_name='ibc.core.channel.v1.Channel.counterparty', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='connection_hops', full_name='ibc.core.channel.v1.Channel.connection_hops', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\026yaml:\"connection_hops\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='version', full_name='ibc.core.channel.v1.Channel.version', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\210\240\037\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=114,
  serialized_end=351,
)


_IDENTIFIEDCHANNEL = _descriptor.Descriptor(
  name='IdentifiedChannel',
  full_name='ibc.core.channel.v1.IdentifiedChannel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='state', full_name='ibc.core.channel.v1.IdentifiedChannel.state', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ordering', full_name='ibc.core.channel.v1.IdentifiedChannel.ordering', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='counterparty', full_name='ibc.core.channel.v1.IdentifiedChannel.counterparty', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='connection_hops', full_name='ibc.core.channel.v1.IdentifiedChannel.connection_hops', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\026yaml:\"connection_hops\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='version', full_name='ibc.core.channel.v1.IdentifiedChannel.version', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='port_id', full_name='ibc.core.channel.v1.IdentifiedChannel.port_id', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='channel_id', full_name='ibc.core.channel.v1.IdentifiedChannel.channel_id', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\210\240\037\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=354,
  serialized_end=638,
)


_COUNTERPARTY = _descriptor.Descriptor(
  name='Counterparty',
  full_name='ibc.core.channel.v1.Counterparty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='port_id', full_name='ibc.core.channel.v1.Counterparty.port_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\016yaml:\"port_id\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='channel_id', full_name='ibc.core.channel.v1.Counterparty.channel_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\021yaml:\"channel_id\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\210\240\037\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=640,
  serialized_end=740,
)


_PACKET = _descriptor.Descriptor(
  name='Packet',
  full_name='ibc.core.channel.v1.Packet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='sequence', full_name='ibc.core.channel.v1.Packet.sequence', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='source_port', full_name='ibc.core.channel.v1.Packet.source_port', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\022yaml:\"source_port\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='source_channel', full_name='ibc.core.channel.v1.Packet.source_channel', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\025yaml:\"source_channel\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='destination_port', full_name='ibc.core.channel.v1.Packet.destination_port', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\027yaml:\"destination_port\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='destination_channel', full_name='ibc.core.channel.v1.Packet.destination_channel', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\032yaml:\"destination_channel\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='ibc.core.channel.v1.Packet.data', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timeout_height', full_name='ibc.core.channel.v1.Packet.timeout_height', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\025yaml:\"timeout_height\"\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timeout_timestamp', full_name='ibc.core.channel.v1.Packet.timeout_timestamp', index=7,
      number=8, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\030yaml:\"timeout_timestamp\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\210\240\037\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=743,
  serialized_end=1141,
)


_PACKETSTATE = _descriptor.Descriptor(
  name='PacketState',
  full_name='ibc.core.channel.v1.PacketState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='port_id', full_name='ibc.core.channel.v1.PacketState.port_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\016yaml:\"port_id\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='channel_id', full_name='ibc.core.channel.v1.PacketState.channel_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\021yaml:\"channel_id\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sequence', full_name='ibc.core.channel.v1.PacketState.sequence', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='ibc.core.channel.v1.PacketState.data', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\210\240\037\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1144,
  serialized_end=1275,
)


_ACKNOWLEDGEMENT = _descriptor.Descriptor(
  name='Acknowledgement',
  full_name='ibc.core.channel.v1.Acknowledgement',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='ibc.core.channel.v1.Acknowledgement.result', index=0,
      number=21, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error', full_name='ibc.core.channel.v1.Acknowledgement.error', index=1,
      number=22, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
    _descriptor.OneofDescriptor(
      name='response', full_name='ibc.core.channel.v1.Acknowledgement.response',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=1277,
  serialized_end=1341,
)

_CHANNEL.fields_by_name['state'].enum_type = _STATE
_CHANNEL.fields_by_name['ordering'].enum_type = _ORDER
_CHANNEL.fields_by_name['counterparty'].message_type = _COUNTERPARTY
_IDENTIFIEDCHANNEL.fields_by_name['state'].enum_type = _STATE
_IDENTIFIEDCHANNEL.fields_by_name['ordering'].enum_type = _ORDER
_IDENTIFIEDCHANNEL.fields_by_name['counterparty'].message_type = _COUNTERPARTY
_PACKET.fields_by_name['timeout_height'].message_type = ibc_dot_core_dot_client_dot_v1_dot_client__pb2._HEIGHT
_ACKNOWLEDGEMENT.oneofs_by_name['response'].fields.append(
  _ACKNOWLEDGEMENT.fields_by_name['result'])
_ACKNOWLEDGEMENT.fields_by_name['result'].containing_oneof = _ACKNOWLEDGEMENT.oneofs_by_name['response']
_ACKNOWLEDGEMENT.oneofs_by_name['response'].fields.append(
  _ACKNOWLEDGEMENT.fields_by_name['error'])
_ACKNOWLEDGEMENT.fields_by_name['error'].containing_oneof = _ACKNOWLEDGEMENT.oneofs_by_name['response']
DESCRIPTOR.message_types_by_name['Channel'] = _CHANNEL
DESCRIPTOR.message_types_by_name['IdentifiedChannel'] = _IDENTIFIEDCHANNEL
DESCRIPTOR.message_types_by_name['Counterparty'] = _COUNTERPARTY
DESCRIPTOR.message_types_by_name['Packet'] = _PACKET
DESCRIPTOR.message_types_by_name['PacketState'] = _PACKETSTATE
DESCRIPTOR.message_types_by_name['Acknowledgement'] = _ACKNOWLEDGEMENT
DESCRIPTOR.enum_types_by_name['State'] = _STATE
DESCRIPTOR.enum_types_by_name['Order'] = _ORDER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Channel = _reflection.GeneratedProtocolMessageType('Channel', (_message.Message,), {
  'DESCRIPTOR' : _CHANNEL,
  '__module__' : 'ibc.core.channel.v1.channel_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.channel.v1.Channel)
  })
_sym_db.RegisterMessage(Channel)

IdentifiedChannel = _reflection.GeneratedProtocolMessageType('IdentifiedChannel', (_message.Message,), {
  'DESCRIPTOR' : _IDENTIFIEDCHANNEL,
  '__module__' : 'ibc.core.channel.v1.channel_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.channel.v1.IdentifiedChannel)
  })
_sym_db.RegisterMessage(IdentifiedChannel)

Counterparty = _reflection.GeneratedProtocolMessageType('Counterparty', (_message.Message,), {
  'DESCRIPTOR' : _COUNTERPARTY,
  '__module__' : 'ibc.core.channel.v1.channel_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.channel.v1.Counterparty)
  })
_sym_db.RegisterMessage(Counterparty)

Packet = _reflection.GeneratedProtocolMessageType('Packet', (_message.Message,), {
  'DESCRIPTOR' : _PACKET,
  '__module__' : 'ibc.core.channel.v1.channel_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.channel.v1.Packet)
  })
_sym_db.RegisterMessage(Packet)

PacketState = _reflection.GeneratedProtocolMessageType('PacketState', (_message.Message,), {
  'DESCRIPTOR' : _PACKETSTATE,
  '__module__' : 'ibc.core.channel.v1.channel_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.channel.v1.PacketState)
  })
_sym_db.RegisterMessage(PacketState)

Acknowledgement = _reflection.GeneratedProtocolMessageType('Acknowledgement', (_message.Message,), {
  'DESCRIPTOR' : _ACKNOWLEDGEMENT,
  '__module__' : 'ibc.core.channel.v1.channel_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.channel.v1.Acknowledgement)
  })
_sym_db.RegisterMessage(Acknowledgement)


DESCRIPTOR._options = None
_STATE._options = None
_STATE.values_by_name["STATE_UNINITIALIZED_UNSPECIFIED"]._options = None
_STATE.values_by_name["STATE_INIT"]._options = None
_STATE.values_by_name["STATE_TRYOPEN"]._options = None
_STATE.values_by_name["STATE_OPEN"]._options = None
_STATE.values_by_name["STATE_CLOSED"]._options = None
_ORDER._options = None
_ORDER.values_by_name["ORDER_NONE_UNSPECIFIED"]._options = None
_ORDER.values_by_name["ORDER_UNORDERED"]._options = None
_ORDER.values_by_name["ORDER_ORDERED"]._options = None
_CHANNEL.fields_by_name['counterparty']._options = None
_CHANNEL.fields_by_name['connection_hops']._options = None
_CHANNEL._options = None
_IDENTIFIEDCHANNEL.fields_by_name['counterparty']._options = None
_IDENTIFIEDCHANNEL.fields_by_name['connection_hops']._options = None
_IDENTIFIEDCHANNEL._options = None
_COUNTERPARTY.fields_by_name['port_id']._options = None
_COUNTERPARTY.fields_by_name['channel_id']._options = None
_COUNTERPARTY._options = None
_PACKET.fields_by_name['source_port']._options = None
_PACKET.fields_by_name['source_channel']._options = None
_PACKET.fields_by_name['destination_port']._options = None
_PACKET.fields_by_name['destination_channel']._options = None
_PACKET.fields_by_name['timeout_height']._options = None
_PACKET.fields_by_name['timeout_timestamp']._options = None
_PACKET._options = None
_PACKETSTATE.fields_by_name['port_id']._options = None
_PACKETSTATE.fields_by_name['channel_id']._options = None
_PACKETSTATE._options = None
# @@protoc_insertion_point(module_scope)
