require 'date'

startDate=Date.new(1901,1,1)
endDate=Date.new(2000,12,31)

countOfSunday = 0

while (true)
    if (startDate === endDate)
        break;
    end
    
    if startDate.wday == 0 and startDate.mday == 1: #일요일이고 1일
        countOfSunday+=1
        puts startDate
    end
    
    startDate = startDate + 1 #하루 증가
end    
        
puts countOfSunday