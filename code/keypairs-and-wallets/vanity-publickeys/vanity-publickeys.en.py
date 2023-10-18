from solders.keypair import Keypair

keypair = Keypair()
while(str(keypair.pubkey())[:5]!="elv1s") :
    keypair = Keypair()

print(f"Created Keypair with Public Key: {keypair.pubkey()}")