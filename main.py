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


# work function

def task(_: int, file: FileHandler):
    """
    :param _: Is not used in this function but is necessary for multiprocessing
    :param file: Filehandler
    """
    # acquire the lock
    for i in range(50):
        pause = random.randint(0, 250)
        Logging.log("Waiting {} ms".format(pause), file)
        time.sleep(pause/1000.0)


def start_multiple_processes(number: int):
    file = FileHandler("log.txt")
    # create a number of processes with different sleep times
    processes = [Process(target=task, args=(i, file)) for i in range(number)]
    # start the processes
    for process in processes:
        process.start()
    # wait for all processes to finish
    for process in processes:
        process.join()


def start_with_multiple_threads(number: int):
    file = FileHandler("log.txt")
    with concurrent.futures.ThreadPoolExecutor(max_workers=number) as executor:
        futures = [executor.submit(task, i, file) for i in range(number)]
        concurrent.futures.wait(futures)

if __name__ == '__main__':
    start_time = datetime.datetime.now()
    start_multiple_processes(2)
    stop_time = datetime.datetime.now()

    print("Took {} seconds".format((stop_time - start_time).seconds))

    start_with_multiple_threads(2)
