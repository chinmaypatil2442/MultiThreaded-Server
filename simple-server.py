# =============================================================================
# Import modules
import socket 
import json
import os
import threading
# =============================================================================

# =============================================================================
# Constants
TCP_IP = '127.0.0.1' 
TCP_PORT = 2004 
BUFFER_SIZE = 1024
resp_success_str = 'HTTP/1.0 200 OK\r\nContent-Type: application/json\r\n\r\n'
resp_error_str = 'HTTP/1.0 404 NOT FOUND\r\nContent-Type: application/json\r\n\r\n'
thread_counter = 1
thread_list = []
# =============================================================================

# =============================================================================
# Classes
class ClientThread(threading.Thread): 
 
    def __init__(self,connection,ip,port,thread_id): 
        threading.Thread.__init__(self) 
        self.connection = connection
        self.ip = ip 
        self.port = port 
        self.thread_id = thread_id
 
    def run(self): 
        try:
            print(f'Thread-{self.thread_id}: Connected and Waiting for Client.')
            request = self.connection.recv(BUFFER_SIZE)
            request_str = request.decode()
            if request_str.split(' ')[0]=='GET':
                client = request_str.rsplit('?', 1)[1].rpartition("&")[0].split('=')[1]
                file = request_str.rsplit('?', 1)[1].rpartition("&")[2].split('=')[1]
                print(f'Thread-{self.thread_id}: Received request from {client}.')
                if os.path.exists(os.path.join(os.getcwd(),file)):
                    f = open(os.path.join(os.getcwd(),file), "rb")
                    file_data = f.read()
                    f.close()
                    response_obj = response(file,file_data.decode())
                    response_str = str(response_string(resp_success_str))
                    response_str += json.dumps(vars(response_obj))
                    self.connection.sendall(response_str.encode())
                    self.connection.close()
                    print(f'Thread-{self.thread_id}: Response sent to {client}. Connection Terminated.')
                else:
                    response_obj = response(file_name=file,error_message='404 File not found.',is_error=True)
                    response_str = str(response_string(resp_error_str))
                    response_str += json.dumps(vars(response_obj))
                    self.connection.sendall(response_str.encode())
                    self.connection.close()
                    print(f'Thread-{self.thread_id}: Response sent to {client}. Connection Terminated.')
        except:
            print('Thread-{self.thread_id}: Connection Terminated Abruptly.')
            self.connection.close()

class response:
     def __init__(self, file_name='', file_data='', error_message='', is_error=False):
        self.file_name = file_name
        self.file_data = file_data
        self.error_message = error_message
        self.is_error = is_error

class response_string:
    def __init__(self, string):
        self.string = string
    def __str__(self):
        return self.string 
# =============================================================================

# =============================================================================
# Main code
Server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
Server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
Server.bind((TCP_IP, TCP_PORT)) 
print(f"Socket Info: IP-{TCP_IP} PORT-{TCP_PORT}\n Waiting for connections...")
   
while True: 
    try:
        Server.listen(4)
        (conn, (ip,port)) = Server.accept()
        conn.settimeout(60)
  
        new_thread = ClientThread(conn,ip,port,thread_counter)
        thread_counter += 1 
        new_thread.start()
        thread_list.append(new_thread) 
    except:
        print('Shutting down server.')
        break

Server.close()

for t in thread_list: 
    t.join() 

# =============================================================================
