#import the time module
import time
class countdown:
#define the countdown function
    def countdown(t):

        while  t >= 0:
            mins,secs = divmod(t, 60) # 60 define that one minute is 60 seconde
            timer = '{:02d}:{:02d}'.format(mins,secs)
            print(timer, end="\r") #force the cursor to go back to the start of the screen so the next line printed will overwrite the previous one
            time.sleep(1) # make the code to wait one second 
            t -= 1
        if t == -1:
            print("Timer stop")
        
    t = 80 #define the time

    countdown(int(t))


