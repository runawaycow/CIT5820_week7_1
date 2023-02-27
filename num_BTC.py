import math

def num_BTC(b):
    if b<=0:
        return 0
    reward_token = 50
    halves = (b-1)//210000
    total_reward = 0
    for i in range(0,halves):
        reward_token = reward_token/2
        total_reward = reward_token*210000
    remaining_block = b - halves*210000
    print(remaining_block)
    total_reward = total_reward + remaining_block * (50.0 / (2.0 ** halves))
    c = float(total_reward)
    return c


