#
#   Request-reply client in Python
#   Connects REQ socket to tcp://localhost:5557
#   Sends json request to zcoind
#
import zmq
import json

MAINNET = "15557"
TESTNET = "15558"

#  Prepare our context and sockets
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:" + MAINNET)

message_input_pr = b"{ \
                    \"type\": \"create-payment-request\", \
                    \"data\": { \
                        \"amount\": \"4000\", \
                        \"label\": \"Joern's Payment Request\",\
                        \"msg\": \"this is a payment request for Joern.\" \
                     } \
                  }";

message_input_list = b"{ \
                    \"type\": \"getblock\", \
                    \"data\": { \
                        \"56b0558e170b2184ee0dbd053f517507dbaf4ad9289ba027dca62b6c03fc8645\" \
                     } \
                  }";

message_input_object = b"{ \
                    \"type\": \"getaddressbalance\", \
                    \"data\": { \
                        \"addresses\": [\"aQ18FBVFtnueucZKeVg4srhmzbpAeb1KoN\"] \
                     } \
                  }";
                  
socket.send(message_input_pr)
message = socket.recv()
print("Received reply [%s]" % (message))