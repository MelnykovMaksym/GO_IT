from multiprocessing import Pool
import time


def factorize(number):
    count = 0
    lst = []
    while True:
        if count <= number:
            count += 1
            if number % count == 0:
                lst.append(count)
            else:
                continue
        else:
            break
    return lst


if __name__ == '__main__':
    a, b, c, d = (128, 255, 99999, 10651060)

    start = time.perf_counter()
    with Pool() as p:
        a, b, c, d = p.map(factorize, (a, b, c, d))
    finish = time.perf_counter()

    print(f'Task done in {round(finish - start, 3)} sec')

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106,
                 1521580, 2130212, 2662765, 5325530, 10651060]
