import multiprocessing
import time

def stub_func(req_queue):
	while not req_queue.empty():
		wait_time = req_queue.get()
		time.sleep(wait_time)
		print(f'{multiprocessing.current_process().name} complete in {wait_time}s')
		return wait_time

if __name__ == '__main__':
	num_process = multiprocessing.cpu_count()
	req_queue = multiprocessing.Queue()

	for i in range(1, 10):
		req_queue.put(i)

	processes = []
	for i in range(num_process):
		process = multiprocessing.Process(target=stub_func, args=(req_queue, ), daemon=True)
		processes.append(process)
		process.start()

	print(f'{len(processes)} processes are running')
	print('--------------------------')
	for process in processes:
		print('process id:', process.pid)
		print('process name:', process.name)
		print('parent process id:', process._parent_pid)
		print(f'{process.name} is alive: {process.is_alive()}')
		print('--------------------------')

	start = time.time()

	for process in processes:
		process.join()
	
	end = time.time()
	print('The total time spent is', f'{end-start}s')



