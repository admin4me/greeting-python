# I am going to create a python program which will greet you as good morning, good afternoon, good evening, depending on current time
import time
timestamp = time.strftime('%H')
timestamps = int(timestamp)
if timestamps > 00:
    print("Good Morning")
elif timestamps > 12:
    print("Good Afternoon")
else:
    print("Good Evening")