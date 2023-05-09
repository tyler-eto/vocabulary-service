# Vocabulary-Service
This service is used to serve up weekly vocabulary words.


## Requirements
```bash
# inside your python3 virtual environment
pip install -r requirements.txt
```


## Usage
Service is meant to be run locally. User can define service by editing PORT variable in server.py. User can define vocabulary file directory by editing VOCAB_DIRECTORY variable in server.py. Weekly files are expected to be comma-separated .txt files.
```python
# inside your python3 virtual environment
python server.py

# to shut down. Press Ctrl-C
```


## How to REQUEST data
Example in python using zmq library:
1. First connect to socket at "tcp://localhost:5555"
```python
>>> import zmq
>>> context = zmq.Context()
>>> client = context.socket(zmq.REQ)
>>> client.connect("tcp://localhost:5555")
```
2. Send a request for a week's vocabulary words in the following format, encoded in utf-8
```python
>>> message = "week01".encode('utf-8')
>>> client.send(message)
```
Example request strings:
* week01
* week02
* week03
* week04
* week05


## How to RECEIVE data
Client will receive a utf-8 encoded response containing the file contents from the desired week. Response will be 10 vocabulary words comma separated

```python
>>> response = client.recv()
>>> contents = response.decode('utf-8')
>>> words = contents.split(',')
>>> print(words)
['calm', 'annoy', 'mumble', 'note', 'report', 'squirm', 'focus', 'feast', 'protect', 'lovely']
```

#### For sequence diagram see UML_sequence.png
