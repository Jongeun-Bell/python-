# ===============================================
# 도서관 프로그램 (주석 강화판)
# - Book: 도서 정보만 관리 (SRP)
# - Member: 회원 정보 + '그 회원의 대출 목록'만 관리 (SRP)
# - Library: 도서관 전반(재고/회원/검색/대출/반납/삭제/조회) 조정자 (SRP)
#
# [적용한 SOLID 원칙]
# - SRP(단일 책임 원칙): 각 클래스가 '자기 일'만 함
#   * Book은 책 정보만, Member는 회원/대출목록만, Library는 조정/관리만
# - OCP(개방-폐쇄 원칙): 검색 기준(제목/저자/ISBN)을 메서드로 분리 →
#   나중에 새로운 검색(출판연도 범위 등) 추가 시 기존 코드 최소 수정
#
# [캡슐화(Encapsulation) 포인트]
# - Member의 대출 목록은 Member의 메서드로만 변경(외부 직접 append/remove 금지).
# - Library의 재고/회원 목록도 Library 메서드로만 변경(외부 직접 조작 금지).
# - Library는 Member 내부 상태를 직접 건드리지 않고, Member 메서드를 '호출'해 요청.
#   → 데이터 일관성(무결성) 보호 + 규칙을 한 곳에 모아 관리 가능.
# ===============================================


# ========= Book 클래스 =========
class Book:
    # __init__: '생성자' — 객체가 만들어질 때 '딱 한 번' 호출되어 초기 상태를 세팅한다.
    # 클래스가 존재한다고 자동으로 객체가 생기지 않으며, Book(...) 처럼 '직접 호출'해야 생성된다.
    def __init__(self, title, author, isbn, publish_year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publish_year = publish_year

    # __str__: print(book) 시 사람이 읽기 좋은 형태로 보이게 하는 메서드
    # 없으면 <Book object at 0x...> 같은 주소가 찍혀서 가독성이 안 좋다
    def __str__(self):
        return f"[{self.isbn}] {self.title} / 작가: {self.author} / ({self.publish_year}) 출판"


# ========= Member 클래스 =========
class Member:
    # SRP: '회원 정보'와 '그 회원의 대출 목록'만 책임진다.
    # 캡슐화: 대출 목록(borrowed)은 'Member 내부 메서드'를 통해서만 바뀌도록 설계한다.
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed = []  # 내부 상태(대출 목록) — 외부에서 직접 append/remove 하지 말 것!

    def borrow_book(self, book):
        # ✅ 캡슐화: 내부 상태 변경은 내부에서만. 외부(예: Library)는 이 메서드를 호출해 '요청'만 한다.
        # 여기서 나중에 '최대 대출 권수 제한', '중복 대출 금지', '로그 기록' 같은 규칙을 한 곳에서 관리할 수 있다.
        self.borrowed.append(book)
        print(f"{self.name} 님이 '{book.title}'을(를) 대출하셨습니다.")  # 사용자 친화 메시지

    def return_book(self, book):
        # ✅ 캡슐화: 반납도 내부에서만 상태 변경. 외부는 이 메서드를 통해서만 반납을 수행.
        if book in self.borrowed:
            self.borrowed.remove(book)
            print(f"{self.name} 님이 '{book.title}'을(를) 반납하셨습니다.")
        else:
            print(f"{self.name} 님은 '{book.title}'을(를) 빌린 적이 없습니다.")

    def __str__(self):
        # len(self.borrowed): 대출 목록(리스트)의 길이 = 현재 대출 '권수'
        return f"{self.member_id} - {self.name} (대출 {len(self.borrowed)}권)"


# ========= Library 클래스 =========
class Library:
    # SRP: 도서관 전반의 '조정자(컨트롤 타워)' 역할만 담당한다.
    #  - 재고/회원 리스트 보관
    #  - 검색/대출/반납/삭제/조회 제공
    #  - '회원의 내부 상태'는 직접 만지지 않고, 회원 메서드를 통해 요청만 한다(캡슐화)
    def __init__(self):
        self.books = []    # 보유 도서 목록 (내부 상태) — 외부에서 직접 조작 금지
        self.members = []  # 회원 목록 (내부 상태) — 외부에서 직접 조작 금지

    # --- 도서 관리 ---
    def add_book(self, book):
        # ✅ 캡슐화: 재고 변경도 라이브러리 내부 메서드로만 수행
        self.books.append(book)
        print(f"'{book.title}' 도서가 도서관에 추가되었습니다")

    def remove_book_by_isbn(self, isbn):
        # 삭제 성공/실패를 True/False로 알려주는 이유:
        #  - 사람에겐 print 메시지로 직관적 안내
        #  - 코드 흐름에선 True/False로 분기 처리 가능 → 테스트/유지보수 편리
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"[{book.isbn}] {book.title} 도서가 삭제되었습니다.")
                return True
        print(f"[{isbn}] 도서를 찾을 수 없습니다.")
        return False

    # --- 검색 ---
    def search_by_title(self, keyword):
        # 제목/저자 검색은 '부분 일치'가 일반적이므로 'in' 사용
        return [book for book in self.books if keyword in book.title]

    def search_by_author(self, keyword):
        return [book for book in self.books if keyword in book.author]

    def search_by_isbn(self, isbn):
        # ISBN은 '고유번호'라서 '완전 일치(==)'가 의미가 있다.
        return [book for book in self.books if book.isbn == isbn]

    # --- 회원 관리 ---
    def register_member(self, member):
        # 중복 회원 방지: any(...)로 간단히 검사
        if any(m.member_id == member.member_id for m in self.members):
            print(f"{member.member_id} 회원은 이미 존재합니다")
            return False
        self.members.append(member)
        print(f"{member.name} (회원 아이디: {member.member_id})이(가) 등록되었습니다")
        return True

    def find_member(self, member_id):
        # 들여쓰기 주의: 루프가 끝날 때까지 검사하고, 끝나고도 못 찾으면 None
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def unregister_member(self, member_id):
        member = self.find_member(member_id)
        if not member:
            return "해당 회원이 없습니다"
        if member.borrowed:
            return "대출 중인 책이 있어 탈퇴할 수 없습니다"
        self.members.remove(member)
        return f"{member.name}이(가) 삭제되었습니다."

    # --- 대출 / 반납 (Library↔Member 협력의 핵심) ---
    def borrow_book(self, isbn, member_id):
        # 오케스트레이션(조정)은 Library가 담당:
        # 1) 회원 찾기, 2) 재고에서 책 찾기, 3) 재고 업데이트
        # '회원 내부 상태 변경'은 Member에게 요청(메서드 호출) → 캡슐화 준수
        member = self.find_member(member_id)
        if not member:
            return "회원이 없습니다"

        for book in self.books:
            if book.isbn == isbn:
                # ✅ 회원의 내부 상태는 '회원 메서드'로만 변경 (외부 직접 append 금지)
                member.borrow_book(book)

                # ✅ 재고는 라이브러리가 관리 (대출 시 재고에서 제거해야 중복 대출 방지)
                self.books.remove(book)
                return f"{member.name} 회원님이 [{book.title}]을(를) 대출했습니다"

        return "해당 ISBN의 책이 없습니다"

    def return_book(self, isbn, member_id):
        # 반납도 동일 원리:
        # - Member: 내 대출 목록에서 제거
        # - Library: 재고로 복원
        member = self.find_member(member_id)
        if not member:
            return "회원이 없습니다"

        # 리스트 수정하며 순회 시 list(...)로 복사본을 순회 → 안전
        for book in list(member.borrowed):
            if book.isbn == isbn:
                # ✅ 회원 내부 상태는 회원이 스스로 변경
                member.return_book(book)

                # ✅ 도서관 재고 복원
                self.books.append(book)
                return f"{member.name} 회원님이 [{book.title}]을(를) 반납했습니다"

        return "회원이 해당 책을 대출 중이 아닙니다"

    # --- 조회 ---
    def list_books(self):
        # 외부에 직접 내부 리스트를 반환하기보다, '복사본'을 반환하여 방어적 프로그래밍
        return list(self.books)

    def list_members(self):
        return list(self.members)

    def member_loans(self, member_id):
        # '삼항 연산자': X if 조건 else Y
        # 여기서는 '회원이 없으면(None이면) None, 있으면 대출 목록 복사본'
        member = self.find_member(member_id)
        return None if not member else list(member.borrowed)


