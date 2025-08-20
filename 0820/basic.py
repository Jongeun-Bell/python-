def greet(name, time_of_day='아침'):
    greetings = {
        '아침': '좋은 아침입니다',
        '점심' : '맛있는 점심 드세요'
    }
    return f"{greetings[time_of_day]},{name}님"

print(greet('jongeun'))