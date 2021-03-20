# DinoRunnerChromeAI

### *What it is?* ###
This project shows an implementation of AI in a popular game of Google Chrome users, *Dino Runner*.

By using Python programming language and knowledge of Objected Oriented Programming, you can develop a simple game using *Pygame* library.

As well as by reading documentation of [NEAT](https://neat-python.readthedocs.io/en/latest/), you are able to implement an Artifitial Inteligence to the very same game. This tool manages to help you create a simple code for an AI to automatically play the Dinosaur Game of this project, along with what your creativity can think of. 

#

### *Used Libraries* ###
- Pygame
- Neat-Python (Neural Network)

To run this program you need to install these libraries, you can do this by:

*write this lines of code in the terminal*

``` pip install pygame ```

``` pip install neat-python ```

#

### *Game Folder* ###
Inside the 'Game' folder you'll find another foler called 'IMGS' which contain the assets | images drawn on screen. 

You'll also find the objects (obstacles and the dinosaur) that may collide with each other. These files are: 
- Bird.py
- Cactus.py
- Dino.py

To run and specify the Neural Network used, you-ll find the file:
- config-feedforward.txt

Finally the last 2 python files will execute the game.
- DinoGame: is used to play the game with Bird Obsacles by yourself
- DinoGame_withAI : will implement NEAT to play the game automatically
