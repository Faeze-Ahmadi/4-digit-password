# find multiple correct passwords in a numeric range

for i in range(1000, 9999):
    i_str = str(i)
    digit_1 = int(i_str[0])
    digit_2 = int(i_str[1])
    digit_3 = int(i_str[2])
    digit_4 = int(i_str[3])

    if digit_3 / digit_1 != 4:
        continue
    if digit_4 % 2 != 0:
        continue
    

