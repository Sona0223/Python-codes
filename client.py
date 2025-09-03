# import socket
# import threading

# nickname = input("Choose your nickname: ")

# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client.connect(('127.0.0.1', 55555))

# # Listen for messages
# def receive():
#     while True:
#         try:
#             message = client.recv(1024).decode('utf-8')
#             if message == 'NICKNAME':
#                 client.send(nickname.encode('utf-8'))
#             else:
#                 print(message)
#         except:
#             print("An error occurred!")
#             client.close()
#             break

# # Send messages
# def write():
#     while True:
#         message = f'{nickname}: {input("")}'
#         client.send(message.encode('utf-8'))

# # Start threads
# receive_thread = threading.Thread(target=receive)
# receive_thread.start()

# write_thread = threading.Thread(target=write)
# write_thread.start()
# client.py
import asyncio
import websockets

async def chat():
    uri = "ws://192.168.89.216:8742"
    async with websockets.connect(uri) as websocket:
        while True:
            msg = input("You: ")
            await websocket.send(msg) 
            response = await websocket.recv()
            print(f"Other: {response}") 

asyncio.run(chat()) 