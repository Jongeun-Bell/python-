import threading
import time

event = threading.Event()

def waiter():
    print("대기자: 이벤트를 기다리는 중")
    event.wait()
    print("대기자: 이벤트를 수신하고 작업 진행")

def setter():
    print("설정자: 작업 중")
    time.sleep(3)
    print("설정자: 이제 이벤트를 설정합니다")
    event.set()

t1 = threading.Thread(target=waiter)
t2 = threading.Thread(target=setter)

t1.start()
t2.start()