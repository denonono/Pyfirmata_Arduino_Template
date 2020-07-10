import pyfirmata
import time

# set up board with the port the arduino is connected to
board = pyfirmata.Arduino("PORT HERE!")

# booting the arduino and looping the inputs
it = pyfirmata.util.Iterator(board)
it.start()
print("Connected!")

# set up pins as connected


# infinite while-loop acting as the arduino loop function
while True:
