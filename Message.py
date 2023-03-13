class Message:
    def __init__(self, msg=""):
        self.msg = msg


class TerminationMessage(Message):
    def __init__(self, msg=""):
        super().__init__(msg)