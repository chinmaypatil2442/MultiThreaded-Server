# =============================================================================
# Import modules
import socket
import json

# =============================================================================

# =============================================================================
# Constants
target_host = '127.0.0.1'
target_port = 2004
request_str = 'GET HTTP/1.0\r\n http://127.0.0.1'
client = 'ClientD'
LIST = "1 - File1.txt\n2 - File2.txt\n3 - File_that_doesnt_exist.txt\nEnter code: "
leave = False

# =============================================================================

# =============================================================================
# Main Code
try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((target_host, target_port))
        print(f'Connected to HOST: {target_host} and PORT: {target_port}')
        while True:
            user_input = input(LIST)
            if user_input == '1':
                file = 'File1.txt'
                request_str += f'?client={client}&file={file}'
                break
            elif user_input == '2':
                file = 'File2.txt'
                request_str += f'?client={client}&file={file}'
                break
            elif user_input == '3':
                file = 'File_that_doesnt_exist.txt'
                request_str += f'?client={client}&file={file}'
                break
            else:
                print('Invalid input. Try again.')
        if not leave:
            print(f'Sent request:\n {request_str}')
            s.send(request_str.encode())
            response = s.recv(1024)
            response_object = response.decode()
            print(f'Response:\n {response_object}')
          

except socket.error as e:
    print(e)  

# =============================================================================


