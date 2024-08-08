from socket import *

serverName = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)

print('This program counts the letter \'b\'')
message = input('input: ')
clientSocket.sendto(message.encode(), (serverName, serverPort))

modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

print('The number of times the letter "b" appears in the sent text is:', int(modifiedMessage.decode()))
clientSocket.close()
