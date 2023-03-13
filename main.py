import time
from multiprocessing import Process

from Client import Client
from Server import Server


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
