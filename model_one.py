# [Libraries]{Reinforcement Learning}
import time
import gymnasium
import miniwob
from miniwob.action import ActionTypes

# [Registration of MiniWob++ Environments]
gymnasium.register_envs(miniwob)

# [Environment]{click-test-2-v1}(Setting render mode to human so we can see it)
env = gymnasium.make('miniwob/click-test-2-v1', render_mode='human')

# [Number of iterations]{Setting a number of iterations for the model}
n_iters = 20

# [try-finally block]{Proper cleanup}
try:
    for _ in range(n_iters):
        # [Starting episode]
        observation, info = env.reset()
        # [Utterance]{Setting utterance value to the text below}
        assert observation['utterance'] == "Click button ONE."
        # [Fields]{Setting the "target" and "ONE" fields in the observation}
        assert observation['fields'] == (('target', 'ONE'),)
        # [Time interval]{Setting time interval for observation}
        time.sleep(2)
        # [DOM elements search]{Searching the DOM element with text value equal to "ONE"}
        for element in observation['dom_elements']:
            # [Breaking search]{Breaking loop if we find the element}
            if element['text'] == 'ONE':
                break
        # [Action]{Setting action to click element}
        action = env.unwrapped.create_action(ActionTypes.CLICK_ELEMENT, ref=element['ref'])
        # [Episode variables]{Retrieving all variables for the action in every step}
        observation, reward, terminated, truncated, info = env.step(action)
        # [Time interval]
        time.sleep(2)
        # [Reward Display]{Printing Reward}
        print(reward)
        # [Terminating Episode]
        assert terminated is True
        if terminated:
            observation, info = env.reset()

finally:
    # [Closing environment]{When everything is done we close the environment}
    env.close()
