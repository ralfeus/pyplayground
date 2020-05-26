# pyplayground
Module to create simple games using pygame. Aimed for kids who want learning Python in a fun way. 

The goal is to have something similar to Scratch Jr. - simple set of blocks to play with but with shift to coding instead of building with a mouse to get a taste of coding and possibility to use Python capabilities anytime you want.

# Install
```pip install pyplayground-ralfeus```

# Usage
```
import pyplayground
class Actor1(pyplayground.Actor):
  # here you override pyplayground.Actor methods you want to use
pyplayground.Game((width, height)).run(Actor1())
```
**width** and **height** are size of game window.

**run** method arguments  are the list of instances of the Actor descendants instances. 

## Any comments, proposals, requests are welcome
