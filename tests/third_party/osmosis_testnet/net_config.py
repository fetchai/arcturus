# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2018-2022 Fetch.AI Limited
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

"""Osmosis network config."""
from time import sleep

import requests

from cosmpy.aerial.client import LedgerClient
from cosmpy.aerial.config import NetworkConfig
from cosmpy.aerial.wallet import LocalWallet


# Network config
PREFIX = "osmo"
DENOM = "uosmo"
GAS_LIMIT = 120000

NET_CONFIG = NetworkConfig(
    chain_id="osmo-test-4",
    url="grpc+http://grpc-test.osmosis.zone:443/",
    fee_minimum_gas_price=1,
    fee_denomination=DENOM,
    staking_denomination=DENOM,
)

DEFAULT_TIMEOUT = 60.0
FUNDED_PK = "974c467d48351204b8481736079edfefa98eba16f4b80d74b279e103e8ee9246"


class FaucetMixIn:
    """Osmosis faucet config"""

    def ask_funds(self, wallet: LocalWallet, ledger: LedgerClient):
        """Request fund from faucet.

        :param wallet: Wallet Address
        :param ledger: LedgerClient
        :raises Exception: fail to topup
        """

        funded_wallet = LocalWallet.from_unsafe_seed(FUNDED_PK, prefix=PREFIX)
        ledger.send_tokens(wallet, 100, DENOM, funded_wallet).wait_to_complete()
