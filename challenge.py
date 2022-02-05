import time 
import os


def timer(t):
    t = t*60 #Convert in minutes
    while t:
        mins = t // 60 #int division
        secs = t % 60 #The module
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

def run():
    os.system("clear")
    pomodoro_times = 0
    while True:
        print("Pomodoro starts now! Remaining time: ")
        timer(25)
        print("Time to break")
        timer(5)
        os.system("clear") # This is for clearing the command line


        if pomodoro_times < 4:
            continue
        else:
            print("No more")
            break

    
if __name__ == '__main__':
    run()
