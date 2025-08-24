# 초기 데이터
phone_book = {
    "person1": {
        "phone": "010-1111-1111",
        "email": "person1@gmail.com",
        "address": "Seoul Gangseo-gu"
    },
    "person2": {
        "phone": "010-2222-2222",
        "email": "person2@gmail.com",
        "address": "Seoul Guemcheon-gu"
    },
    "person3": {
        "phone": None,
        "email": "person3@gmail.com",
        "address": "Seoul Jongro-gu"
    }
}

##### 추가 #####

# 1) 직접 조작 
phone_book["person4"] = {
    "phone": "010-4444-4444",
    "email": "person4@gmail.com",
    "address": "Seoul Mapo-gu"
}
print("추가 []:", phone_book["person4"])

# 2) update() 메소드 사용 (여러 개 한꺼번에 추가/병합 가능)
phone_book.update({
    "person5": {
        "phone": "010-5555-5555",
        "email": "person5@gmail.com",
        "address": "Seoul Songpa-gu"
    }
})
print("추가 update:", phone_book["person5"])

# 3) setdefault() 사용 (없으면 추가, 있으면 유지)
phone_book.setdefault("person6", {
    "phone": None,
    "email": None,
    "address": "Unknown"
})
print("추가 setdefault:", phone_book["person6"])

#----------------------------------------

##### 검색 #####

# 1) 직접 조작
print("검색 []:", phone_book["person1"])

# 2) get() 사용 (없을 때 기본값 반환 가능)
print("검색 get(존재):", phone_book.get("person2"))
print("검색 get(없음):", phone_book.get("ghost", "없음"))

#----------------------------------------

##### 수정 #####

# 1) 직접 조작 (필드 하나 수정)
phone_book["person2"]["phone"] = "010-2222-9999"
print("수정 []:", phone_book["person2"])

# 2) update() 사용 (여러 필드 동시 수정)
phone_book["person1"].update({
    "email": "new1@gmail.com",
    "address": "Seoul Jung-gu"
})
print("수정 update:", phone_book["person1"])

#----------------------------------------

##### 삭제 #####

# 1) 직접 조작 (del) 
del phone_book["person3"] # person3 키를 딕셔너리에서 완전히 제거
print("삭제 del:", "person3" in phone_book) # 제거 되었기 때문에 False 출력 

# 2) pop() 사용 (삭제 후 값 반환)
removed = phone_book.pop("person4", None) # person4 키가 없을 경우 None을 반환 (즉, 에러 안남)
print("삭제 pop:", removed)

#----------------------------------------

###### fromkeys() 예제 #####

# 여러 키를 미리 생성하고, 같은 초기값 지정할 때 사용
# 새 사람 추가 시 기본 구조 세팅

contacts = ["phone", "email", "address"]
phone_book["person8"] = dict.fromkeys(contacts, "미입력")
print("fromkeys 응용:", phone_book["person8"])