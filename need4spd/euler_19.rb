startDate=Time.gm(1901,"jan",1)
endDate=(2000,"dec",31)

plusDate = (60 * 60 * 24)

countOfSunday = 0

while True:
    if startDate == endDate:
        break;
    
    if startDate.weekday() == 6 and startDate.day == 1: #일요일이고 1일
        countOfSunday+=1
        print (startDate)
    
    startDate = startDate + plusDay #하루 증가
    
        
print (countOfSunday)