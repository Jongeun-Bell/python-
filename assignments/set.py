# 집합 과제 

users = {
    "Alice": ["music", "movies", "reading"],
    "Bob": ["Sports", "trip", "music"],
    "Charlie": ["programming", "game", "movies"],
    "David": ["cooking", "trip", "photograph"],
    "Eve": ["programming", "reading", "music"],
    "Frank": ["sports", "game", "cooking"],
    "Grace": ["movies", "trip", "reading"]
}

def common_interest(u1, u2):
    set1 = set(users[u1])
    set2 = set(users[u2])
    return set1 & set2 


def reply_common_interest(u1,u2):
    common = common_interest(u1,u2)
    if common: 
        return f"{u1}와 {u2}의 공통 관심사는 {common} 입니다"
    else:
        return f"{u1}와 {u2}는 공통 관심사가 없습니다."
    

print(reply_common_interest("Eve","Charlie")) # 공통 관심사 1개 
print(reply_common_interest("Alice","Grace")) # 공통 관심사 2개 
print(reply_common_interest("Frank","Grace")) # 공통 관심사 없음 










