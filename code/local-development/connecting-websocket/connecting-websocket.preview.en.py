async with connect("wss://api.devnet.solana.com") as websocket:
    # Create a Test Wallet
    wallet = Keypair()
    # Subscribe to the Test wallet to listen for events
    await websocket.account_subscribe(wallet.pubkey())
    # Capture response from account subscription 
    first_resp = await websocket.recv()
    print(
        f"Subscription successful with id {first_resp.result}, listening for events \n"
    )
    updated_account_info = await websocket.recv()
    print(updated_account_info)    