previous_num = 0

for i in range(10):
    if i>previous_num:
        current_num = i
        
        print(f'previous number = {previous_num}, current number = {current_num}, sum = {current_num + previous_num}')

    previous_num = i
   