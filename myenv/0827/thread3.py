import time 
import concurrent.futures


def task(params):
    name, duration = params
    print(f"작업{name}시작")
    time.sleep(duration)
    return f"{name} 완료, 소요시간: {duration}초"

params =[
    ("A",2),
    ("B",1),
    ("C",3),
    ("D",1.5)
]

with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor: 
    results = list(executor.map(task,params))

    for result in results:
        print(result)