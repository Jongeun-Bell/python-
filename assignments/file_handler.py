############################### 과제 #################################
# file_handler.py
# 1) 텍스트/CSV/JSON/바이너리 읽기·쓰기
# 2) 다양한 오류 처리 (파일 없음/권한/형식 오류)
# 3) 사용자 정의 예외 계층
# 4) 로깅으로 오류 기록
# 5) 모든 파일 작업은 with 사용
#####################################################################

import csv
import json
import logging 
import os                    # 상위 폴더 자동 생성을 위해 필요


# 4) 로깅으로 오류 기록 > 파일에 기록 (레벨 INFO 이상)
logging.basicConfig(
    filename="fileio.log",   # 로그 파일 이름
    level=logging.INFO,      # 로그 레벨 (DEBUG < INFO < WARNING < ERROR < CRITICAL)
    format="%(asctime)s %(levelname)s %(name)s:%(lineno)d - %(message)s",
    encoding="utf-8"
)

log = logging.getLogger(__name__)

# 3) 사용자 정의 예외 계층 (함수에서 쓰이므로 먼저 정의)
class FileAccessError(Exception):
    """파일 접근 관련 오류 (경로 없음, 권한, OS 에러 등)"""
class InvalidFormatError(Exception):
    """파일 형식/내용 오류 (JSON, CSV 파싱 실패 등)"""

# -------------------------------
# 공통 safe_open 함수
# -------------------------------
def safe_open(path:str, mode:str, encoding:str = "utf-8"):
    if any(m in mode for m in ("w", "a", "x", "+")):
    # 쓰기/추가/생성/갱신 모드에서는 상위 폴더를 자동 생성
        parent = os.path.dirname(path)
        if parent:
            os.makedirs(parent, exist_ok=True)
    try:
        if "b" in mode:
            return open(path,mode)
        return open(path, mode, encoding=encoding,newline="")
    except FileNotFoundError as e:
        log.exception("File not found: %s", path)
        raise FileAccessError(f"File not found: {path}") from e
    except PermissionError as e:
        log.exception("Permission denied: %s", path)
        raise FileAccessError(f"Permission denied: {path}") from e
    except OSError as e:
        log.exception("OS error: %s", path)
        raise FileAccessError(f"File access error: {path}") from e
    

# -------------------------------
# 1-1) Text
# -------------------------------
def read_txt(path:str, encoding:str = "utf-8") -> str:
    log.info("reading text file: %s", path)
    with safe_open(path, "r", encoding) as f:
        return f.read()

def write_txt(path: str, text:str, encoding:str ="utf-8") -> None:
    log.info("writing text file: %s", path)
    with safe_open(path,"w",encoding) as f:
        f.write(text)


# -------------------------------
# 1-2) JSON
# -------------------------------
def read_json(path:str, encoding:str="utf-8"):
    log.info("reading json file: %s", path)
    try: 
        with safe_open(path,"r",encoding) as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        log.exception("json read: parsing failed: %s",path)
        raise InvalidFormatError(f"json format error:{path}") from e 
    

def write_json(path: str, data, encoding: str = "utf-8") -> None:
    log.info("Writing JSON file: %s", path)
    try:
        with safe_open(path, "w", encoding) as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except TypeError as e:
        log.exception("JSON write: invalid data format: %s", path)
        raise InvalidFormatError(f"JSON serialization error: {path}") from e


# -------------------------------
# 1-3) CSV
# -------------------------------
def read_csv(path:str, encoding:str="utf-8"):
    log.info("reading csv file: %s", path)
    try:
        with safe_open(path, "r",encoding) as f:
            reader = csv.reader(f)
            return list(reader)
    except csv.Error as e:
        log.exception("CSV read: parsing failed: %s", path)
        raise InvalidFormatError(f"CSV format error: {path}") from e
    
def write_csv(path: str, rows, encoding: str = "utf-8") -> None:
    log.info("Writing CSV file: %s", path)
    try:
        with safe_open(path, "w", encoding) as f:
            writer = csv.writer(f)
            writer.writerows(rows)
    except csv.Error as e:
        log.exception("CSV write: invalid data: %s", path)
        raise InvalidFormatError(f"CSV write error: {path}") from e
    
# -------------------------------
# 1-4) Binary
# -------------------------------
def read_binary(path: str) -> bytes:
    log.info("Reading binary file: %s", path)
    with safe_open(path, "rb") as f:
        return f.read()

def write_binary(path: str, data: bytes) -> None:
    log.info("Writing binary file: %s", path)
    with safe_open(path, "wb") as f:
        f.write(data)

# -------------------------------
# 샘플 파일을 코드로 생성하는 헬퍼
# -------------------------------
def init_samples(base_dir: str = ".") -> None:
    """Create sample text/json/csv/binary files under base_dir."""
    # 상위 폴더는 safe_open이 자동 생성하므로, 경로만 맞춰서 쓰면 됨
    write_txt(f"{base_dir}/sample.txt", "Hello from text!")
    write_json(f"{base_dir}/sample.json", {"ok": True, "items": [1, 2, 3]})
    write_csv(f"{base_dir}/sample.csv", [
        ["name", "age"],
        ["Alice", 30],
        ["Bob", 25],
    ])
    write_binary(f"{base_dir}/sample.bin", b"\x00\x01\x02ABC")


# -------------------------------
# 실행 예시
# -------------------------------
if __name__ == "__main__":
    try:
        # 샘플 파일 생성 (하위 폴더 'demo'에 생성)
        init_samples("demo")

        # 생성한 파일 읽기
        print("TXT:",  read_txt("demo/sample.txt"))
        print("JSON:", read_json("demo/sample.json"))
        print("CSV:",  read_csv("demo/sample.csv"))
        print("BIN:",  read_binary("demo/sample.bin"))

    except (FileAccessError, InvalidFormatError) as e:
        print("Error:", e)