def format_duration(seconds):   
    years = ""
    days = ""
    hours = ""
    minut = ""
    secon= ""
    year = 0
    day = 0
    hour = 0
    mnt = 0
    sec = 0
    if seconds == 0:
        return 'now'
    if  seconds < 60:
        sec = seconds
    elif 60 <= seconds < 3600:
        mnt = seconds // 60
        sec = seconds % 60
    elif 3600 <= seconds < 86400:
        hour = seconds // 3600
        mnt = (seconds % 3600)// 60
        sec = (seconds % 3600)% 60
    elif 86400 <= seconds < 31536000:
        day = seconds // 86400
        hour = (seconds % 86400)//3600
        mnt = ((seconds % 86400)%3600)//60
        sec = ((seconds % 86400)%3600)%60
    elif seconds >= 31536000:
        year = seconds // 31536000
        day = (seconds % 31536000)//86400
        hour = ((seconds % 31536000)%86400)//3600
        mnt = (((seconds % 31536000)%86400)%3600)//60
        sec = (((seconds % 31536000)%86400)%3600)%60  
    if seconds > 0:
        secon = str(sec) + ' seconds'
        if sec == 1:
            secon = str(sec) + ' second'
        if seconds >= 60:
            minut = str(mnt) + ' minutes' 
            if mnt == 1:
                minut = str(mnt) + ' minute' 
            if seconds >= 3600:
                hours = str(hour) + ' hours'
                if hour == 1:
                    hours = str(hour) + ' hour'
                if seconds >= 86400:
                    days = str(day) + ' days'
                    if day == 1:
                        days = str(day) + ' day'       
                    if seconds >= 31536000:
                        years = str(year) + ' years'
                        if year == 1:
                            years = str(year) + ' year'
    if seconds >= 60:
        if sec == 0:
            secon = ''
    if seconds >= 3600:
        if mnt == 0:
            minut = ''
        if seconds >=86400:
            if hour == 0:
                hours = ''
            if seconds >= 31536000:
                if day == 0:
                    days = ''
    if seconds >= 31536000:
        if secon !='':
            return years + ', '+ days + ', '+ hours + ', '+ minut + ' and ' + secon
        else:
            return years + ', '+ days + ', '+ hours + ' and ' + minut  + secon
    elif 31536000 > seconds >= 86400:
        if (secon =='') and (minut =='') and (hours ==''):
            return days
        elif (secon =='') and (minut ==''):
            return days + ' and ' + hours


        else:
            return days +', '+ hours +', '+ minut +' and ' + secon
    elif 86400 > seconds >= 3600:
        if (secon =='') and (minut ==''):
            return hours 
        elif secon == '':
            return hours + ' and ' + minut + secon
        else:
            return hours + ', ' + minut + ' and ' + secon
    elif 3600 > seconds >= 60:
        if secon !='':
            return minut + ' and ' + secon
        else:
            return minut + secon
    elif seconds < 60:
        return secon

print(format_duration(130975323))
