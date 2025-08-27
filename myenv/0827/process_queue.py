import multiprocessing
import time
import random

def producer_process(queue):
    print(f"생산자 프로세스 시작: {multiprocessing.current_process().name}")
    for i in range(5):
        item = f"데이터 - {i}"
        queue.put(item)
        print(f"생산:{item}")
        time.sleep(random.uniform(0.1,0.5))

        queue.put(None)
        print("생산자 프로세스 종료")

def consumer_process(queue):
    print(f"소비자 프로세스 시작: {multiprocessing.current_process().name}")
    while True:
        item = queue.get()
        if item is None:
            break
        print(f"소비:{item}")
        time.sleep(random.uniform(0.2,0.7))
    print("소비자 프로세스 종료")

if __name__ == "__main__":
    q = multiprocessing.Queue()

    prod = multiprocessing.Process(target=producer_process,args=(q,))
    cons = multiprocessing.Process(target=consumer_process,args=(q,))

    prod.start()
    cons.start()

    prod.join()
    cons.join()

    print("모든 프로세스 종료")