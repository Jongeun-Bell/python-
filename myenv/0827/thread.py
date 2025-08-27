import threading
import time

def background_task():
    while True:
        print("백그라운드 작업 실행 중")
        time.sleep(1)


deamon_thread = threading.Thread(target=background_task,daemon=True)
deamon_thread.start()

print("메인 쓰레드 시작")
time.sleep(2)
print("메인 쓰레드 종료")