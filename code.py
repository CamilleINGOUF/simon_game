import time
import random
from adafruit_circuitplayground.express import cpx

LOSE_NOTE = 100
WIN_TONE  = 420

ANWSER_TIME = 3.0
LOOP_DELAY  = 0.250

## All button of the game, with the correct pads, pixels and tone
PLAYABLE_BUTTONS = {
  1 : { 'pads':(4,5), 'pixels':(0,1,2), 'color':0x00FF00, 'note':396},
  2 : { 'pads':(6,7), 'pixels':(2,3,4), 'color':0xFFFF00, 'note':484},
  3 : { 'pads':(1, ), 'pixels':(5,6,7), 'color':0x0000FF, 'note':610},
  4 : { 'pads':(2,3), 'pixels':(7,8,9), 'color':0xFF0000, 'note':445},  
}

## create a random sequence of numbers from 1 to 4
## The sequence is always of length 8
def random_sequence():
    return [random.randint(1,4) for i in range(8)]

## Used to display the a button on the matching pixels
## Will also play the matching tone
def show_button(button, duration):
    cpx.pixels.fill(0)
    for p in button['pixels']:
        cpx.pixels[p] = button['color']
    if button['note'] == None:
        time.sleep(duration)
    else:
        cpx.play_tone(button['note'], duration)
    cpx.pixels.fill(0)
    
## Shows the sequence to a certain step
## e.g. : Step = 2, will show the first two sequence's elements
def show_sequence(sequence, step):    
    duration = 0.7
    for b in range(step):
        time.sleep(0.01)
        show_button(PLAYABLE_BUTTONS[sequence[b]], duration)    

## Will tell use if a given pad is being touched or not
def cap_map(b):
    if b == 1: return cpx.touch_A1
    if b == 2: return cpx.touch_A2
    if b == 3: return cpx.touch_A3
    if b == 4: return cpx.touch_A4
    if b == 5: return cpx.touch_A5
    if b == 6: return cpx.touch_A6
    if b == 7: return cpx.touch_A7    
    
## Returns the current touched pad
## Returns None if none is touched
def get_button_press():
    for button in PLAYABLE_BUTTONS.values():
        for pad in button['pads']:
            if cap_map(pad):
                show_button(button, LOOP_DELAY)
                return button
    return None

## Called if game is lost
## Just shows a red circle with the losing tone
def game_lost(step):
    cpx.pixels.fill(0xFF0000)
    cpx.play_tone(LOSE_NOTE, 1.5)
    
    while True:
        pass
    
## Called if the game is won
## Display a pattern and then a green circle
def game_won():
    for i in range(3):
        show_button(PLAYABLE_BUTTONS[4], 0.1)        
        show_button(PLAYABLE_BUTTONS[2], 0.1)        
        show_button(PLAYABLE_BUTTONS[3], 0.1)        
        show_button(PLAYABLE_BUTTONS[1], 0.1)  
    
    cpx.pixels.fill(0x00FF00)
    cpx.play_tone(WIN_TONE, 1.5)

    while True:
        pass               

## Initiate the game ##
cpx.pixels.fill(0)
cpx.pixels.brightness = 0.005
cpx.pixels[0] = 0xFFFFFF
sequence = random_sequence()
current_step = 1
########################

while True:
    ## The game startes when you press a or b
    if cpx.button_b or cpx.button_a :
        while True:
            ## shows the sequence to the current step
            show_sequence(sequence, current_step)
    
            ## Reads player answer to the displayed sequence
            ## if The player chose the wrong answer or take to much time, he loses
            for step in range(current_step):
                start_answer_time = time.monotonic()
                answer = None
                while (time.monotonic() - start_answer_time < ANWSER_TIME) and (answer == None):
                    answer = get_button_press()
                if answer != PLAYABLE_BUTTONS[sequence[step]]:
                    game_lost(sequence[step])

            current_step += 1
            if current_step > len(sequence):
                game_won()
              
            time.sleep(LOOP_DELAY)