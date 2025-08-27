data = bytes([0x48,0x65,0x6c,0x6c,0x6F])

with open('binary_data.bin', 'wb') as file:
    file.write(data)