# Ultimate-Tic-Tac-Toe

## Installing

Download the Python 3 installer package from the official website and install it, if not installed previously.

Run the following in the terminal to install the PyGame and NumPy libraries

```bash
pip install pygame
pip install numpy
```

## Running the application
Download the source code from the repository and run the file just as any other Python script (.py) file.

```
python uttt.py
```

Before running the application player can choose what algorithm he wants to use: ordinary minimax algorithm or its improved version with alpha beta prunning

The `depth` variable can be changed to set the difficulty level(performance of AI).

The `turn`  variable can be changed to define who is doing first turn: 

Human moves first
```
turn = -1 
```
AI moves first
```
turn =  1 
```
Random choice
```
turn = random.choice([-1, 1])
```
