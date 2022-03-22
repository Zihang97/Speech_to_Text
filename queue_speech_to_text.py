import deepspeech
import wave
import numpy as np
import multiprocessing
import time

def speech_to_text(model_file_path, req_queue, return_dict):
	model = deepspeech.Model(model_file_path)
	while not req_queue.empty():
		start = time.time()
		filename = req_queue.get()
		with wave.open(filename, 'r') as w:
			rate = w.getframerate()
			frames = w.getnframes()
			buffer = w.readframes(frames)
		data16 = np.frombuffer(buffer, dtype=np.int16)
		text = model.stt(data16)
		end = time.time()
		
		process = multiprocessing.current_process()
		print('process id:', process.pid)
		print('process name:', process.name)
		print('parent process id:', process._parent_pid)
		print(f'{process.name} is alive: {process.is_alive()}')
		print('--------------------------')
		time.sleep(1)
		print(f'{process.name} complete in {end-start}s')
		return_dict[filename] = text

if __name__ == '__main__':
	model_file_path = 'deepspeech/deepspeech-0.9.3-models.pbmm'
	file1 = 'deepspeech/audio/2830-3980-0043.wav'
	file2 = 'deepspeech/audio/4507-16021-0012.wav'
	file3 = 'deepspeech/audio/8455-210777-0068.wav'

	num_process = multiprocessing.cpu_count()
	req_queue = multiprocessing.Queue()
	manager = multiprocessing.Manager()
	return_dict = manager.dict()


	req_queue.put(file1)
	req_queue.put(file2)
	req_queue.put(file3)

	processes = []
	for i in range(num_process):
		process = multiprocessing.Process(target=speech_to_text, args=(model_file_path, req_queue, return_dict), daemon=True)
		processes.append(process)
		process.start()

	print(f'{len(processes)} processes are running')
	print('--------------------------')

	for process in processes:
		process.join()

	for k, v in return_dict.items():
		print(f'File {k}:', v)