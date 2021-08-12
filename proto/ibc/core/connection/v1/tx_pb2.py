# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ibc/core/connection/v1/tx.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from ibc.core.client.v1 import client_pb2 as ibc_dot_core_dot_client_dot_v1_dot_client__pb2
from ibc.core.connection.v1 import connection_pb2 as ibc_dot_core_dot_connection_dot_v1_dot_connection__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ibc/core/connection/v1/tx.proto',
  package='ibc.core.connection.v1',
  syntax='proto3',
  serialized_options=b'Z;github.com/cosmos/cosmos-sdk/x/ibc/core/03-connection/types',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1fibc/core/connection/v1/tx.proto\x12\x16ibc.core.connection.v1\x1a\x14gogoproto/gogo.proto\x1a\x19google/protobuf/any.proto\x1a\x1fibc/core/client/v1/client.proto\x1a\'ibc/core/connection/v1/connection.proto\"\xfd\x01\n\x15MsgConnectionOpenInit\x12\'\n\tclient_id\x18\x01 \x01(\tB\x14\xf2\xde\x1f\x10yaml:\"client_id\"\x12@\n\x0c\x63ounterparty\x18\x02 \x01(\x0b\x32$.ibc.core.connection.v1.CounterpartyB\x04\xc8\xde\x1f\x00\x12\x30\n\x07version\x18\x03 \x01(\x0b\x32\x1f.ibc.core.connection.v1.Version\x12-\n\x0c\x64\x65lay_period\x18\x04 \x01(\x04\x42\x17\xf2\xde\x1f\x13yaml:\"delay_period\"\x12\x0e\n\x06signer\x18\x05 \x01(\t:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"\x1f\n\x1dMsgConnectionOpenInitResponse\"\xe9\x05\n\x14MsgConnectionOpenTry\x12\'\n\tclient_id\x18\x01 \x01(\tB\x14\xf2\xde\x1f\x10yaml:\"client_id\"\x12\x41\n\x16previous_connection_id\x18\x02 \x01(\tB!\xf2\xde\x1f\x1dyaml:\"previous_connection_id\"\x12\x43\n\x0c\x63lient_state\x18\x03 \x01(\x0b\x32\x14.google.protobuf.AnyB\x17\xf2\xde\x1f\x13yaml:\"client_state\"\x12@\n\x0c\x63ounterparty\x18\x04 \x01(\x0b\x32$.ibc.core.connection.v1.CounterpartyB\x04\xc8\xde\x1f\x00\x12-\n\x0c\x64\x65lay_period\x18\x05 \x01(\x04\x42\x17\xf2\xde\x1f\x13yaml:\"delay_period\"\x12`\n\x15\x63ounterparty_versions\x18\x06 \x03(\x0b\x32\x1f.ibc.core.connection.v1.VersionB \xf2\xde\x1f\x1cyaml:\"counterparty_versions\"\x12M\n\x0cproof_height\x18\x07 \x01(\x0b\x32\x1a.ibc.core.client.v1.HeightB\x1b\xf2\xde\x1f\x13yaml:\"proof_height\"\xc8\xde\x1f\x00\x12)\n\nproof_init\x18\x08 \x01(\x0c\x42\x15\xf2\xde\x1f\x11yaml:\"proof_init\"\x12-\n\x0cproof_client\x18\t \x01(\x0c\x42\x17\xf2\xde\x1f\x13yaml:\"proof_client\"\x12\x33\n\x0fproof_consensus\x18\n \x01(\x0c\x42\x1a\xf2\xde\x1f\x16yaml:\"proof_consensus\"\x12U\n\x10\x63onsensus_height\x18\x0b \x01(\x0b\x32\x1a.ibc.core.client.v1.HeightB\x1f\xf2\xde\x1f\x17yaml:\"consensus_height\"\xc8\xde\x1f\x00\x12\x0e\n\x06signer\x18\x0c \x01(\t:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"\x1e\n\x1cMsgConnectionOpenTryResponse\"\xd6\x04\n\x14MsgConnectionOpenAck\x12/\n\rconnection_id\x18\x01 \x01(\tB\x18\xf2\xde\x1f\x14yaml:\"connection_id\"\x12I\n\x1a\x63ounterparty_connection_id\x18\x02 \x01(\tB%\xf2\xde\x1f!yaml:\"counterparty_connection_id\"\x12\x30\n\x07version\x18\x03 \x01(\x0b\x32\x1f.ibc.core.connection.v1.Version\x12\x43\n\x0c\x63lient_state\x18\x04 \x01(\x0b\x32\x14.google.protobuf.AnyB\x17\xf2\xde\x1f\x13yaml:\"client_state\"\x12M\n\x0cproof_height\x18\x05 \x01(\x0b\x32\x1a.ibc.core.client.v1.HeightB\x1b\xf2\xde\x1f\x13yaml:\"proof_height\"\xc8\xde\x1f\x00\x12\'\n\tproof_try\x18\x06 \x01(\x0c\x42\x14\xf2\xde\x1f\x10yaml:\"proof_try\"\x12-\n\x0cproof_client\x18\x07 \x01(\x0c\x42\x17\xf2\xde\x1f\x13yaml:\"proof_client\"\x12\x33\n\x0fproof_consensus\x18\x08 \x01(\x0c\x42\x1a\xf2\xde\x1f\x16yaml:\"proof_consensus\"\x12U\n\x10\x63onsensus_height\x18\t \x01(\x0b\x32\x1a.ibc.core.client.v1.HeightB\x1f\xf2\xde\x1f\x17yaml:\"consensus_height\"\xc8\xde\x1f\x00\x12\x0e\n\x06signer\x18\n \x01(\t:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"\x1e\n\x1cMsgConnectionOpenAckResponse\"\xdd\x01\n\x18MsgConnectionOpenConfirm\x12/\n\rconnection_id\x18\x01 \x01(\tB\x18\xf2\xde\x1f\x14yaml:\"connection_id\"\x12\'\n\tproof_ack\x18\x02 \x01(\x0c\x42\x14\xf2\xde\x1f\x10yaml:\"proof_ack\"\x12M\n\x0cproof_height\x18\x03 \x01(\x0b\x32\x1a.ibc.core.client.v1.HeightB\x1b\xf2\xde\x1f\x13yaml:\"proof_height\"\xc8\xde\x1f\x00\x12\x0e\n\x06signer\x18\x04 \x01(\t:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"\"\n MsgConnectionOpenConfirmResponse2\xf9\x03\n\x03Msg\x12z\n\x12\x43onnectionOpenInit\x12-.ibc.core.connection.v1.MsgConnectionOpenInit\x1a\x35.ibc.core.connection.v1.MsgConnectionOpenInitResponse\x12w\n\x11\x43onnectionOpenTry\x12,.ibc.core.connection.v1.MsgConnectionOpenTry\x1a\x34.ibc.core.connection.v1.MsgConnectionOpenTryResponse\x12w\n\x11\x43onnectionOpenAck\x12,.ibc.core.connection.v1.MsgConnectionOpenAck\x1a\x34.ibc.core.connection.v1.MsgConnectionOpenAckResponse\x12\x83\x01\n\x15\x43onnectionOpenConfirm\x12\x30.ibc.core.connection.v1.MsgConnectionOpenConfirm\x1a\x38.ibc.core.connection.v1.MsgConnectionOpenConfirmResponseB=Z;github.com/cosmos/cosmos-sdk/x/ibc/core/03-connection/typesb\x06proto3'
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,google_dot_protobuf_dot_any__pb2.DESCRIPTOR,ibc_dot_core_dot_client_dot_v1_dot_client__pb2.DESCRIPTOR,ibc_dot_core_dot_connection_dot_v1_dot_connection__pb2.DESCRIPTOR,])




