import zmq
from constPS import *

context = zmq.Context()
s = context.socket(zmq.PUB)  # create a publisher socket
p = "tcp://" + HOST + ":" + PORT  # how and where to communicate
s.bind(p)  # bind socket to the address

while True:
    topic = input("Enter the topic: ")  
    message = input("Enter the message: ") 
    s.send_multipart([str.encode(topic), str.encode(message)])  #Publicação da mensagem
