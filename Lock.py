from threading import RLock, Thread
from time import time, sleep

lock = RLock()


def func(locker, delay):
    timer = time()
    locker.acquire()
    sleep(delay)
    locker.release()
    print('Done', time() - timer)


t1 = Thread(target=func, args=(lock, 2))
t2 = Thread(target=func, args=(lock, 2))

t1.start()
t2.start()
print('Started')