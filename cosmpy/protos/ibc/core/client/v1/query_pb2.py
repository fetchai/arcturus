# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ibc/core/client/v1/query.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from ibc.core.client.v1 import client_pb2 as ibc_dot_core_dot_client_dot_v1_dot_client__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1eibc/core/client/v1/query.proto\x12\x12ibc.core.client.v1\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x1fibc/core/client/v1/client.proto\x1a\x19google/protobuf/any.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x14gogoproto/gogo.proto\",\n\x17QueryClientStateRequest\x12\x11\n\tclient_id\x18\x01 \x01(\t\"\x8d\x01\n\x18QueryClientStateResponse\x12*\n\x0c\x63lient_state\x18\x01 \x01(\x0b\x32\x14.google.protobuf.Any\x12\r\n\x05proof\x18\x02 \x01(\x0c\x12\x36\n\x0cproof_height\x18\x03 \x01(\x0b\x32\x1a.ibc.core.client.v1.HeightB\x04\xc8\xde\x1f\x00\"V\n\x18QueryClientStatesRequest\x12:\n\npagination\x18\x01 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"\xba\x01\n\x19QueryClientStatesResponse\x12`\n\rclient_states\x18\x01 \x03(\x0b\x32).ibc.core.client.v1.IdentifiedClientStateB\x1e\xc8\xde\x1f\x00\xaa\xdf\x1f\x16IdentifiedClientStates\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"x\n\x1aQueryConsensusStateRequest\x12\x11\n\tclient_id\x18\x01 \x01(\t\x12\x17\n\x0frevision_number\x18\x02 \x01(\x04\x12\x17\n\x0frevision_height\x18\x03 \x01(\x04\x12\x15\n\rlatest_height\x18\x04 \x01(\x08\"\x93\x01\n\x1bQueryConsensusStateResponse\x12-\n\x0f\x63onsensus_state\x18\x01 \x01(\x0b\x32\x14.google.protobuf.Any\x12\r\n\x05proof\x18\x02 \x01(\x0c\x12\x36\n\x0cproof_height\x18\x03 \x01(\x0b\x32\x1a.ibc.core.client.v1.HeightB\x04\xc8\xde\x1f\x00\"l\n\x1bQueryConsensusStatesRequest\x12\x11\n\tclient_id\x18\x01 \x01(\t\x12:\n\npagination\x18\x02 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"\xa9\x01\n\x1cQueryConsensusStatesResponse\x12L\n\x10\x63onsensus_states\x18\x01 \x03(\x0b\x32,.ibc.core.client.v1.ConsensusStateWithHeightB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"\x1a\n\x18QueryClientParamsRequest\"G\n\x19QueryClientParamsResponse\x12*\n\x06params\x18\x01 \x01(\x0b\x32\x1a.ibc.core.client.v1.Params2\xfb\x06\n\x05Query\x12\xa4\x01\n\x0b\x43lientState\x12+.ibc.core.client.v1.QueryClientStateRequest\x1a,.ibc.core.client.v1.QueryClientStateResponse\":\x82\xd3\xe4\x93\x02\x34\x12\x32/ibc/core/client/v1beta1/client_states/{client_id}\x12\x9b\x01\n\x0c\x43lientStates\x12,.ibc.core.client.v1.QueryClientStatesRequest\x1a-.ibc.core.client.v1.QueryClientStatesResponse\".\x82\xd3\xe4\x93\x02(\x12&/ibc/core/client/v1beta1/client_states\x12\xe4\x01\n\x0e\x43onsensusState\x12..ibc.core.client.v1.QueryConsensusStateRequest\x1a/.ibc.core.client.v1.QueryConsensusStateResponse\"q\x82\xd3\xe4\x93\x02k\x12i/ibc/core/client/v1beta1/consensus_states/{client_id}/revision/{revision_number}/height/{revision_height}\x12\xb3\x01\n\x0f\x43onsensusStates\x12/.ibc.core.client.v1.QueryConsensusStatesRequest\x1a\x30.ibc.core.client.v1.QueryConsensusStatesResponse\"=\x82\xd3\xe4\x93\x02\x37\x12\x35/ibc/core/client/v1beta1/consensus_states/{client_id}\x12\x8f\x01\n\x0c\x43lientParams\x12,.ibc.core.client.v1.QueryClientParamsRequest\x1a-.ibc.core.client.v1.QueryClientParamsResponse\"\"\x82\xd3\xe4\x93\x02\x1c\x12\x1a/ibc/client/v1beta1/paramsB9Z7github.com/cosmos/cosmos-sdk/x/ibc/core/02-client/typesb\x06proto3')



