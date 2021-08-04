# MultiThreaded-Server

Program Implementation Details:
Program has been written in language: Python 3.7
Imported modules list:
socket
json
os
threading


Steps:
Server file named, “simple-server.py”, needs to be executed first, with the command “python simple-server.py”. Server will bind to the socket with IP-127.0.0.1 and PORT-2004 and wait for connections.
The clients, files named “ClientA.py”, “ClientB.py”, “ClientC.py” and “ClientD.py”, can be run similarly using “python “ and the filename. 
The client will first connect to the HOST using the same socket upon which the server creates a new thread and prints “Thread-<id>: Connected and Waiting for Client.”  and the client will print “Connected to HOST: 127.0.0.1 and PORT: 2004”.
Now, as the list of files is hardcoded on the client side, it will print 
“1 - File1.txt
2 - File2.txt
3 - File_that_doesnt_exist.txt
Enter code: ”.
Here the user will input the respective code “1 or 2 or 3” and the sent request will be printed as “Sent request: ” followed by the request. Upon receiving the request the server will print “Thread-<id>: Received request from Client<name>.”.

The server will process the request, send the response accordingly and terminate the connection and the thread, then print “Thread-<id>: Response sent to Client<name>. Connection Terminated.”.
After receiving the response from the server, the client leaves the socket and prints “Response: ” followed by the received response.
The server will create a new thread and connection for each new client.
