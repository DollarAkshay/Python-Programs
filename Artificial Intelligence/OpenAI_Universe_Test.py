import gym
MAX_STEPS = 20
env = gym.make('CartPole-v0')
env.monitor.start('/tmp/cartpole-experiment-1', force=True, video_callable=False)

for i_episode in range(200):
    observation = env.reset()
    for t in range(MAX_STEPS):
        env.render()
        print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break
env.monitor.close() 