def a(num)
	r=num/2
	return r.to_i()
end

def b(num)
	return (3*num) + 1
end

targetnum=1000000
loopCnt=1

biggestLoopCnt=0
biggestLoopCntNum=0

r=targetnum

while true
	if r%2 == 0
		r=a(r)
	else
		r=b(r)
	end
	
	loopCnt+=1
	
	if r==1
		if biggestLoopCnt < loopCnt
			biggestLoopCnt = loopCnt
			biggestLoopCntNum = targetnum
		end
		
		loopCnt=1
		targetnum-=1
		r=targetnum
	end
	
	if targetnum==1:
		break
	end
end

puts "big" + biggestLoopCntNum.to_s