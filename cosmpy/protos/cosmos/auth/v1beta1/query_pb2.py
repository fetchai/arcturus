# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/auth/v1beta1/query.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from cosmos.auth.v1beta1 import auth_pb2 as cosmos_dot_auth_dot_v1beta1_dot_auth__pb2
from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1f\x63osmos/auth/v1beta1/query.proto\x12\x13\x63osmos.auth.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x19google/protobuf/any.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1e\x63osmos/auth/v1beta1/auth.proto\x1a\x19\x63osmos_proto/cosmos.proto\"0\n\x13QueryAccountRequest\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"K\n\x14QueryAccountResponse\x12\x33\n\x07\x61\x63\x63ount\x18\x01 \x01(\x0b\x32\x14.google.protobuf.AnyB\x0c\xca\xb4-\x08\x41\x63\x63ountI\"\x14\n\x12QueryParamsRequest\"H\n\x13QueryParamsResponse\x12\x31\n\x06params\x18\x01 \x01(\x0b\x32\x1b.cosmos.auth.v1beta1.ParamsB\x04\xc8\xde\x1f\x00\x32\x9c\x02\n\x05Query\x12\x8f\x01\n\x07\x41\x63\x63ount\x12(.cosmos.auth.v1beta1.QueryAccountRequest\x1a).cosmos.auth.v1beta1.QueryAccountResponse\"/\x82\xd3\xe4\x93\x02)\x12\'/cosmos/auth/v1beta1/accounts/{address}\x12\x80\x01\n\x06Params\x12\'.cosmos.auth.v1beta1.QueryParamsRequest\x1a(.cosmos.auth.v1beta1.QueryParamsResponse\"#\x82\xd3\xe4\x93\x02\x1d\x12\x1b/cosmos/auth/v1beta1/paramsB+Z)github.com/cosmos/cosmos-sdk/x/auth/typesb\x06proto3')



_QUERYACCOUNTREQUEST = DESCRIPTOR.message_types_by_name['QueryAccountRequest']
_QUERYACCOUNTRESPONSE = DESCRIPTOR.message_types_by_name['QueryAccountResponse']
_QUERYPARAMSREQUEST = DESCRIPTOR.message_types_by_name['QueryParamsRequest']
_QUERYPARAMSRESPONSE = DESCRIPTOR.message_types_by_name['QueryParamsResponse']
QueryAccountRequest = _reflection.GeneratedProtocolMessageType('QueryAccountRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYACCOUNTREQUEST,
  '__module__' : 'cosmos.auth.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.auth.v1beta1.QueryAccountRequest)
  })
_sym_db.RegisterMessage(QueryAccountRequest)

QueryAccountResponse = _reflection.GeneratedProtocolMessageType('QueryAccountResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYACCOUNTRESPONSE,
  '__module__' : 'cosmos.auth.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.auth.v1beta1.QueryAccountResponse)
  })
_sym_db.RegisterMessage(QueryAccountResponse)

QueryParamsRequest = _reflection.GeneratedProtocolMessageType('QueryParamsRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYPARAMSREQUEST,
  '__module__' : 'cosmos.auth.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.auth.v1beta1.QueryParamsRequest)
  })
_sym_db.RegisterMessage(QueryParamsRequest)

QueryParamsResponse = _reflection.GeneratedProtocolMessageType('QueryParamsResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYPARAMSRESPONSE,
  '__module__' : 'cosmos.auth.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.auth.v1beta1.QueryParamsResponse)
  })
_sym_db.RegisterMessage(QueryParamsResponse)

_QUERY = DESCRIPTOR.services_by_name['Query']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z)github.com/cosmos/cosmos-sdk/x/auth/types'
  _QUERYACCOUNTREQUEST._options = None
  _QUERYACCOUNTREQUEST._serialized_options = b'\350\240\037\000\210\240\037\000'
  _QUERYACCOUNTRESPONSE.fields_by_name['account']._options = None
  _QUERYACCOUNTRESPONSE.fields_by_name['account']._serialized_options = b'\312\264-\010AccountI'
  _QUERYPARAMSRESPONSE.fields_by_name['params']._options = None
  _QUERYPARAMSRESPONSE.fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _QUERY.methods_by_name['Account']._options = None
  _QUERY.methods_by_name['Account']._serialized_options = b'\202\323\344\223\002)\022\'/cosmos/auth/v1beta1/accounts/{address}'
  _QUERY.methods_by_name['Params']._options = None
  _QUERY.methods_by_name['Params']._serialized_options = b'\202\323\344\223\002\035\022\033/cosmos/auth/v1beta1/params'
  _QUERYACCOUNTREQUEST._serialized_start=194
  _QUERYACCOUNTREQUEST._serialized_end=242
  _QUERYACCOUNTRESPONSE._serialized_start=244
  _QUERYACCOUNTRESPONSE._serialized_end=319
  _QUERYPARAMSREQUEST._serialized_start=321
  _QUERYPARAMSREQUEST._serialized_end=341
  _QUERYPARAMSRESPONSE._serialized_start=343
  _QUERYPARAMSRESPONSE._serialized_end=415
  _QUERY._serialized_start=418
  _QUERY._serialized_end=702
# @@protoc_insertion_point(module_scope)
