## MiniWoB First Project

The MiniWoB++ library contains a collection of over 100 web interaction environments, along with JavaScript and Python interfaces for programmatically interacting with them. The Python interface follows the Gymnasium API and uses Selenium WebDriver to perform actions on the web browser.

In this GitHub repository, we will be creating our first MiniWoB++ Reinforcement Learning Model in the most basic environment: _click-test-2_. In this environment, our model will learn to click on the DOM element whose text is equal to "ONE" in less than 10 seconds to receive a positive reward.

### Environment Initialization:

An environmnet can be created using [gymnasium.make](https://gymnasium.farama.org/api/registry/#gymnasium.make)

The most common arguments include:

- `render_mode`: Render mode. Supported values are:
  - `None` (default): Headless Chrome, which does not show the browser window.
  - `Human`: Shows the browser window.
- `action_space_config`: Configuration for the action space. Supported values are:
  - An `ActionSpaceConfig` object.
  - A `present name`, which will instantiate an `ActionSpaceConfig` object.

### Observation Space

The `reset` and `step` methods return an observation, which is a `dict` with the following fields:
_ `utterance`: Task instruction string, such as "Click Button ONE."
_ `fields`: Environment-specific key-value pairs extracted from the utterance, such as `(("target","ONE"),)`.
_ `screenshot`: A numpy array of shape `(height, width, 3)` containing the RGB values.
_ `dom_elements`: A tuple of dicts, each listing properties like the geometry and HTML attributes of a visible DOM element.

### Action Space

The `step` method takes an `action` object, which should be a `dict` with the following fields:

- `action_type`: The action type index from `env.unwrapped.action_space_config.action_types`.
- Other fields such as `ref`, `coords`, `text`, etc. should be specified based on the action type. The action space `env.unwrapped.action_space` specifies which fields should be included.