_MSGCONNECTIONOPENINIT = _descriptor.Descriptor(
  name='MsgConnectionOpenInit',
  full_name='ibc.core.connection.v1.MsgConnectionOpenInit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='client_id', full_name='ibc.core.connection.v1.MsgConnectionOpenInit.client_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\020yaml:\"client_id\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='counterparty', full_name='ibc.core.connection.v1.MsgConnectionOpenInit.counterparty', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='version', full_name='ibc.core.connection.v1.MsgConnectionOpenInit.version', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='delay_period', full_name='ibc.core.connection.v1.MsgConnectionOpenInit.delay_period', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\023yaml:\"delay_period\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='signer', full_name='ibc.core.connection.v1.MsgConnectionOpenInit.signer', index=4,
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
  serialized_options=b'\350\240\037\000\210\240\037\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=183,
  serialized_end=436,
)


_MSGCONNECTIONOPENINITRESPONSE = _descriptor.Descriptor(
  name='MsgConnectionOpenInitResponse',
  full_name='ibc.core.connection.v1.MsgConnectionOpenInitResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=438,
  serialized_end=469,
)


_MSGCONNECTIONOPENTRY = _descriptor.Descriptor(
  name='MsgConnectionOpenTry',
  full_name='ibc.core.connection.v1.MsgConnectionOpenTry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='client_id', full_name='ibc.core.connection.v1.MsgConnectionOpenTry.client_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\020yaml:\"client_id\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='previous_connection_id', full_name='ibc.core.connection.v1.MsgConnectionOpenTry.previous_connection_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\035yaml:\"previous_connection_id\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='client_state', full_name='ibc.core.connection.v1.MsgConnectionOpenTry.client_state', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\023yaml:\"client_state\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='counterparty', full_name='ibc.core.connection.v1.MsgConnectionOpenTry.counterparty', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='delay_period', full_name='ibc.core.connection.v1.MsgConnectionOpenTry.delay_period', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\023yaml:\"delay_period\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='counterparty_versions', full_name='ibc.core.connection.v1.MsgConnectionOpenTry.counterparty_versions', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\034yaml:\"counterparty_versions\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='proof_height', full_name='ibc.core.connection.v1.MsgConnectionOpenTry.proof_height', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\023yaml:\"proof_height\"\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='proof_init', full_name='ibc.core.connection.v1.MsgConnectionOpenTry.proof_init', index=7,
      number=8, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\021yaml:\"proof_init\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='proof_client', full_name='ibc.core.connection.v1.MsgConnectionOpenTry.proof_client', index=8,
      number=9, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\023yaml:\"proof_client\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='proof_consensus', full_name='ibc.core.connection.v1.MsgConnectionOpenTry.proof_consensus', index=9,
      number=10, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\026yaml:\"proof_consensus\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='consensus_height', full_name='ibc.core.connection.v1.MsgConnectionOpenTry.consensus_height', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\027yaml:\"consensus_height\"\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='signer', full_name='ibc.core.connection.v1.MsgConnectionOpenTry.signer', index=11,
      number=12, type=9, cpp_type=9, label=1,
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
  serialized_options=b'\350\240\037\000\210\240\037\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=472,
  serialized_end=1217,
)


