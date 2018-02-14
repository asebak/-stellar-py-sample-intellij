import requests
from stellar_base.keypair import Keypair

kp = Keypair.random()

publickey = kp.address().decode()
print 'public key is :' + publickey
seed = kp.seed().decode()
print 'seed is :' + seed

r = requests.get('https://horizon-testnet.stellar.org/friendbot?addr=' + publickey)