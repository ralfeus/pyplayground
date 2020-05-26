import pyplayground as ppg
import time

class Actor1(ppg.Actor):
    def __init__(self):
        self.set_skin('image1.png')
        self.set_heading(-90)
        
    def on_key_down(self, key):
        if key == ppg.K_UP:
            self.move(1)
        elif key == ppg.K_DOWN:
            self.move(-1)
        elif key == ppg.K_RIGHT:
            self.turn(5)
        elif key == ppg.K_LEFT:
            self.turn(-5)
        elif key == ppg.K_1:
            self.strife(-2)
        elif key == ppg.K_2:
            self.strife(2)
        # print(self.touches_actor('Actor2'))
        time.sleep(.01)
        
    def on_start(self):
        self.show()
    
class Actor2(ppg.Actor):
    def __init__(self):
        self.set_skin('ball.png')
        self.set_position(200, 100)
        self.direction = 1
        
    def on_start(self):
        self.show()
        #self.run_forever(self.wander)
        
    def wander(self):
        if self.touches_edge():
            self.direction *= -1
        self.move(5 * self.direction)
        time.sleep(.1)

ppg.Game((640, 480)).run(Actor2(), Actor1())