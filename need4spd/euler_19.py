from datetime import datetime, timedelta

startDate = datetime(1901,1,1)
endDate = datetime(2000,12,31)

plusDay = timedelta(days=1)

countOfSunday = 0
while True:
    if startDate == endDate:
        break;
    
    if startDate.weekday() == 6 and startDate.day == 1: #일요일이고 1일
        countOfSunday+=1
        print (startDate)
    
    startDate = startDate + plusDay #하루 증가
    
        
print (countOfSunday)