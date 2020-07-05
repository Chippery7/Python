import random
import time
num = random.randint(1,100)
def playgame(max):
    t1_start = time.time()
    while True:
        print('Guess the random number')
        guess = input()
        i = int(guess)
        if i == num:
            print('You\'ve guessed correctly!')
            end = input("Press enter to stop timer")
            end_time = time.time()
            duration = int(end_time - t1_start)
            print("It took", duration, "seconds")
            break
        elif i < num:
            print('Guess higher,kid')
        elif i > num:
            print('Guess lower,kid')

playgame(100)
        
