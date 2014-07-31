import time
from ThreadPool import ThreadPool


def test_job(id):
	print(id)
#	print(sleep)
	print('job is doing!')


def test():
	print('start testing')
	tp = ThreadPool()
	for i in range(15):
		time.sleep(0.1)
		tp.add_job(test_job, i)
	
	t = time.time()
	tp.wait_for_complete()
	
	print('s:'+str(time.time()-t))
	print('end testing')
		
if __name__ == '__main__':
	test()