_QUERYCLIENTSTATEREQUEST = DESCRIPTOR.message_types_by_name['QueryClientStateRequest']
_QUERYCLIENTSTATERESPONSE = DESCRIPTOR.message_types_by_name['QueryClientStateResponse']
_QUERYCLIENTSTATESREQUEST = DESCRIPTOR.message_types_by_name['QueryClientStatesRequest']
_QUERYCLIENTSTATESRESPONSE = DESCRIPTOR.message_types_by_name['QueryClientStatesResponse']
_QUERYCONSENSUSSTATEREQUEST = DESCRIPTOR.message_types_by_name['QueryConsensusStateRequest']
_QUERYCONSENSUSSTATERESPONSE = DESCRIPTOR.message_types_by_name['QueryConsensusStateResponse']
_QUERYCONSENSUSSTATESREQUEST = DESCRIPTOR.message_types_by_name['QueryConsensusStatesRequest']
_QUERYCONSENSUSSTATESRESPONSE = DESCRIPTOR.message_types_by_name['QueryConsensusStatesResponse']
_QUERYCLIENTPARAMSREQUEST = DESCRIPTOR.message_types_by_name['QueryClientParamsRequest']
_QUERYCLIENTPARAMSRESPONSE = DESCRIPTOR.message_types_by_name['QueryClientParamsResponse']
QueryClientStateRequest = _reflection.GeneratedProtocolMessageType('QueryClientStateRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYCLIENTSTATEREQUEST,
  '__module__' : 'ibc.core.client.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.client.v1.QueryClientStateRequest)
  })
_sym_db.RegisterMessage(QueryClientStateRequest)

QueryClientStateResponse = _reflection.GeneratedProtocolMessageType('QueryClientStateResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYCLIENTSTATERESPONSE,
  '__module__' : 'ibc.core.client.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.client.v1.QueryClientStateResponse)
  })
_sym_db.RegisterMessage(QueryClientStateResponse)

QueryClientStatesRequest = _reflection.GeneratedProtocolMessageType('QueryClientStatesRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYCLIENTSTATESREQUEST,
  '__module__' : 'ibc.core.client.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.client.v1.QueryClientStatesRequest)
  })
_sym_db.RegisterMessage(QueryClientStatesRequest)

QueryClientStatesResponse = _reflection.GeneratedProtocolMessageType('QueryClientStatesResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYCLIENTSTATESRESPONSE,
  '__module__' : 'ibc.core.client.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.client.v1.QueryClientStatesResponse)
  })
_sym_db.RegisterMessage(QueryClientStatesResponse)

QueryConsensusStateRequest = _reflection.GeneratedProtocolMessageType('QueryConsensusStateRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYCONSENSUSSTATEREQUEST,
  '__module__' : 'ibc.core.client.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.client.v1.QueryConsensusStateRequest)
  })
_sym_db.RegisterMessage(QueryConsensusStateRequest)

QueryConsensusStateResponse = _reflection.GeneratedProtocolMessageType('QueryConsensusStateResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYCONSENSUSSTATERESPONSE,
  '__module__' : 'ibc.core.client.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.client.v1.QueryConsensusStateResponse)
  })
_sym_db.RegisterMessage(QueryConsensusStateResponse)

QueryConsensusStatesRequest = _reflection.GeneratedProtocolMessageType('QueryConsensusStatesRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYCONSENSUSSTATESREQUEST,
  '__module__' : 'ibc.core.client.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.client.v1.QueryConsensusStatesRequest)
  })
_sym_db.RegisterMessage(QueryConsensusStatesRequest)

QueryConsensusStatesResponse = _reflection.GeneratedProtocolMessageType('QueryConsensusStatesResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYCONSENSUSSTATESRESPONSE,
  '__module__' : 'ibc.core.client.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.client.v1.QueryConsensusStatesResponse)
  })
_sym_db.RegisterMessage(QueryConsensusStatesResponse)

QueryClientParamsRequest = _reflection.GeneratedProtocolMessageType('QueryClientParamsRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYCLIENTPARAMSREQUEST,
  '__module__' : 'ibc.core.client.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.client.v1.QueryClientParamsRequest)
  })
