import zmq
import time


HOST = "localhost"
PORT = 5555
ENCODING = "utf-8"


def main():
    context = zmq.Context()

    #  Socket to talk to server
    print("Connecting to hello world server...")
    client = context.socket(zmq.REQ)
    client.connect("tcp://{h}:{p}".format(h=HOST, p=PORT))
    print("-- Connected!")
    time.sleep(1)

    for week in ["week01", "week03", "week05"]:
        print('Attempting to get vocabulary words for "{w}"'.format(w=week))
        time.sleep(2)  # wait a bit to watch it go
        print('--Sending "{}"'.format(week))
        client.send(week.encode(ENCODING))

        # read contents
        contents = client.recv()
        if contents:
            print('--Received response')
            vocabulary_list = contents.decode(ENCODING).split(',')
            print("--Vocabulary for {w}: {v}".format(w=week, v=vocabulary_list))
        time.sleep(1)


if __name__ == '__main__':
    main()

