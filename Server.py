import zmq

from FileHandler import FileHandler
from Logging import Logging
from Message import *
from Utility import serialize, deserialize


class Server:

    def __init__(self):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REP)
        self.socket.bind("tcp://*:6666")
        self.clientCount = 0
        self.file = FileHandler("log.txt")
        self.running = True

    def run(self):
        while self.running:
            message: Message = deserialize(self.socket.recv())
            Logging.log("{}".format(message.msg), self.file)

            if isinstance(message, TerminationMessage):
                self.running = False

            response = Message()
            if message.msg == "get_last_entry":
                response.msg = self.get_last_entry()
            else:
                response.msg = f"Client number {self.clientCount}."

            self.socket.send(serialize(response))

            self.clientCount += 1


    def get_last_entry(self):
        return self.file.read_last_line()
