import unittest
from cosm.wasm.rest_client import WasmRestClient
from cosm.tests.helpers import MockQueryRestClient

from cosmwasm.wasm.v1beta1.query_pb2 import (
    QuerySmartContractStateRequest,
    QuerySmartContractStateResponse,
    QueryAllContractStateRequest,
    QueryAllContractStateResponse,
    QueryCodeRequest,
    QueryCodeResponse,
    QueryCodesRequest,
    QueryCodesResponse,
    QueryContractHistoryRequest,
    QueryContractHistoryResponse,
    QueryContractInfoRequest,
    QueryContractInfoResponse,
    QueryContractsByCodeRequest,
    QueryContractsByCodeResponse,
    QueryRawContractStateRequest,
    QueryRawContractStateResponse,
)
from google.protobuf.json_format import ParseDict

import json
import base64


class WasmTests(unittest.TestCase):
    def test_query_codes(self):
        content = {
            "code_infos": [
                {"code_id": 3, "creator": "fetchaddress", "data_hash": "hash"},
            ],
            "pagination": {"total": 1},
        }
        expected_response = ParseDict(content, QueryCodesResponse())

        mock_client = MockQueryRestClient(json.dumps(content))
        wasm = WasmRestClient(mock_client)

        assert wasm.Codes(QueryCodesRequest()) == expected_response
        assert mock_client.last_request == "/wasm/v1beta1/code?"

    def test_query_code(self):
        content = {
            "code_info": {"code_id": 3, "creator": "fetchaddress", "data_hash": "hash"},
            "data": "bytecode",
        }
        expected_response = ParseDict(content, QueryCodeResponse())

        mock_client = MockQueryRestClient(json.dumps(content))
        wasm = WasmRestClient(mock_client)

        assert wasm.Code(QueryCodeRequest(code_id=1)) == expected_response
        assert mock_client.last_request == "/wasm/v1beta1/code/1?"

    def test_query_smart_contract_state(self):
        raw_content = b'{\n  "data": {"balance":"1"}\n}'
        expected_response = QuerySmartContractStateResponse(data=b'{"balance": "1"}')

        mock_client = MockQueryRestClient(raw_content)
        wasm = WasmRestClient(mock_client)

        assert (
            wasm.SmartContractState(
                QuerySmartContractStateRequest(
                    address="fetchcontractaddress", query_data=b"{}"
                )
            )
            == expected_response
        )
        assert (
            mock_client.last_request
            == "/wasm/v1beta1/contract/fetchcontractaddress/smart/e30=?"
        )

    def test_query_raw_contract_state(self):
        raw_content = b'{\n  "data": {"balance":"1"}\n}'
        expected_response = QueryRawContractStateResponse(data=b'{"balance": "1"}')

        mock_client = MockQueryRestClient(raw_content)
        wasm = WasmRestClient(mock_client)

        assert (
            wasm.RawContractState(
                QueryRawContractStateRequest(
                    address="fetchcontractaddress", query_data=b"{}"
                )
            )
            == expected_response
        )
        assert (
            mock_client.last_request
            == "/wasm/v1beta1/contract/fetchcontractaddress/raw/e30=?"
        )

    def test_query_all_contract_state(self):
        content = {
            "models": [
                {
                    "key": "00047572697300000000000000000000000000000000000000000000000000000000000004D2",
                    "value": "c29tZV9wYXRo",
                },
            ],
            "pagination": {"next_key": None, "total": "3"},
        }

        expected_response = ParseDict(content, QueryAllContractStateResponse())

        mock_client = MockQueryRestClient(json.dumps(content))
        wasm = WasmRestClient(mock_client)

        assert (
            wasm.AllContractState(
                QueryAllContractStateRequest(address="fetchcontractaddress")
            )
            == expected_response
        )
        assert (
            mock_client.last_request
            == "/wasm/v1beta1/contract/fetchcontractaddress/state?"
        )
