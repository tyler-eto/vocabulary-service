import zmq
import time


HOST = "localhost"
PORT = 5555
ENCODING = "utf-8"


def main():
    context = zmq.Context()

    #  Socket to talk to server
    print("Connecting to hello world server...")
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://{h}:{p}".format(h=HOST, p=PORT))
    print("-- Connected!")
    time.sleep(1)

    for week in ["week01", "week03", "week05"]:
        print('Attempting to get vocabulary words for "{w}"'.format(w=week))
        time.sleep(2)  # wait a bit to watch it go
        socket.send(week.encode(ENCODING))

        # read contents
        contents = socket.recv()
        if contents:
            vocabulary_list = contents.decode(ENCODING).split(',')
            print("\tVocabulary for {w}: {v}".format(w=week, v=vocabulary_list))
        time.sleep(1)


if __name__ == '__main__':
    main()