_MSGCONNECTIONOPENTRYRESPONSE = _descriptor.Descriptor(
  name='MsgConnectionOpenTryResponse',
  full_name='ibc.core.connection.v1.MsgConnectionOpenTryResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=1219,
  serialized_end=1249,
)


_MSGCONNECTIONOPENACK = _descriptor.Descriptor(
  name='MsgConnectionOpenAck',
  full_name='ibc.core.connection.v1.MsgConnectionOpenAck',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='connection_id', full_name='ibc.core.connection.v1.MsgConnectionOpenAck.connection_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\024yaml:\"connection_id\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='counterparty_connection_id', full_name='ibc.core.connection.v1.MsgConnectionOpenAck.counterparty_connection_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037!yaml:\"counterparty_connection_id\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='version', full_name='ibc.core.connection.v1.MsgConnectionOpenAck.version', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='client_state', full_name='ibc.core.connection.v1.MsgConnectionOpenAck.client_state', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\023yaml:\"client_state\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='proof_height', full_name='ibc.core.connection.v1.MsgConnectionOpenAck.proof_height', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\023yaml:\"proof_height\"\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='proof_try', full_name='ibc.core.connection.v1.MsgConnectionOpenAck.proof_try', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\020yaml:\"proof_try\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='proof_client', full_name='ibc.core.connection.v1.MsgConnectionOpenAck.proof_client', index=6,
      number=7, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\023yaml:\"proof_client\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='proof_consensus', full_name='ibc.core.connection.v1.MsgConnectionOpenAck.proof_consensus', index=7,
      number=8, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\026yaml:\"proof_consensus\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='consensus_height', full_name='ibc.core.connection.v1.MsgConnectionOpenAck.consensus_height', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\027yaml:\"consensus_height\"\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='signer', full_name='ibc.core.connection.v1.MsgConnectionOpenAck.signer', index=9,
      number=10, type=9, cpp_type=9, label=1,
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
  serialized_options=b'\350\240\037\000\210\240\037\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1252,
  serialized_end=1850,
)


