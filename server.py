import zmq
import os
from os.path import isfile


PORT = 5555
VOCAB_DIRECTORY = "vocabulary"
ENCODING = "utf-8"


def file_path_exists(file_path):
    if isfile(file_path):
        return True
    return False


def main():
    context = zmq.Context()
    server = context.socket(zmq.REP)
    server.bind("tcp://*:{port}".format(port=PORT))
    print("VocabularyService now available at tcp port {p}...".format(p=PORT))

    # enter server loop
    while True:
        try:
            #  Wait for next request from client
            message = server.recv()
            file_name = message.decode(ENCODING) + '.txt'
            print("Received request for {m} vocabulary".format(m=message))

            # check for file
            file_path = os.path.join(VOCAB_DIRECTORY, file_name)
            if not file_path_exists(file_path):
                print("--{} NOT FOUND. Sending back empty message".format(file_name))
                server.send(b"")
                continue

            print("--{} FOUND!".format(file_name))

            #  Send file contents back to client
            with open(file_path, 'rb') as fi:
                message = fi.read()
                print("--Sending following message to client: {}\n".format(message))
                server.send(message)
        except KeyboardInterrupt:
            print("Got Ctrl-C. Shutting down.")
            break


if __name__ == '__main__':
    main()
