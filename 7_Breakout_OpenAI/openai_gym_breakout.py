"""
author: Dominik Stec,
index:  s12623,
email:  s12623@pja.edu.pl
To run game simulation type:
 >> python openai_gym_breakout.py
as Python interpreter command
gym and numpy modules installation is need
"""
import gym
import numpy as np
import time
import random
import math

#  game environment
env_name = 'BreakoutDeterministic-v4'

env = gym.make(env_name).env

#  video
#  code indent bug in library
recording = False
env = gym.wrappers.Monitor(env, "./vid", video_callable=lambda episode_id: recording,force=True)

#  action constants
BALL = 1
RIGHT = 2
LEFT = 3

#  unused
#  low performance method
def rgb_to_gray(obs_rgb):
    np_gray = np.empty(obs_rgb.shape[:-1])
    i, j = 0, 0
    for row in obs_rgb:
        for col in row:
            gray = 0.2989 * col[0] + 0.5870 * col[1] + 0.1140 * col[2]
            np_gray[i][j: j+1] = gray
            j = j+1
        i = i+1
        j = 0
    return np_gray

#  hyperparameters
#  learning rate - how strong should be Q-value updated after each step; 0 < alpha <= 1
alpha = 0.1
#  discount factor - a reward should be choose now in this step or in long term steps average in future; 0 <= gamma <= 1
gamma = 0.6
#  more exploration with random actions and more negatives rewards or exploatation with q-value actions; 0 <= eps <= 1
epsilon = 0.1

q_table = np.zeros(env.reset().shape[:-1])

#  episode is one round
#  100 iter == 1 hour
for episode in range(500):
    reward = 0
    reward_sum_1 = 0
    reward_sum_2 = 0
    randomize_actions = np.zeros(10)
    obs, _, _, _ = env.step(BALL)
    if episode % 10 == 0:
        print(f'game round: {episode}')
    #  step is single player move
    for step in range(30):
        #  exploration or exploatation
        if random.uniform(0,1) < epsilon:
            action = random.randint(2, 3)
        else:
            action = np.argmax(q_table[obs])

        #  action numbers mapping
        if action == 0:
            action = RIGHT
        elif action == 1:
            action = LEFT

        next_obs, reward, done, info = env.step(action)

        #  policy
        if reward == 1:
            reward = 20
        reward_sum_1 = reward_sum_1 + reward
        if reward_sum_1 <= 3:
            reward = -10
        elif reward_sum_1 == 0:
            reward = -5
        elif reward_sum_1 >= 3:
            reward = 50
        randomize_actions[step % 10] = action
        if RIGHT in randomize_actions and not LEFT in randomize_actions:
            reward = -2
        elif LEFT in randomize_actions and not RIGHT in randomize_actions:
            reward = -2
        else:
            reward = 1

        #  Q-table
        old_value = q_table[obs, action]
        next_max = np.max(q_table[next_obs])
        new_value = (1-alpha) * old_value + alpha * (reward + gamma * next_max)
        q_table[obs, action] = new_value
        obs = next_obs

        #  render game view
        env.render(mode='human')

        #  statistics
        if reward > 0:
            reward_sum_2 += 1

        #  end of round
        if done:
            accuracy = reward_sum_2/step*100
            reward_percent = reward/step*100
            loc_time = time.localtime()
            print(f'timestamp: {time.strftime("%H:%M:%S", loc_time)}')
            print(f'accuracy: {math.floor(accuracy)} %')
            print(f'rewards: {math.floor(reward_percent)} % \n')
            env.reset()
            break

env.close()