# Display random Character from time function

import time

currentTime = time.time()

currentSeconds = int(currentTime)

number = currentSeconds % 90

Character = chr(number)

print(currentSeconds)

print(number)

print("Random character is: ", Character)