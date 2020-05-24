# pyplayground
Module to create simple games using pygame. Aimed for kids who want learning Python in a fun way
# Usage
```
import pyplayground
class Actor1(pyplayground.Actor):
  # here you override pyplayground.Actor methods you want to use
pyplayground.Game().init((width, height)).run(Actor1())
```
**width** and **height** are size of game window.

**run** method arguments  are the list of instances of the Actor descendants instances. 

## Any comments, proposals, requests are welcome