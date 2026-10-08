binary = []
value = int(input('Insert value: '))
index_value = value
division_count = 0

while True:
    remaining = value // 2
    value = remaining
    if remaining == 0:
        division_count += 1
        break
    division_count += 1

def binary_encryption(index_value):
    for i in range(division_count, 0, -1):
        if index_value % 2 == 0:
            binary.append(0)
        if index_value % 2 == 1:
            binary.append(1)
        if index_value == 1 and not binary:
            binary.append(1)
            break
        index_value = index_value // 2

binary_encryption(index_value)
binary.reverse()
print(''.join(map(str, binary)))

#                        _         _                                        _     
#  _ __ ___    __ _   __| |  ___  | |__   _   _    __ _   __ _  ___  _ __  | |__  
# | '_ ` _ \  / _` | / _` | / _ \ | '_ \ | | | |  / _` | / _` |/ __|| '_ \ | '_ \ 
# | | | | | || (_| || (_| ||  __/ | |_) || |_| | | (_| || (_| |\__ \| |_) || | | |
# |_| |_| |_| \__,_| \__,_| \___| |_.__/  \__, |  \__, | \__,_||___/| .__/ |_| |_|
#                                         |___/   |___/             |_|           