_MSGCONNECTIONOPENACKRESPONSE = _descriptor.Descriptor(
  name='MsgConnectionOpenAckResponse',
  full_name='ibc.core.connection.v1.MsgConnectionOpenAckResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=1852,
  serialized_end=1882,
)


_MSGCONNECTIONOPENCONFIRM = _descriptor.Descriptor(
  name='MsgConnectionOpenConfirm',
  full_name='ibc.core.connection.v1.MsgConnectionOpenConfirm',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='connection_id', full_name='ibc.core.connection.v1.MsgConnectionOpenConfirm.connection_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\024yaml:\"connection_id\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='proof_ack', full_name='ibc.core.connection.v1.MsgConnectionOpenConfirm.proof_ack', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\020yaml:\"proof_ack\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='proof_height', full_name='ibc.core.connection.v1.MsgConnectionOpenConfirm.proof_height', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\023yaml:\"proof_height\"\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='signer', full_name='ibc.core.connection.v1.MsgConnectionOpenConfirm.signer', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_options=b'\350\240\037\000\210\240\037\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1885,
  serialized_end=2106,
)


_MSGCONNECTIONOPENCONFIRMRESPONSE = _descriptor.Descriptor(
  name='MsgConnectionOpenConfirmResponse',
  full_name='ibc.core.connection.v1.MsgConnectionOpenConfirmResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=2108,
  serialized_end=2142,
)

