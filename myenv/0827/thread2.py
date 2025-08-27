import threading
import time

data = None
condition = threading.Condition()

def prepare_data():
    global data

    print("준비 스레드: 데이터 준비 중")
    time.sleep(2)

    with condition:
        data = "준비된 데이터"
        print("준비 스레드: 데이터가 준비되었습니다")
        condition.notify()


def wait_for_data():
    print("대기 스레드: 데이터를 기다립니다")

    with condition:
        condition.wait()
        print(f"대기 스레드: 데이터 '{data}'를 받았습니다")

t1 = threading.Thread(target=wait_for_data)
t2 = threading.Thread(target=prepare_data)

t1.start()
t2.start()
