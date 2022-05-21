##   first, import the socket library to be used in communication   ##
import socket

## After importing, you need to create a socket object  ##

reciever = socket.socket()

print("Reciever socket is created successfully and ready to recieve messages")


# Choose the port to start communicating on ( the ip in this case will be your local host)
port = 3000

# Bind the port to the reciever socket 
reciever.bind(('',port))

print("choosing port %s to accept connections" %(port))


# start listening to one client
reciever.listen(1)

print("Listening on the specified port")

# generate you public and private keys to be used for communication
n = 15
e = 13
d = 11



cipher = ''
mes =''

# wait for the sender to request connections
sender, address = reciever.accept()

print('Got connection from', address)

#start be sending the public key to the sender so he can text you
sender.send(str(e).encode())

sender.send(str(n).encode())


while mes != '0':
    
    # waiting for messages
    cipher = sender.recv(1024).decode()

    mes = cipher

    print('Recieved message: ', mes)

print('Closing Connection.......')
reciever.close()

