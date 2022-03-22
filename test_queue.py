import pytest
from queue_stub import *
from queue_speech_to_text import *

def test_stub_func_without_input():
	with pytest.raises(TypeError):
		stub_func()

def test_stub_func_with_input2():
	start = time.time()
	q = multiprocessing.Queue()
	q.put(2)
	stub_func(q)
	end = time.time()
	assert end - start >= 2

def test_stub_func_with_input3():
	start = time.time()
	q = multiprocessing.Queue()
	q.put(3)
	stub_func(q)
	end = time.time()
	assert end - start >= 3

def test_speech_func():
	with pytest.raises(TypeError):
		speech_to_text()
