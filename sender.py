##   first, import the socket library to be used in communication   ##
import socket
from rsa import *

## After importing, you need to create a socket object  ##

sender = socket.socket()

print("Sender socket is created successfully and ready to send messages")


# Choose the port to start communicating on ( the ip in this case will be your local host)
port = 12345

# Connect to the port where the reciever is listening 
sender.connect(('127.0.0.1', port))

print("choosing port %s to start connections" %(port))



# get the public key to encrypt messages
e = int(sender.recv(1024).decode());
n = int(sender.recv(1024).decode());

pu = e,n

print("Recieved public key is e=" + str(e) + " n=" + str(n))

mes =''


while mes != 'exit()':
    
    # waiting for messages to be typed
    mes = input('Write your message: ')

    # 1- To be general with different key sizes, we encrypt the message character by character\
    length = len(mes)    
    # 2- Encrypt using the public key
    num = Encrypt(length,pu)
    # 3- first send the length to the reciever (also encrypted)
    sender.send(str(num).encode())
    print(length)
    for i in range(0,length):
        print(i)  
        num = ConvertToInt(mes[i])
        cipher = Encrypt(num,pu)
        sender.send(str(cipher).encode())

print('Closing Connection.......')
sender.close()

