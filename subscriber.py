import zmq
from constPS import *

context = zmq.Context()
s = context.socket(zmq.SUB)  # create a subscriber socket
p = "tcp://" + HOST + ":" + PORT  # how and where to communicate
s.connect(p)  # connect to the server

while True:
    topic = input("Enter the topic to subscribe: ")  
    s.setsockopt_string(zmq.SUBSCRIBE, topic)  

    for _ in range(5): 
        [topic, message] = s.recv_multipart()  #Recebimento da mensagem
        print(f"Topic: {topic.decode()}, Message: {message.decode()}")
