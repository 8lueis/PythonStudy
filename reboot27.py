p_num = {
    'kim':'01009876543',
    'lee':'01012345678',
    'lim':'01033334444'
}
print(p_num)

print(p_num['kim'])

p_num['kang'] = '01055556666'
print(p_num)

del p_num['kim']
print(p_num)

p_num['lim'] = '0233334444'
print(p_num)