import math

def num_BTC(b):
    if b<=0:
        return 0
    reward_token = 50
    halves = (b-1)//210000
    total_reward = 0
    for i in range(0,halves):                
        
        total_reward = reward_token*210000 + total_reward
        reward_token = reward_token/2
        #print(total_reward)
    remaining_block = b - halves*210000
    #print(remaining_block)
    #print(halves)
    #print(total_reward)
    total_reward = total_reward + remaining_block * (50.0 / (2.0 ** halves))
    c = float(total_reward)
    return c