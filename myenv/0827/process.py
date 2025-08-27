import multiprocessing
import time

def count_up(name, max_count):
    """숫자를 세는 간단한 함수"""
    for i in range(1, max_count +1):
        print(f"프로세스 {name}: 카운트 {i}")
        time.sleep(0.5)

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=count_up, args=("A",5))
    p2 = multiprocessing.Process(target=count_up, args=("B",4))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

