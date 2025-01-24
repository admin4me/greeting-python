# I am going to create a python program which will greet you as good morning, good afternoon, good evening, depending on current time
import time
timestamp = time.strftime('%H')
timestamps = int(timestamp)
if timestamps > 17:
    print("Good Evening")
elif timestamps > 12:
    print("Good Afternoon")
else:
    print("Good Morning")