_MSGCONNECTIONOPENINIT.fields_by_name['counterparty'].message_type = ibc_dot_core_dot_connection_dot_v1_dot_connection__pb2._COUNTERPARTY
_MSGCONNECTIONOPENINIT.fields_by_name['version'].message_type = ibc_dot_core_dot_connection_dot_v1_dot_connection__pb2._VERSION
_MSGCONNECTIONOPENTRY.fields_by_name['client_state'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_MSGCONNECTIONOPENTRY.fields_by_name['counterparty'].message_type = ibc_dot_core_dot_connection_dot_v1_dot_connection__pb2._COUNTERPARTY
_MSGCONNECTIONOPENTRY.fields_by_name['counterparty_versions'].message_type = ibc_dot_core_dot_connection_dot_v1_dot_connection__pb2._VERSION
_MSGCONNECTIONOPENTRY.fields_by_name['proof_height'].message_type = ibc_dot_core_dot_client_dot_v1_dot_client__pb2._HEIGHT
_MSGCONNECTIONOPENTRY.fields_by_name['consensus_height'].message_type = ibc_dot_core_dot_client_dot_v1_dot_client__pb2._HEIGHT
_MSGCONNECTIONOPENACK.fields_by_name['version'].message_type = ibc_dot_core_dot_connection_dot_v1_dot_connection__pb2._VERSION
_MSGCONNECTIONOPENACK.fields_by_name['client_state'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_MSGCONNECTIONOPENACK.fields_by_name['proof_height'].message_type = ibc_dot_core_dot_client_dot_v1_dot_client__pb2._HEIGHT
_MSGCONNECTIONOPENACK.fields_by_name['consensus_height'].message_type = ibc_dot_core_dot_client_dot_v1_dot_client__pb2._HEIGHT
_MSGCONNECTIONOPENCONFIRM.fields_by_name['proof_height'].message_type = ibc_dot_core_dot_client_dot_v1_dot_client__pb2._HEIGHT
DESCRIPTOR.message_types_by_name['MsgConnectionOpenInit'] = _MSGCONNECTIONOPENINIT
DESCRIPTOR.message_types_by_name['MsgConnectionOpenInitResponse'] = _MSGCONNECTIONOPENINITRESPONSE
DESCRIPTOR.message_types_by_name['MsgConnectionOpenTry'] = _MSGCONNECTIONOPENTRY
DESCRIPTOR.message_types_by_name['MsgConnectionOpenTryResponse'] = _MSGCONNECTIONOPENTRYRESPONSE
DESCRIPTOR.message_types_by_name['MsgConnectionOpenAck'] = _MSGCONNECTIONOPENACK
DESCRIPTOR.message_types_by_name['MsgConnectionOpenAckResponse'] = _MSGCONNECTIONOPENACKRESPONSE
DESCRIPTOR.message_types_by_name['MsgConnectionOpenConfirm'] = _MSGCONNECTIONOPENCONFIRM
DESCRIPTOR.message_types_by_name['MsgConnectionOpenConfirmResponse'] = _MSGCONNECTIONOPENCONFIRMRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MsgConnectionOpenInit = _reflection.GeneratedProtocolMessageType('MsgConnectionOpenInit', (_message.Message,), {
  'DESCRIPTOR' : _MSGCONNECTIONOPENINIT,
  '__module__' : 'ibc.core.connection.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.connection.v1.MsgConnectionOpenInit)
  })
_sym_db.RegisterMessage(MsgConnectionOpenInit)

MsgConnectionOpenInitResponse = _reflection.GeneratedProtocolMessageType('MsgConnectionOpenInitResponse', (_message.Message,), {
  'DESCRIPTOR' : _MSGCONNECTIONOPENINITRESPONSE,
  '__module__' : 'ibc.core.connection.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.connection.v1.MsgConnectionOpenInitResponse)
  })
_sym_db.RegisterMessage(MsgConnectionOpenInitResponse)

MsgConnectionOpenTry = _reflection.GeneratedProtocolMessageType('MsgConnectionOpenTry', (_message.Message,), {
  'DESCRIPTOR' : _MSGCONNECTIONOPENTRY,
  '__module__' : 'ibc.core.connection.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.connection.v1.MsgConnectionOpenTry)
  })
_sym_db.RegisterMessage(MsgConnectionOpenTry)

MsgConnectionOpenTryResponse = _reflection.GeneratedProtocolMessageType('MsgConnectionOpenTryResponse', (_message.Message,), {
  'DESCRIPTOR' : _MSGCONNECTIONOPENTRYRESPONSE,
  '__module__' : 'ibc.core.connection.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.connection.v1.MsgConnectionOpenTryResponse)
  })
_sym_db.RegisterMessage(MsgConnectionOpenTryResponse)

MsgConnectionOpenAck = _reflection.GeneratedProtocolMessageType('MsgConnectionOpenAck', (_message.Message,), {
  'DESCRIPTOR' : _MSGCONNECTIONOPENACK,
  '__module__' : 'ibc.core.connection.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.connection.v1.MsgConnectionOpenAck)
  })
_sym_db.RegisterMessage(MsgConnectionOpenAck)

MsgConnectionOpenAckResponse = _reflection.GeneratedProtocolMessageType('MsgConnectionOpenAckResponse', (_message.Message,), {
  'DESCRIPTOR' : _MSGCONNECTIONOPENACKRESPONSE,
  '__module__' : 'ibc.core.connection.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.connection.v1.MsgConnectionOpenAckResponse)
  })
_sym_db.RegisterMessage(MsgConnectionOpenAckResponse)

MsgConnectionOpenConfirm = _reflection.GeneratedProtocolMessageType('MsgConnectionOpenConfirm', (_message.Message,), {
  'DESCRIPTOR' : _MSGCONNECTIONOPENCONFIRM,
  '__module__' : 'ibc.core.connection.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.connection.v1.MsgConnectionOpenConfirm)
  })
_sym_db.RegisterMessage(MsgConnectionOpenConfirm)

MsgConnectionOpenConfirmResponse = _reflection.GeneratedProtocolMessageType('MsgConnectionOpenConfirmResponse', (_message.Message,), {
  'DESCRIPTOR' : _MSGCONNECTIONOPENCONFIRMRESPONSE,
  '__module__' : 'ibc.core.connection.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.connection.v1.MsgConnectionOpenConfirmResponse)
  })
_sym_db.RegisterMessage(MsgConnectionOpenConfirmResponse)


DESCRIPTOR._options = None
_MSGCONNECTIONOPENINIT.fields_by_name['client_id']._options = None
_MSGCONNECTIONOPENINIT.fields_by_name['counterparty']._options = None
_MSGCONNECTIONOPENINIT.fields_by_name['delay_period']._options = None
_MSGCONNECTIONOPENINIT._options = None
_MSGCONNECTIONOPENTRY.fields_by_name['client_id']._options = None
_MSGCONNECTIONOPENTRY.fields_by_name['previous_connection_id']._options = None
_MSGCONNECTIONOPENTRY.fields_by_name['client_state']._options = None
_MSGCONNECTIONOPENTRY.fields_by_name['counterparty']._options = None
_MSGCONNECTIONOPENTRY.fields_by_name['delay_period']._options = None
_MSGCONNECTIONOPENTRY.fields_by_name['counterparty_versions']._options = None
_MSGCONNECTIONOPENTRY.fields_by_name['proof_height']._options = None
_MSGCONNECTIONOPENTRY.fields_by_name['proof_init']._options = None
_MSGCONNECTIONOPENTRY.fields_by_name['proof_client']._options = None
_MSGCONNECTIONOPENTRY.fields_by_name['proof_consensus']._options = None
_MSGCONNECTIONOPENTRY.fields_by_name['consensus_height']._options = None
_MSGCONNECTIONOPENTRY._options = None
_MSGCONNECTIONOPENACK.fields_by_name['connection_id']._options = None
_MSGCONNECTIONOPENACK.fields_by_name['counterparty_connection_id']._options = None
_MSGCONNECTIONOPENACK.fields_by_name['client_state']._options = None
_MSGCONNECTIONOPENACK.fields_by_name['proof_height']._options = None
_MSGCONNECTIONOPENACK.fields_by_name['proof_try']._options = None
_MSGCONNECTIONOPENACK.fields_by_name['proof_client']._options = None
_MSGCONNECTIONOPENACK.fields_by_name['proof_consensus']._options = None
_MSGCONNECTIONOPENACK.fields_by_name['consensus_height']._options = None
_MSGCONNECTIONOPENACK._options = None
_MSGCONNECTIONOPENCONFIRM.fields_by_name['connection_id']._options = None
_MSGCONNECTIONOPENCONFIRM.fields_by_name['proof_ack']._options = None
_MSGCONNECTIONOPENCONFIRM.fields_by_name['proof_height']._options = None
_MSGCONNECTIONOPENCONFIRM._options = None

_MSG = _descriptor.ServiceDescriptor(
  name='Msg',
  full_name='ibc.core.connection.v1.Msg',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=2145,
  serialized_end=2650,
  methods=[
  _descriptor.MethodDescriptor(
    name='ConnectionOpenInit',
    full_name='ibc.core.connection.v1.Msg.ConnectionOpenInit',
    index=0,
    containing_service=None,
    input_type=_MSGCONNECTIONOPENINIT,
    output_type=_MSGCONNECTIONOPENINITRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ConnectionOpenTry',
    full_name='ibc.core.connection.v1.Msg.ConnectionOpenTry',
    index=1,
    containing_service=None,
    input_type=_MSGCONNECTIONOPENTRY,
    output_type=_MSGCONNECTIONOPENTRYRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ConnectionOpenAck',
    full_name='ibc.core.connection.v1.Msg.ConnectionOpenAck',
    index=2,
    containing_service=None,
    input_type=_MSGCONNECTIONOPENACK,
    output_type=_MSGCONNECTIONOPENACKRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ConnectionOpenConfirm',
    full_name='ibc.core.connection.v1.Msg.ConnectionOpenConfirm',
    index=3,
    containing_service=None,
    input_type=_MSGCONNECTIONOPENCONFIRM,
    output_type=_MSGCONNECTIONOPENCONFIRMRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MSG)

DESCRIPTOR.services_by_name['Msg'] = _MSG

# @@protoc_insertion_point(module_scope)
