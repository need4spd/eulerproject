def isPrimeNumber(num)
	t=2
	while t<=num
		rest=num%t
		if rest==0 and t==num
			return true
		elsif rest==0 and t!=num
			return false
		else
			t=t+1
		end
	end
	
	return false
end

def getPrimeNumber(offset)
	numOfPrime=0
	targetNum=2
	
	while true
		r=isPrimeNumber(targetNum)
		if r
			numOfPrime+=1
			
			if numOfPrime == offset
				return targetNum
			end
		end
		
		targetNum+=1
	
	end
	
	return targetNum
end

r=getPrimeNumber(10001)
puts r