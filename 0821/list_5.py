# to do 리스트 만들기 

tasks = []

# 할일 추가 
def add_task(task):
    tasks.append(task)
    print(f"{task}가 추가되었습니다")

# 할일 보기 
def view_tasks(tasks):
    for i, task in enumerate(tasks):
        print(f"{i}:{task}")

# 할일 삭제 
def completed_task(task_index):
    completed = tasks.pop(task_index)
    print(f"{completed}가 삭제되었습니다")


add_task('파이썬 마스터')
add_task('운동하기')
view_tasks()
completed_task(1)
view_tasks()
