import os
import socket
import pickle
import json
from fetch_response import fetch_response 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 9999))
s.listen(5)

clientsocket, addr = s.accept()
print(f"Connected to {addr}")

while True:

    data = clientsocket.recv(1024)
    deserialized_data = pickle.loads(data)
    print("Recieved Information from Client")
    prompts = deserialized_data[1]
    client_id = deserialized_data[0]
    reqd_json = fetch_response(client_id, prompts)
    # reqd_json = pickle.dumps(reqd_json)
    clientsocket.sendall(reqd_json.encode())
    print("Data sent from server")
    clientsocket.close()








