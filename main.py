# This is a sample Python script.
import datetime
import random
import string
import time
import threading
import concurrent.futures
from multiprocessing import Process
from FileHandler import FileHandler
from Logging import Logging
from Server import Server
from Client import Client

def start_server():
    server = Server()
    server.run()

def start_client():
    client = Client()
    client.run()
    client.terminate()

if __name__ == '__main__':
    server_proc = Process(target=start_server)
    client_proc = Process(target=start_client)

    server_proc.start()
    time.sleep(1)
    client_proc.start()

    server_proc.join()
    client_proc.join()