_sym_db.RegisterMessage(QueryClientParamsRequest)

QueryClientParamsResponse = _reflection.GeneratedProtocolMessageType('QueryClientParamsResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYCLIENTPARAMSRESPONSE,
  '__module__' : 'ibc.core.client.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.client.v1.QueryClientParamsResponse)
  })
_sym_db.RegisterMessage(QueryClientParamsResponse)

_QUERY = DESCRIPTOR.services_by_name['Query']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z7github.com/cosmos/cosmos-sdk/x/ibc/core/02-client/types'
  _QUERYCLIENTSTATERESPONSE.fields_by_name['proof_height']._options = None
  _QUERYCLIENTSTATERESPONSE.fields_by_name['proof_height']._serialized_options = b'\310\336\037\000'
  _QUERYCLIENTSTATESRESPONSE.fields_by_name['client_states']._options = None
  _QUERYCLIENTSTATESRESPONSE.fields_by_name['client_states']._serialized_options = b'\310\336\037\000\252\337\037\026IdentifiedClientStates'
  _QUERYCONSENSUSSTATERESPONSE.fields_by_name['proof_height']._options = None
  _QUERYCONSENSUSSTATERESPONSE.fields_by_name['proof_height']._serialized_options = b'\310\336\037\000'
  _QUERYCONSENSUSSTATESRESPONSE.fields_by_name['consensus_states']._options = None
  _QUERYCONSENSUSSTATESRESPONSE.fields_by_name['consensus_states']._serialized_options = b'\310\336\037\000'
  _QUERY.methods_by_name['ClientState']._options = None
  _QUERY.methods_by_name['ClientState']._serialized_options = b'\202\323\344\223\0024\0222/ibc/core/client/v1beta1/client_states/{client_id}'
  _QUERY.methods_by_name['ClientStates']._options = None
  _QUERY.methods_by_name['ClientStates']._serialized_options = b'\202\323\344\223\002(\022&/ibc/core/client/v1beta1/client_states'
  _QUERY.methods_by_name['ConsensusState']._options = None
  _QUERY.methods_by_name['ConsensusState']._serialized_options = b'\202\323\344\223\002k\022i/ibc/core/client/v1beta1/consensus_states/{client_id}/revision/{revision_number}/height/{revision_height}'
  _QUERY.methods_by_name['ConsensusStates']._options = None
  _QUERY.methods_by_name['ConsensusStates']._serialized_options = b'\202\323\344\223\0027\0225/ibc/core/client/v1beta1/consensus_states/{client_id}'
  _QUERY.methods_by_name['ClientParams']._options = None
  _QUERY.methods_by_name['ClientParams']._serialized_options = b'\202\323\344\223\002\034\022\032/ibc/client/v1beta1/params'
  _QUERYCLIENTSTATEREQUEST._serialized_start=210
  _QUERYCLIENTSTATEREQUEST._serialized_end=254
  _QUERYCLIENTSTATERESPONSE._serialized_start=257
  _QUERYCLIENTSTATERESPONSE._serialized_end=398
  _QUERYCLIENTSTATESREQUEST._serialized_start=400
  _QUERYCLIENTSTATESREQUEST._serialized_end=486
  _QUERYCLIENTSTATESRESPONSE._serialized_start=489
  _QUERYCLIENTSTATESRESPONSE._serialized_end=675
  _QUERYCONSENSUSSTATEREQUEST._serialized_start=677
  _QUERYCONSENSUSSTATEREQUEST._serialized_end=797
  _QUERYCONSENSUSSTATERESPONSE._serialized_start=800
  _QUERYCONSENSUSSTATERESPONSE._serialized_end=947
  _QUERYCONSENSUSSTATESREQUEST._serialized_start=949
  _QUERYCONSENSUSSTATESREQUEST._serialized_end=1057
  _QUERYCONSENSUSSTATESRESPONSE._serialized_start=1060
  _QUERYCONSENSUSSTATESRESPONSE._serialized_end=1229
  _QUERYCLIENTPARAMSREQUEST._serialized_start=1231
  _QUERYCLIENTPARAMSREQUEST._serialized_end=1257
  _QUERYCLIENTPARAMSRESPONSE._serialized_start=1259
  _QUERYCLIENTPARAMSRESPONSE._serialized_end=1330
  _QUERY._serialized_start=1333
  _QUERY._serialized_end=2224
# @@protoc_insertion_point(module_scope)
