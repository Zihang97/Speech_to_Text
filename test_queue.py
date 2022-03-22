import pytest
from queue_stub import *
from queue_speech_to_text import *

def test_stub_func_without_input():
	with pytest.raises(TypeError):
		stub_func()

def test_stub_func_with_input2():
	q = multiprocessing.Queue()
	q.put(2)
	assert stub_func(q) == 2
	
def test_stub_func_with_input3():
	q = multiprocessing.Queue()
	q.put(10)
	assert stub_func(q) == 10

def test_speech_func():
	with pytest.raises(TypeError):
		speech_to_text()
