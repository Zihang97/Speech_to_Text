# EC530_Speech_to_Text
This project is a speech-to-text module that can handle requests from multiple users simultaneously to transfer speech (audio file) to text. It builds a queue system combined with multiprocessing to manage multiple requests.

## Phase1: Build Queue System
`Phase1` builds the queue system with multiprocessing but use stub function to test. The codes for `Phase1` lie in the file [queue_stub.py](./queue_stub.py). The requests to the stub function (function calls with different parameters) are put into the queue and multiple processes are started to consume the queue at the same time. Python module `multiprocessing` is used to control multiple processes. The queue system uses class `multiprocessing.Queue` in `multiprocessing` module instead of `queue.Queue` (which is a near clone but slightly different).

<img src="picture/stub1.PNG" height=400> <img src="picture/stub2.PNG" height=400>

## Phase2: Speech to Text
<img src="picture/speech.PNG" height=400>
