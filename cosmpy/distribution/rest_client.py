# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2018-2021 Fetch.AI Limited
#   Modifications copyright (C) 2022 Cros-Nest
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ------------------------------------------------------------------------------

"""Implementation of Distribution interface using REST."""

from google.protobuf.json_format import Parse

from cosmpy.common.rest_client import RestClient
from cosmpy.protos.cosmos.distribution.v1beta1.query_pb2 import (
    QueryCommunityPoolRequest, QueryCommunityPoolResponse,
    QueryDelegationTotalRewardsRequest, QueryDelegationTotalRewardsResponse, QueryDelegationRewardsRequest,
    QueryDelegationRewardsResponse, QueryDelegatorValidatorsRequest, QueryDelegatorValidatorsResponse,
    QueryDelegatorWithdrawAddressResponse, QueryDelegatorWithdrawAddressRequest, QueryParamsRequest,
    QueryValidatorCommissionResponse, QueryValidatorCommissionRequest, QueryParamsResponse,
    QueryValidatorOutstandingRewardsRequest, QueryValidatorSlashesRequest, QueryValidatorSlashesResponse,
    QueryValidatorOutstandingRewardsResponse)
from cosmpy.distribution.interface import Distribution


class DistributionRestClient(Distribution):
    """Distribution REST client."""

    API_URL = "/cosmos/distribution/v1beta1"

    def __init__(self, rest_api: RestClient) -> None:
        """
        Initialize.

        :param rest_api: RestClient api
        """
        self._rest_api = rest_api

    def CommunityPool(self, request: QueryCommunityPoolRequest) -> QueryCommunityPoolResponse:
        """CommunityPool queries the community pool coins."""
        json_response = self._rest_api.get(f"{self.API_URL}/community_pool")
        return Parse(json_response, QueryCommunityPoolResponse())

    def DelegationTotalRewards(self, request: QueryDelegationTotalRewardsRequest) -> QueryDelegationTotalRewardsResponse:
        """DelegationTotalRewards queries the total rewards accrued by a each validator."""
        json_response = self._rest_api.get(f"{self.API_URL}/delegators/{request.delegator_address}/rewards")
        return Parse(json_response, QueryDelegationTotalRewardsResponse())

    def DelegationRewards(self, request: QueryDelegationRewardsRequest) -> QueryDelegationRewardsResponse:
        """DelegationRewards queries the total rewards accrued by a delegation."""
        json_response = self._rest_api.get(f"{self.API_URL}/delegators/{request.delegator_address}/rewards/{request.validator_address}")
        return Parse(json_response, QueryDelegationRewardsResponse())

    def DelegatorValidators(self, request: QueryDelegatorValidatorsRequest) -> QueryDelegatorValidatorsResponse:
        """DelegatorValidators queries the validators of a delegator."""
        json_response = self._rest_api.get(f"{self.API_URL}/delegators/{request.delegator_address}/validators")
        return Parse(json_response, QueryDelegatorValidatorsResponse())

    def DelegatorWithdrawAddress(self, request: QueryDelegatorWithdrawAddressRequest) -> QueryDelegatorWithdrawAddressResponse:
        """DelegatorWithdrawAddress queries withdraw address of a delegator."""
        json_response = self._rest_api.get(f"{self.API_URL}/delegators/{request.delegator_address}/withdraw_address")
        return Parse(json_response, QueryDelegatorWithdrawAddressResponse())

    def Params(self, request: QueryParamsRequest) -> QueryParamsResponse:
        """Params queries params of the distribution module."""
        json_response = self._rest_api.get(f"{self.API_URL}/params")
        return Parse(json_response, QueryParamsResponse())

    def ValidatorCommission(self, request: QueryValidatorCommissionRequest) -> QueryValidatorCommissionResponse:
        """ValidatorCommission queries accumulated commission for a validator."""
        json_response = self._rest_api.get(f"{self.API_URL}/validators/{request.validator_address}/commission")
        return Parse(json_response, QueryValidatorCommissionResponse())

    def ValidatorOutstandingRewards(self, request: QueryValidatorOutstandingRewardsRequest) -> QueryValidatorOutstandingRewardsResponse:
        """ValidatorOutstandingRewards queries rewards of a validator address."""
        json_response = self._rest_api.get(f"{self.API_URL}/validators/{request.validator_address}/outstanding_rewards")
        return Parse(json_response, QueryValidatorOutstandingRewardsResponse())

    def ValidatorSlashes(self, request: QueryValidatorSlashesRequest) -> QueryValidatorSlashesResponse:
        """ValidatorSlashes queries slash events of a validator."""
        json_response = self._rest_api.get(f"{self.API_URL}/validators/{request.validator_address}/slashes",
                                           request,
                                           ['validatorAddress'])
        return Parse(json_response, QueryValidatorSlashesResponse())
