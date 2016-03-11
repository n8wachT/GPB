# -*- coding: utf-8 -*-
import socket
import json

class SDBApi:
    def __init__(self, host='localhost', port=9090):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host, port))
        print('SDBApi started.')
    def write(self, text):
        self.socket.sendall(text.encode())
        return self.read()
        
    def read(self):
        response = ''
        while(not response.endswith('\n')):
            data = self.socket.recv(1024)
            response = response + data.decode()
        return response.split('\n')[0]
        
    def add_value(self, name, value):
        return self.write('add ' + name + ' ' + value )
        
    def del_value(self, name):
        return self.write('del ' + name)
        
    def get_value(self, name):
        return self.write('get ' + name)
        
    def get_all(self):
        return self.write('get all')
        
    def save(self):
        return self.write('save')
        
    def load(self):
        return self.write('load')
        
    def toggle_json(self):
        return self.write('json')
        
    def exit(self):
        self.socket.close()
