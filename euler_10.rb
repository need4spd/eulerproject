def isPrime(n)
	if n==2
		return true
	elsif n%2==0
		return false
	end
	
	i=3
	
	range=Math.sqrt(n).to_i()+1
	
	while i<range
		if n%i==0
			return false
		end
		
		i+=1
	end
	
	return true
end

num=2
sumOfPrime=0

while true
	if isPrime(num)
		sumOfPrime+=num
	end
	
	num+=1
	
	if num==2000000
		break
	end
end

puts sumOfPrime