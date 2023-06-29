import time
print(time.strftime("Time :%H:%M:%S"))
hour=int(time.strftime("%H"))
minutes=int(time.strftime("%M"))
'''Good morning5:00 AM to 12:00 PM. 
Good noon 12:00 PM to 2:30 PM.
Good afternoon 2:30 PM to 5:00 PM. 
Good evening 5:00 PM to 8:00 PM. 
Good night 8 to whole night till to 5:00 AM.'''
if hour>=5 and hour<12:
    print("Good morning")
elif hour>=12 and hour<14:
    if minutes>=30:
        print("Good noon")
    else:
        print("Good morning")
elif hour>=14 and hour<17:
    if minutes>=30:
        print("Good Afternoon")
    else:
        print("Good noon")
elif hour>=17 and hour<=20:
    print("Good evening")
else:
    print("Good night")