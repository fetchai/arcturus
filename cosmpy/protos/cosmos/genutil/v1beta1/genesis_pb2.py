# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/genutil/v1beta1/genesis.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cosmos/genutil/v1beta1/genesis.proto',
  package='cosmos.genutil.v1beta1',
  syntax='proto3',
  serialized_options=b'Z,github.com/cosmos/cosmos-sdk/x/genutil/types',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n$cosmos/genutil/v1beta1/genesis.proto\x12\x16\x63osmos.genutil.v1beta1\x1a\x14gogoproto/gogo.proto\"X\n\x0cGenesisState\x12H\n\x07gen_txs\x18\x01 \x03(\x0c\x42\x37\xfa\xde\x1f\x18\x65ncoding/json.RawMessage\xea\xde\x1f\x06gentxs\xf2\xde\x1f\ryaml:\"gentxs\"B.Z,github.com/cosmos/cosmos-sdk/x/genutil/typesb\x06proto3'
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,])




_GENESISSTATE = _descriptor.Descriptor(
  name='GenesisState',
  full_name='cosmos.genutil.v1beta1.GenesisState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='gen_txs', full_name='cosmos.genutil.v1beta1.GenesisState.gen_txs', index=0,
      number=1, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372\336\037\030encoding/json.RawMessage\352\336\037\006gentxs\362\336\037\ryaml:\"gentxs\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=86,
  serialized_end=174,
)

DESCRIPTOR.message_types_by_name['GenesisState'] = _GENESISSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GenesisState = _reflection.GeneratedProtocolMessageType('GenesisState', (_message.Message,), {
  'DESCRIPTOR' : _GENESISSTATE,
  '__module__' : 'cosmos.genutil.v1beta1.genesis_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.genutil.v1beta1.GenesisState)
  })
_sym_db.RegisterMessage(GenesisState)


DESCRIPTOR._options = None
_GENESISSTATE.fields_by_name['gen_txs']._options = None
# @@protoc_insertion_point(module_scope)
