from emotes.interfaces.reader import EmoteReader
from infrastructure.reader import LocalFileReader, RemoteFileReader, MemoryFileReader


def local_reader_provider() -> EmoteReader:
    return LocalFileReader()


def remote_reader_provider() -> EmoteReader:
    return RemoteFileReader()


def memory_reader_provider() -> EmoteReader:
    return MemoryFileReader()
