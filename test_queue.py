import pytest
from queue_stub import *
from queue_speech_to_text import *

def test_stub_func():
	with pytest.raises(TypeError):
		stub_func()


def test_speech_func():
	with pytest.raises(TypeError):
		speech_to_text()
