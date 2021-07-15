from cosm.crypto.interface import Signer
from cosmos.tx.v1beta1.tx_pb2 import Tx, TxRaw, TxBody, SignDoc, SignerInfo, AuthInfo, ModeInfo, Fee


def sign_transaction(
        tx: Tx,
        signer: Signer,
        chain_id=None,
        account_number=None,
        deterministic=None
        ):
    sd = SignDoc()
    sd.body_bytes = tx.body.SerializeToString()
    sd.auth_info_bytes = tx.auth_info.SerializeToString()
    sd.chain_id = chain_id
    sd.account_number = account_number

    data_for_signing = sd.SerializeToString()

    # Generating deterministic signature:
    deterministic_signature = signer.sign(data_for_signing, deterministic=deterministic)
    tx.signatures.extend([deterministic_signature])
