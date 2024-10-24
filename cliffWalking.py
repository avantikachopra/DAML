import numpy as np
import gym
import matplotlib.pyplot as plt

# Building the environment
env = gym.make('CliffWalking-v0', render_mode="rgb_array")

# Defining the different parameters
epsilon = 0.1
total_episodes = 10000
max_steps = 100
alpha = 0.8
gamma = 0.95
total_trials = 10


# Function to choose the next action
def choose_action(state):
    if np.random.uniform(0, 1) < epsilon:
        action = env.action_space.sample()
    else:
        action = np.argmax(Q[state, :])
    return action


# Function to learn the Q-value
def update(state, state2, reward, action, action2):
    predict = Q[state][action]
    target = reward + gamma * Q[state2][action2]
    Q[state][action] += alpha * (target - predict)


# Initializing the reward
reward = 0

# Plotting rewards and episode lengths
reward_list = []
episode_list = []
qmatrix_list = np.zeros((env.observation_space.n, env.action_space.n))
temp1 = []
temp2 = []

# Starting the SARSA/Q-Learning learning
for trial in range(total_trials):
    Q = np.zeros((env.observation_space.n, env.action_space.n))

    for episode in range(total_episodes):
        t = 0
        sum1 = 0
        state1, info1 = env.reset()
        action1 = choose_action(state1)

        while t < max_steps:
            # Visualizing the training
            env.render()
            # Getting the next state
            state2, reward, done, truncated, info = env.step(action1)
            if done:
                reward += 99

            # Choosing the next action
            action2 = choose_action(state2)
            # Learning the Q-value
            update(state1, state2, reward, action1, action2)
            state1 = state2
            action1 = action2

            # Updating the respective values
            t += 1
            sum1 += reward

            # If at the end of learning process
            if done:
                break

        temp1.append(sum1)
        temp2.append(t)
        reward_list.append(temp1)
        episode_list.append(temp2)

        for k in range(0, 48):
            for l in range(0, 4):
                qmatrix_list[k][l] = (qmatrix_list[k][l] + Q[k][l]) / 2

final_reward = []
final_episode = []
for i in range(0, total_episodes):
    temp3 = 0
    temp4 = 0
    for j in range(0, total_trials):
        temp3 += reward_list[j][i]
        temp4 += episode_list[j][i]
    final_reward.append(temp3 / total_trials)
    final_episode.append(temp4 / total_trials)
