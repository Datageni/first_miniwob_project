import time
import gymnasium
import miniwob
from miniwob.action import ActionTypes


gymnasium.register_envs(miniwob)

# [Environment]{click-test-2-v1}
env = gymnasium.make('miniwob/click-test-2-v1', render_mode='human')

try:
    observation, info = env.reset()
    assert observation['utterance'] == "Click button ONE."
    assert observation['fields'] == (('target', 'ONE'),)
    time.sleep(2)


    for element in observation['dom_elements']:
        if element['text'] =='ONE':
            break
    
    action = env.unwrapped.create_action(ActionTypes.CLICK_ELEMENT, ref=element['ref'])
    observation, reward, terminated, truncated, info = env.step(action)

    print(reward)
    assert terminated is True
    time.sleep(2)

finally:
    print('Done')