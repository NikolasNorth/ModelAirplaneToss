# Model Airplane Toss

### Description
This prototype represents an horizontal slice of my game.

##### What is shown:
- Main components of the gaming experience:
  - Airplane jumping
  - Collision detection with obstacles
  - Score incrementing by 1 with every successful pass between the set of obstacles.
- Image file paths for airplanes and backgrounds are stored inside an array which can be used to add additional images later in development. (i.e. allowing for optionality for the player to change airplanes or backgrounds)
- Implemented a class called Game. When it is instantiated you can pass in the airplane image and background image of choice.

##### What is missing:
- Additional airplane and background images
- Functionality which would allow user to select, when presented with a set of options, their airplane and/or background of choice from the game window
- Scoring leaderboard

##### Additional refinements that need to be made to improve gaming experience:
- Underlying logic implementing the airplane jump animation can be tweaked to allow for a smoother animation
  - I find the initial change of acceleration upwards is too strong and the animation can follow more of a arc trajectory, rather than straight up and down
- Modify collision function within obstacle.py to make collisions with obstacles more accurate
  - I find with the upper obstacle in particular, when you get close to approaching it with your airplane it registers as a collision when it is not.

### How To Install
Model Airplane Toss is built using Pygame and can be run within a virtual environment.
Steps To Install Pygame and setup virtual environment:
- Ensure you have `pipenv` installed on your system. <br>
(https://pipenv-fork.readthedocs.io/en/latest/install.html#installing-pipenv)
- `cd` into the ModelAirplaneToss directory containing the source code from your terminal
- From your terminal, run `pipenv install` to setup your virtual environment and install pygame dependency
- At this point you should have all you need to execute the game

### How To Execute
- From your terminal, `cd` into the ModelAirplaneToss directory
- Run `pipenv run python main.py`
- A game window should appear.

### How To Play
- When you launch the game, you will be brought to the welcome screen.
- Press spacebar to start the game
- Continue pressing spacebar and use built-in gravitational force to guide your airplane through the opening between the set of obstacles
- With each successful pass, you will increment your score by 1
- Touching either of the pipes, upper window boundary or lower window boundary will result in the airplane 'crashing'
- When the airplane crashes, the game will pause. Press the escape (ESC) key on your keyboard to go to the game over screen
- Once on the game over screen, if you wish to restart the game, press the spacebar
- Otherwise, if you wish to exit the game, simply close the window
