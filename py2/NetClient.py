# -*- coding: utf-8 -*-
from SDBServer import start
import socket

help_message = '''
Usage: NetClient.py [OPTIONS]
-p  -port [PORT]    set listening port
-j  -json           enable json mode
-h  -help           shows this message and exits.
'''
running = True
server = None
def start_socket(port=9090):
    db_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print ('Socket created')
    db_socket.bind(('', port))
    print('Socket bind complete')
    db_socket.listen(1)
    print('Socket waiting on port ' + str(port))
    return db_socket
    
def wait_client(socket):
    while running:
        conn, addr = socket.accept()
        print('Connected by', addr)
        try:
            data = conn.recv(1024)
            while data:
                text = data.decode().split('\n')[0]
                result = parse(text) + '\n'
                conn.sendall(result.encode())
                data = conn.recv(1024)
        except ConnectionResetError:
            pass
        conn.close()
    socket.close()
    server.save()

def stop_server():
    running = False
    
def error(message):
    if(server.json_mode):
        return '{"error": ' + '"' + message + '"}'
    else:
        return '[error] ' + message
    
def parse(text):
    if(text == ''):
        return error('Empty Query')    
    args = text.split()
    if(len(args) == 3):
        if(args[0] != 'add'):
            return error('Invalid Usage')
        return server.add_value(args[1], args[2])
    elif(len(args) == 2):
        if(args[0] == 'get' and args[1] == 'all'):
            return server.get_all()
        elif(args[0] == 'del'):
            return server.del_value(args[1])
        elif(args[0] == 'get'):
            return server.get_value(args[1])
        else:
            return error('Invalid Usage')
    elif(len(args) == 1):
        if(args[0] == 'save'):
            return server.save()
        elif(args[0] == 'load'):
            return server.load()
        elif(args[0] == 'exit'):
            stop_server()
            return '{null : null}'
        elif(args[0] == 'json'):
            return server.json()
        else:
            return error('Invalid Keyword')
    else:
        return error('Invalid Arguments')

def main(args):
    possible_args = ['-h', '--help', '-j', '--json', '-p', '--port']
    #print(args)
    global server
    if(len(args) == 1):
        
        server = start(False)
        s = start_socket()
        wait_client(s)
    else:
        args.pop(0)
        ind = 0
        for x in args:
            if('-j' in args or '--json' in args):
                json = True
            if('-h' in args or '--help' in args):
                print(help_message)
                return
            if('-p' in args or '--port' in args):
                try:
                    port = int(args[i+1])
                    break
                except(IndexError, ValueError):
                    print('Invalid option [' + x + ']\nTry \'--help\' or \'-h\' for more information.')
                    return
            ind += 1
        server = start(json)
        s = start_socket(port)
        wait_client(s)
if __name__ == '__main__':
    import sys
    main(sys.argv)
