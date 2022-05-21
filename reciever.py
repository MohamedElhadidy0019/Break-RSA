##   first, import the socket library to be used in communication   ##
import socket

from rsa import *

## After importing, you need to create a socket object  ##

reciever = socket.socket()

print("Reciever socket is created successfully and ready to recieve messages")


# Choose the port to start communicating on ( the ip in this case will be your local host)
port = 12345

# Bind the port to the reciever socket 
reciever.bind(('',port))

print("choosing port %s to accept connections" %(port))


# start listening to one client
reciever.listen(1)

print("Listening on the specified port")

# generate you public and private keys to be used for communication
pu , pr = RSA(10)

e,n = pu
print("Public Key is e=" + str(e) + " n="+ str(n))

# wait for the sender to request connections
sender, address = reciever.accept()

print('Got connection from', address)

#start be sending the public key to the sender so he can text you
sender.send(str(e).encode())

sender.send(str(n).encode())


# As long as you didn't recieve '0' as the message, keep reading
mes =''
while mes != 'exit()':
    
    # waiting for message
    # 1- decode the recieved string 
    # 2- convert it to integer so it can be decrypted
    cipher = int(sender.recv(1024).decode())
    # 3- decrypt it using your private key
    length = Decrypt(cipher,pr)
    # 4- The first recieved character is the message length
    # 5- loop over it and start recieving characters one by one
    print(length)
    mes = ''
    for i in range(0, length):
        print(i)
        cipher = int(sender.recv(1024).decode())
        num = Decrypt(cipher,pr)
        mes += ConvertToStr(num)

    print('Recieved message: ', mes)

print('Closing Connection.......')
reciever.close()

