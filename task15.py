def exponent(base, exp):
    power_of_exp=base**exp
    return power_of_exp
base_num=input('enter base:')
exp_num=input('enter exp:')
base_num=int(base_num)
exp_num=int(exp_num)
if exp_num>0:
    print(exponent(base_num, exp_num))
else:
    print('exp is negative integer')



