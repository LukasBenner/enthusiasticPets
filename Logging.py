import os
import string
import threading
from datetime import datetime

from FileHandler import FileHandler


class Logging:

    @staticmethod
    def log(message: string, file: FileHandler):
        # concat string
        message = Logging.__build_message(message)
        print(message, end="")
        file.append(message)

    @staticmethod
    def __build_message(message: string) -> string:
        return "[PID: {} | TID: {} | {}]    {} \n".format(os.getpid(),
                                                          threading.get_native_id(),
                                                          datetime.now(),
                                                          message)
