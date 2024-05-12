from web3 import Web3, middleware
from web3.exceptions import ContractLogicError
from web3.gas_strategies.time_based import *
from web3.middleware import geth_poa_middleware
import json
import os

w3 = Web3(provider=Web3.HTTPProvider("https://eth-sepolia.g.alchemy.com/v2/BWya-x-AKAA-bDx-d3xWC-exYQ8h7KJf"))

from_addr = os.getenv('from_addr')
contract_addr = '0x18c005e964227f873a03ef89f14a7b5678dce697'
contract_addr = Web3.to_checksum_address(contract_addr)
ABI = json.load(open('../abi.json'))
PRIVATE_KEY = os.getenv('METAMASK_PRIVATE_KEY')

contract = w3.eth.contract(contract_addr, abi=ABI)

w3.middleware_onion.inject(geth_poa_middleware, layer=0)
w3.middleware_onion.add(middleware.latest_block_based_cache_middleware)
w3.middleware_onion.add(middleware.simple_cache_middleware)

strategy = construct_time_based_gas_price_strategy(10)

w3.eth.set_gas_price_strategy((strategy))

def handle_transaction(fn_name, args):
    addr = Web3.to_checksum_address(from_addr)

    def calculate_nonce():
        return Web3.to_hex(w3.eth.get_transaction_count(addr))

    data = contract.encodeABI(fn_name, args=args)

    while True:
        try:
            gas = getattr(contract.functions, fn_name)(*args).estimate_gas({'from': addr})
            break
        except ContractLogicError as e:
            print(f"A contract error occurred while calculating gas: {e}")
            print("S=skip, R=retry, Q=quit")
            answer = input("> ")
            if "q" in answer.lower():
                quit()
            elif "s" in answer.lower():
                return
        except Exception as e:
            print(f"A misc. error occurred while calculating gas: {e}")
            print("Resolve bug. Quitting now.")
            quit()

    gasprice = w3.eth.generate_gas_price()

    txn_fee = gas * gasprice

    tr = {'to': contract.address,
          'from': from_addr,
          'value': Web3.to_hex(0),
          'gasPrice': Web3.to_hex(gasprice),
          'nonce': calculate_nonce(),
          'data': data,
          'gas': gas,
          }

    while True:
        try:
            signed = w3.eth.account.sign_transaction(tr, PRIVATE_KEY)
            tx = w3.eth.send_raw_transaction(signed.rawTransaction)
            tx_receipt = w3.eth.wait_for_transaction_receipt(tx)
            print("TXN RECEIPT: ", tx_receipt)
            break
        except Exception as e:
            print(f"{fn_name} Error: ", e)
            print("\nC=continue, R=retry, Q=quit")
            answer = input("> ")
            if "q" in answer.lower():
                quit()
            elif answer.lower() == 'c':
                break
            else:
                tr['nonce'] = calculate_nonce()
