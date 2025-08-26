# 딕셔너리를 활용해 간단한 주소록 프로그램 작성 
# key: 아이디(id000) / 이름(name), 전화번호(phone), 이메일(email), 주소(address)
# 기능: 연락처 추가, 삭제, 검색, 수정, 모든 연락처 보기 

# 초기 데이터 (ID를 키로 사용)
phone_book = {
    "id001": {
        "name": "person1",
        "phone": "010-1111-1111",
        "email": "person1@gmail.com",
        "address": "Seoul Gangseo-gu"
    },
    "id002": {
        "name": "person2",
        "phone": "010-2222-2222",
        "email": "person2@gmail.com",
        "address": "Seoul Guemcheon-gu"
    },
    "id003": {
        "name": "person3",
        "phone": None,
        "email": "person3@gmail.com",
        "address": "Seoul Jongro-gu"
    }
}

# 프로그램 
while True: 
    print("\n========== Phone Book Program ==========")
    print("1. ADD")
    print("2. DELETE")
    print("3. SEARCH")
    print("4. MODIFY")
    print("5. SHOW ALL")
    print("0. EXIT")
    sel = input("CHOOSE AN OPTION")

    match sel:
        # 1. ADD (추가하기)
        case "1":
            print("Please enter ID")
            uid = input("ID: ").strip()
            if uid in phone_book:
                print("[ADD Failed] ID already exists")
                continue
            name = input("name: ").strip()
            phone = input("phone: ").strip()
            email = input("email: ").strip()
            address = input("address: ").strip()
            phone_book.setdefault(uid,{
                "name": name,
                "phone":phone,
                "email":email,
                "address":address
            })
            print(f"{uid} ADD completed.")

        # 2. DELETE (삭제하기)
        case "2":
            print("Please enter ID")
            uid = input("ID: ").strip()
            deleted = phone_book.pop(uid,None)
            if deleted is None:
                print("[DELETE Failed] ID doesn't exist")
            else:
                print("{uid} DELETE completed")

        # 3. SEARCH (검색하기)
        case "3":
            print("Please enter ID")
            uid = input("ID: ").strip()
            info = phone_book.get(uid)
            if info is None:
                print("[SEARCH Failed] ID doesn't exist")
            else:
                print(f"ID: {uid}")
                print(f"NAME: {info.get('name')}")
                print(f"PHONE: {info.get('phone')}")
                print(f"EMAIL: {info.get('email')}")
                print(f"ADDRESS: {info.get('address')}")

        # 4. MODIFY (수정하기)
        case "4":
            print("Please enter ID")
            uid = input("ID: ").strip()
            info = phone_book.get(uid)
            if info is None:
                print("[MODIFY Failed] ID doesn't exist")
                continue

            new_name = input(" NEW NAME(PRESS ENTER TO KEEP THE ORIGINAL): " ).strip()
            new_phone = input(" NEW PHONE(PRESS ENTER TO KEEP THE ORIGINAL): " ).strip()
            new_email = input(" NEW EMAIL(PRESS ENTER TO KEEP THE ORIGINAL): ").strip()
            new_address = input(" NEW ADDRESS(PRESS ENTER TO KEEP THE ORIGINAL): ").strip()

            changes = {}
            if new_name: changes["name"] = new_name
            if new_phone: changes["phone"] = new_phone
            if new_email: changes["email"] = new_email
            if new_address: changes["address"] = new_address

            if changes: 
                phone_book[uid].update(changes)
                print(f"{uid} MODIFY COMPLETED")
            else:
                print("NO CHANGES MADE")            

        # 5. SHOW ALL (전체 보기)
        case "5":
            if not phone_book:
                print("THIS PHONE BOOK IS EMPTY")
            else:
                for uid in sorted(phone_book.keys()):
                    info = phone_book[uid]
                    print(f" {uid} | {info.get('name')} | {info.get('phone')} | {info.get('email')} | {info.get('address')}")

        # 0. EXIT (프로그램 종료)
        case "0":
            print("END THE PROGRAM")
            break

        case _:
            print("INVALID NUMBER. TRY AGAIN")
