'''
线程池
'''
import queue, sys, threading


class Worker(threading.Thread):
	'''
	工作线程
	'''
	
	#  线程闲置等待时间
	Default_Timeout = 5
	
	def __init__(self, workQueue, **kwargs):
		
		threading.Thread.__init__(self, kwargs = kwargs)
		
		self.timeout = Worker.Default_Timeout
		self.setDaemon(True)
		self.workQueue = workQueue
		self.start()

		
	def run(self):
		while True:
			try:
				callable, args, kwargs = self.workQueue.get(timeout = self.timeout)
				res = callable(args)
			except queue.Empty:  #  任务队列空的时候结束此线程
				break
			except :
				print(sys.exc_info())
				raise


class ThreadPool:
	'''
	线程池
	'''
	
	#  默认线程数量
	Default_Number = 8
	
	def __init__(self, num_of_threads = Default_Number):
	
		self.workQueue = queue.Queue()
		self.threads = []
		self.__createThreadPool(num_of_threads)
	
	
	def __createThreadPool(self, num_of_threads):
		
		for i in range(num_of_threads):
			thread = Worker(self.workQueue)
			self.threads.append(thread)
	
	
	def wait_for_complete(self):
		
		#等待所有线程完成。
		while len(self.threads):
			thread = self.threads.pop()
			
			#等待线程结束
			if thread.isAlive():  #  判断线程是否还存活来决定是否调用join
				thread.join()
	
	
	def add_job(self, callable, *args, **kwargs):
		self.workQueue.put((callable, args, kwargs))