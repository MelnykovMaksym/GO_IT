import string
from time import sleep
from threading import Thread, RLock

sleep_time = 0.3
lock = RLock()

def Count_alphavet(locker, x):
    alphavet = string.ascii_uppercase
    locker.acquire()
    for letter in alphavet:
        print(letter)
        sleep(x)
    locker.release()


def Count_numbers():
    count = 0
    while count < 27:
        print(count)
        count += 1
        sleep(0.3)

t1 = Thread(target=Count_alphavet,args=(lock,sleep_time))
t1.start()
t2 = Thread(target=Count_numbers)
t2.start()
