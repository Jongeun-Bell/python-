def copy_image(source_file, destination_file):
    
    try:
        with open(source_file, 'rb') as source:
            image_data = source.read()
        with open(destination_file, 'wb') as destination:
            destination.write(image_data)
        
        print(f"{source_file}가 {destination_file}로 복사되었습니다")
        return True

    except FileNotFoundError:
        print(f"{source_file}파일을 찾을 수 없음")
    except Exception as e:
        print(f"에러:{e}")
        return False

copy_image('img.jpg','copy.jpg')