##   first, import the socket library to be used in communication   ##
import socket

## After importing, you need to create a socket object  ##

sender = socket.socket()

print("Sender socket is created successfully and ready to send messages")


# Choose the port to start communicating on ( the ip in this case will be your local host)
port = 3000

# Connect to the port where the reciever is listening 
sender.connect(('127.0.0.1', port))

print("choosing port %s to start connections" %(port))



# get the public key to encrypt messages
e = int(sender.recv(1024).decode());
n = int(sender.recv(1024).decode());



cipher = ''
mes =''


while mes != '0':
    
    # waiting for messages to be typed
    mes = input('Write your message: ')
    cipher = mes

    sender.send(cipher.encode())

print('Closing Connection.......')
sender.close()

