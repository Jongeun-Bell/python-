# 파일을 읽고 > 암호화 > 복호화

def xor_encrypt_decrypt(input_file, output_file):

    try:
        with open(input_file, 'rb') as infile:
            data = infile.read

        with open(output_file,'rb') as outfile:
            outfile.write(data)

    except Exception as e:
        print(f'오류{e}')


xor_encrypt_decrypt('example.txt','output.txt')