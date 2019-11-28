seconds = int(input())

if seconds >= 3600:
    hours = int(seconds/3600)
    seconds = seconds - hours*3600
else:
    hours = 0

if seconds >= 60:
    minutes = int(seconds/60)
    seconds = seconds - minutes*60
else:
    minutes = 0

print("%d:%d:%d" %(hours, minutes, seconds))
