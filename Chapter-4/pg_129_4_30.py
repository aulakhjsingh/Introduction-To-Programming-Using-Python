import time

hrs, mins = eval(input('Enter the time zone offset to GMT (Hrs, Mins): '))

# Get current time
currentTime = time.time()

# Obtain the total seconds since midnight, Jan 1, 1970
totalSeconds = int(currentTime + ((hrs * 60 * 60) + (mins * 60)))

# Get the current second
currentSecond = totalSeconds % 60

# Obtain the total minutes
totalMinutes = totalSeconds // 60

# Compute the current minute in the hour
currentMinute = totalMinutes % 60

# Obtain the total hours
totalHours = totalMinutes // 60

# Compute the current hour
currentHour = totalHours % 24

# Display results
if currentHour >= 12:
    print("Current time is", currentHour % 12, ":", currentMinute, ":", currentSecond, "PM")
else:
    print("Current time is", currentHour % 12, ":", currentMinute, ":", currentSecond, "AM")
