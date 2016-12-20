import gym
import gym_pull



gym_pull.pull('github.com/ppaquette/gym-doom')
env = gym.make('ppaquette/DoomBasic-v0')

env.configure(remotes=1) # automatically creates a local docker container
observation_n = env.reset()

while True:
    action_n = [[('KeyEvent', 'ArrowUp', True)] for ob in observation_n] # your agent here
    observation_n, reward_n, done_n, info = env.step(action_n)
    env.render()