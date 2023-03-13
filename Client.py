import zmq

from Message import *
from Utility import serialize, deserialize


class Client:
    def __init__(self):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REQ)
        self.socket.connect("tcp://localhost:6666")

    def run(self):
        request = Message("get_last_entry")
        self.socket.send(serialize(request))

        response = self.socket.recv()
        print(deserialize(response).msg)

    def terminate(self):
        request = TerminationMessage("terminate")
        self.socket.send(serialize(request))

        self.socket.disconnect("tcp://localhost:6666")
