# Mancala Bot

import numpy as np
import gym
import matplotlib.pyplot as plt

# Building the environment
states = 14
actions = 6

#Parameters
epsilon = 0.3
alpha = 0.8
gamma = 0.95

def choose_action(state):
    if np.random.uniform(0, 1) < epsilon:
        action = random_integer = np.random.randint(1, actions+1)
    else:
        action = np.argmax(Q[state, :])
    return action

print(Q)

def update(Q, state, state2, reward, action, action2):
    predict = Q[state][action]
    target = reward + gamma * Q[state2][action2]
    Q[state][action] += alpha * (target - predict)

# Initializing the reward
reward = 0


reward_list = []
Q1 = np.zeros((states, actions)) #agent 1
Q2 = np.zeros((states, actions)) #agent 2
seeds = np.full((states,), 4)





