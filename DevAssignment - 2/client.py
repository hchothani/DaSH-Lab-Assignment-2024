import socket
import pickle
import json
import sys

sys.setrecursionlimit(1000000)

c1, c2, c3 = input(" Enter Client Division")
client_id = input("Enter Client ID: 1")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 9999))

with open('input.txt', 'r') as f:
        all = f.readlines()

print("Read Lines")

prompts = all[:3]
data = [client_id, prompts]
serialized_data = pickle.dumps(data)
s.sendall(serialized_data)

print("Sent Data to Server")

data = ""
while True:
    chunk = s.recv(4096)
    if not chunk:
        break
    print("Adding Data")
    data+=chunk.decode()


data = json.loads(data)
print("Recieved Data from Server")
reqd_json = data
client_id = str(client_id)
outfile = f'output{client_id}.json' 
with open(outfile, 'w') as output_file:
    json.dump(reqd_json, output_file, indent=4)

print("Created Output File")



   