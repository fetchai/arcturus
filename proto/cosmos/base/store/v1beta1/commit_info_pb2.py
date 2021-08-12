# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/base/store/v1beta1/commit_info.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cosmos/base/store/v1beta1/commit_info.proto',
  package='cosmos.base.store.v1beta1',
  syntax='proto3',
  serialized_options=b'Z(github.com/cosmos/cosmos-sdk/store/types',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n+cosmos/base/store/v1beta1/commit_info.proto\x12\x19\x63osmos.base.store.v1beta1\x1a\x14gogoproto/gogo.proto\"^\n\nCommitInfo\x12\x0f\n\x07version\x18\x01 \x01(\x03\x12?\n\x0bstore_infos\x18\x02 \x03(\x0b\x32$.cosmos.base.store.v1beta1.StoreInfoB\x04\xc8\xde\x1f\x00\"W\n\tStoreInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12<\n\tcommit_id\x18\x02 \x01(\x0b\x32#.cosmos.base.store.v1beta1.CommitIDB\x04\xc8\xde\x1f\x00\"/\n\x08\x43ommitID\x12\x0f\n\x07version\x18\x01 \x01(\x03\x12\x0c\n\x04hash\x18\x02 \x01(\x0c:\x04\x98\xa0\x1f\x00\x42*Z(github.com/cosmos/cosmos-sdk/store/typesb\x06proto3'
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,])




_COMMITINFO = _descriptor.Descriptor(
  name='CommitInfo',
  full_name='cosmos.base.store.v1beta1.CommitInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='cosmos.base.store.v1beta1.CommitInfo.version', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='store_infos', full_name='cosmos.base.store.v1beta1.CommitInfo.store_infos', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=96,
  serialized_end=190,
)


_STOREINFO = _descriptor.Descriptor(
  name='StoreInfo',
  full_name='cosmos.base.store.v1beta1.StoreInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='cosmos.base.store.v1beta1.StoreInfo.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='commit_id', full_name='cosmos.base.store.v1beta1.StoreInfo.commit_id', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=192,
  serialized_end=279,
)


_COMMITID = _descriptor.Descriptor(
  name='CommitID',
  full_name='cosmos.base.store.v1beta1.CommitID',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='cosmos.base.store.v1beta1.CommitID.version', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hash', full_name='cosmos.base.store.v1beta1.CommitID.hash', index=1,
      number=2, type=12, cpp_type=9, label=1,
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
  serialized_options=b'\230\240\037\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=281,
  serialized_end=328,
)

_COMMITINFO.fields_by_name['store_infos'].message_type = _STOREINFO
_STOREINFO.fields_by_name['commit_id'].message_type = _COMMITID
DESCRIPTOR.message_types_by_name['CommitInfo'] = _COMMITINFO
DESCRIPTOR.message_types_by_name['StoreInfo'] = _STOREINFO
DESCRIPTOR.message_types_by_name['CommitID'] = _COMMITID
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CommitInfo = _reflection.GeneratedProtocolMessageType('CommitInfo', (_message.Message,), {
  'DESCRIPTOR' : _COMMITINFO,
  '__module__' : 'cosmos.base.store.v1beta1.commit_info_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.base.store.v1beta1.CommitInfo)
  })
_sym_db.RegisterMessage(CommitInfo)

StoreInfo = _reflection.GeneratedProtocolMessageType('StoreInfo', (_message.Message,), {
  'DESCRIPTOR' : _STOREINFO,
  '__module__' : 'cosmos.base.store.v1beta1.commit_info_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.base.store.v1beta1.StoreInfo)
  })
_sym_db.RegisterMessage(StoreInfo)

CommitID = _reflection.GeneratedProtocolMessageType('CommitID', (_message.Message,), {
  'DESCRIPTOR' : _COMMITID,
  '__module__' : 'cosmos.base.store.v1beta1.commit_info_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.base.store.v1beta1.CommitID)
  })
_sym_db.RegisterMessage(CommitID)


DESCRIPTOR._options = None
_COMMITINFO.fields_by_name['store_infos']._options = None
_STOREINFO.fields_by_name['commit_id']._options = None
_COMMITID._options = None
# @@protoc_insertion_point(module_scope)
