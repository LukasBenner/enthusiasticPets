import pickle
from Message import Message


def serialize(msg: Message) -> bytes:
    return pickle.dumps(msg)


def deserialize(msg: bytes) -> Message:
    return pickle.loads(msg)
