import socket
import pickle
import json
import sys

sys.setrecursionlimit(1000000)

print("Enter Client Division")
c1 = int(input())
c2 = int(input())
c3 = int(input())
client_id = int(input("Enter Client ID 1, 2 or 3: "))



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 9999))

with open('input.txt', 'r') as f:
        all = f.readlines()

print("Read Lines")

if (client_id==1):
    prompts = all[:c1]
elif (client_id==2):
    prompts = all[c1:c1+c2]
else:
    prompts = all[c1+c2:]

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



   
