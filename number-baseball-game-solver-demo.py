import itertools

def remove_elements(num_list, nums, strike, ball):
    i = 0
    for _ in range(len(num_list)):
        temp_strike, temp_ball = get_strike_and_ball(num_list[i], nums)

        if (strike != temp_strike or ball != temp_ball): 
            del num_list[i]
        else:
            i = i+1
    return num_list

def get_strike_and_ball(cur_num, set_num):
    temp_strike = 0
    temp_ball = 0
    for i in range(3):
        for j in range(3):
            if ( i == j and cur_num[i] == set_num[j]):
                temp_strike = temp_strike + 1
                break
            elif ( cur_num[i] == set_num[j] ):
                temp_ball = temp_ball + 1
                break
    return temp_strike, temp_ball

arr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
all_case_nums = list(itertools.permutations(arr, 3)) 
while (len(all_case_nums) != 1): 
    print("민권봇 : ", end='')
    for i in range(3):
        print(all_case_nums[0][i], end='')
    print()

    strike = int(input("strike : "))
    ball = int(input("ball  : "))

    all_case_nums = remove_elements(all_case_nums, all_case_nums[0], strike, ball)

print("민권봇 : 정답은 ", end='')
for i in range(3):
    print(all_case_nums[0][i], end='')
print()