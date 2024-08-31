Implemented using sockets and json module

The server listens for a connection. The Client looks for a connection on port 9999.

The Client asks for a division of the prompts in input.txt between 3 clients and asks for the client_id of the client being emulated. The Client then sends this information to the server.
The server uses this information to call fetch_response which is the api call to groq and receives the required json to be outputted.

Server sends this json to Client which then creates the output.json file.

Serialization and unserializatin were done using json module.