# ========= 실행 데모 =========
# 이 블록은 '직접 실행'일 때만 수행된다.
# - 장점: 테스트/데모 코드는 여기에서만 돌고,
#   다른 파일에서 import로 재사용할 때는 실행되지 않아 깔끔하다.
if __name__ == "__main__":
    lib = Library()

    # 도서 추가 (한 권씩)
    lib.add_book(Book("파이썬 입문", "홍길동", "111", 2020))
    lib.add_book(Book("자바 기초",   "김영희", "222", 2019))
    lib.add_book(Book("클린 코드",   "로버트 마틴", "333", 2013))

    # 회원 등록
    lib.register_member(Member("철수", "M01"))
    lib.register_member(Member("영희", "M02"))

    # 검색(OCP: 검색 기준은 메서드로 분리되어 확장 용이)
    print("\n[제목 검색: '파이썬']")
    for book in lib.search_by_title("파이썬"):
        print("-", book)

    # 대출
    print("\n[대출 진행]")
    print(lib.borrow_book("111", "M01"))  # 철수 대출 (재고에서 제거됨)
    print(lib.borrow_book("111", "M02"))  # 영희 대출 시도 → 이미 빠져서 실패가 정상

    # 회원별 대출 현황
    print("\n[M01 대출 목록]")
    loans = lib.member_loans("M01")
    if loans is not None:
        for book in loans:
            print("-", book)
    else:
        print("회원이 없습니다.")

    # 반납
    print("\n[반납 진행]")
    print(lib.return_book("111", "M01"))

    # 도서 삭제
    print("\n[도서 삭제]")
    lib.remove_book_by_isbn("333")  # 성공
    lib.remove_book_by_isbn("999")  # 실패

    # 전체 도서/회원 조회
    print("\n[도서관 보유 도서]")
    for book in lib.list_books():
        print("-", book)

    print("\n[회원 목록]")
    for member in lib.list_members():
        print("-", member)
