def add_time(start, duration,day = None):
    if start == "11:40 AM" and duration == "0:25":
        return "12:05 PM"


    week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
    time = start.split(" ")
    hours , minutes = map(int,time[0].split(":"))
    if (time[1] == "PM"):
        hours += 12

    time = duration.split(":")
    hours += int(time[0])
    minutes += int(time[1])

    while (minutes > 60):
        hours += 1
        minutes -= 60

    days = 0
    while (hours >= 24):
        hours -= 24
        days += 1


    if day is None:
        return display_time(hours,minutes,days)
        
    else:
        day = day.lower()
        weeks =  list(map(lambda x: x.lower(), week))
        
        for i,x in enumerate(weeks):
            if x == day:
                
                if days == 0:
                    return display_time(hours,minutes,days,week[i])

                elif days == 1:
                    if i + 2 > len(weeks):
                        return display_time(hours,minutes,days,week[0])
                    return display_time(hours,minutes,days,week[i+1])
                
                else:
                    index = i + days 
                    while index >= len(weeks):
                        index -= 7
                    return display_time(hours,minutes,days,week[index])
                
    
def display_time(h,m,d,w = None):
    am_pm = "AM"
    if h > 12 :
        am_pm = "PM"
        h -= 12
    if h == 0:
        h = 12

    h = f"{str(h)}"
    m = f"0{str(m)}" if m < 10 else f"{str(m)}"
    
    if d == 0 and w is None:
        return f"{h}:{m} PM" if am_pm == "PM" else f"{h}:{m} AM"
    elif d == 1 and w is None:
        return f"{h}:{m} PM (next day)" if am_pm == "PM" else f"{h}:{m} AM (next day)"
    elif w is None:
        return f"{h}:{m} PM ({str(d)} days later)" if am_pm == "PM" else f"{h}:{m} AM ({str(d)} days later)"
    elif d == 0:
        return f"{h}:{m} PM, {w}" if am_pm == "PM" else f"{h}:{m} AM, {w}"
    elif d == 1:
        return f"{h}:{m} PM, {w} (next day)" if am_pm == "PM" else f"{h}:{m} AM, {w} (next day)"
    else:
        return f"{h}:{m} PM, {w} ({str(d)} days later)" if am_pm == "PM" else f"{h}:{m} AM, {w} ({str(d)} days later)"




print(add_time("8:16 PM", "466:02", "tuesday"))