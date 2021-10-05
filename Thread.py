from threading import Thread
from time import sleep

def thread_func(sleep_time):
    sleep(sleep_time)
    print('Wake up!')

thread = Thread(target=thread_func, args=(2,))
thread.start()
print('Some stuff')
