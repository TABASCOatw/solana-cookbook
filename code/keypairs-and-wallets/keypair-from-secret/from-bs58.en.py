from solders.keypair import Keypair

b58_string = "5MaiiCavjCmn9Hs1o3eznqDEhRwxo7pXiAYez7keQUviUkauRiTMD8DrESdrNjN8zd9mTmVhRvBJeg5vhyvgrAhG"
keypair = Keypair.from_string(b58_string)
print(f"Created Keypair with Public Key: {keypair.pubkey()}")