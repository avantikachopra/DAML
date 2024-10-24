# Mancala Bot

import numpy as np
import gym
import matplotlib.pyplot as plt

# Building the environment
states = 14
# [p1,p1,p1,p1,p1,p1,s1,p2,p2,p2,p2,p2,p2,s2]

actions = 6

#Parameters
epsilon = 1
alpha = 0.8
gamma = 0.95

def choose_action(Q, player):
    if player == 1:
        if np.random.uniform(0, 1) < epsilon:
            action = random_integer = np.random.randint(0, 6)
        else:
            action = np.argmax(Q)
    else:
        if np.random.uniform(0, 1) < epsilon:
            action = random_integer = np.random.randint(7, 13)
        else:
            action = np.argmax(Q)+7
    return action

def update(Q, reward, action, action1):
    predict = Q[action]
    target = reward + gamma * Q[action1]
    Q[action] += alpha * (target - predict)

# Initializing the reward
reward1 = 0
reward2 = 0

reward_list = []
Q1 = np.zeros(actions) # agent 1
Q2 = np.zeros(actions) # agent 2
seeds = np.full(states, 4)
seeds[6] = 0
seeds[13] = 0
turn = 1

print("[p1,p1,p1,p1,p1,p1,s1,p2,p2,p2,p2,p2,p2,s2]")
print(seeds)

rounds = 0
action1 = choose_action(Q1,1)

while np.sum(seeds[1:6]) > 0 or np.sum(seeds[7:13]) > 0:
    #reward calculation +10 if last in player store, +5 if in player store, +1 if in player sink, +1 for each opposite collected seed, -1 if in opponent's sink
    if turn == 1:

        distribute1 = seeds[action1]
        seeds[action1] = 0
        state = action1 + 1

        if distribute1 != 0:

            while distribute1 > 1:
                if(state != 13):
                    seeds[state] += 1
                    distribute1 -= 1

                if(state == 6):
                    reward1 += 5
                if(state >= 0 and state <= 5):
                    reward1 += 1
                if(state >= 7 and state <= 12):
                    reward1 -= 1

                state += 1
                if(state == 14):
                    state = 0

            if(state == 6): #check if ends on your store
                seeds[6] += 1
                reward1 += 10
                turn = 1 #get another turn
            elif(state == 13): #move over if ends on opponents store
                seeds[0] += 1
                reward1 -= 1
                turn = 2 #opponents turn
            else:
                turn = 2

            if(seeds[state] == 0 and state >= 0 and state <= 5):
                opposite = 12 - state
                seeds[6] += seeds[opposite] + 1
                reward1 += seeds[opposite] + 1
                seeds[opposite] = 0
            elif (state != 6 and state != 13):
                seeds[state] += 1
                if(state >= 1 and state <= 5):
                    reward1 += 1
                elif(state >= 7 and state <= 12):
                    reward1 -= 1


        else:
            turn = 2

        sum = np.sum(seeds)
        print("Player 1")
        print("Move = ", action1)
        print(seeds)
        print("Sum = ", np.sum(seeds))
        print("Reward1 = ", reward1)
        print("Turn = ", turn)
        print("")

        naction1 = choose_action(Q1, 1)

        update(Q1, reward1, action1, naction1)
        action1 = naction1

        rounds +=1

        if(rounds == 1):
            action2 = choose_action(Q2,2)

    else:

        #player 2

        # action2 = int(input("Your Move = ")) #play yourself
        # print("")

        distribute2 = seeds[action2]
        seeds[action2] = 0
        state = action2 + 1

        if distribute2 != 0:

            while distribute2 > 1:
                if (state != 6):
                    seeds[state] += 1
                    distribute2 -= 1

                if (state == 13):
                    reward2 += 5
                if (state >= 7 and state <= 12):
                    reward2 += 1
                if (state >= 0 and state <= 5):
                    reward2 -= 1

                state += 1
                if (state == 14):
                    state = 0


            if (state == 13):  # check if ends on your store
                seeds[13] += 1
                reward2 += 10
                turn = 2  # get another turn
            elif (state == 6):  # move over if ends on opponents store
                seeds[7] += 1
                reward2 -= 1
                turn = 1 # opponents turn
            else:
                turn = 1

            if (seeds[state] == 0 and state >= 7 and state <= 12):
                opposite = 12 - state
                seeds[12] += seeds[opposite] + 1
                reward2 += seeds[opposite] + 1
                seeds[opposite] = 0
            elif(state != 13 and state != 6):
                seeds[state] += 1
                if (state >= 7 and state <= 12):
                    reward1 += 1
                elif (state >= 1 and state <= 5):
                    reward1 -= 1

        else:
            turn = 1

        rounds += 1

        naction2 = choose_action(Q2, 2)

        update(Q2, reward2, action2-7, naction2-7)
        action2 = naction2

        sum = np.sum(seeds)
        print("Player 2")
        print("Move = ", action2)
        print(seeds)
        print("Sum = ", np.sum(seeds))
        print("Reward2 = ", reward2)
        print("Turn = ", turn)
        print("")





if(seeds[6] > seeds[13]):
    print("Player 1 wins! with ", seeds[6])
else:
    print("Player 2 wins! with ", seeds[13])


