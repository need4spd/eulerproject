def numberOfPrimeFactors(num)
	if num==1
		return 1
	end
	
	startnum=2
	exponentDict=Hash.new(0)
	
	quota=0
	rest=0
	
	while true
		quota=num/startnum
		rest=num%startnum
		
		if rest==0
		
			if exponentDict.has_key?(startnum)
				exponentDict[startnum] = exponentDict[startnum] + 1
			else
				exponentDict[startnum] = 1
			end
			
			startnum=2
			num=quota
		else
			startnum+=1
		end
		
		if quota==1 and rest==0
			break
		end
	end
	
	r=1
	exponentDict.each_value {|value| r = r * (value + 1)}
	
	return r
end

start = Time.new

i=1
result=0
while true
	result+=i
	i+=1
	
	numberOfPrime=numberOfPrimeFactors(result)
	
	if numberOfPrime >= 500
		puts result
		break
	end
end

puts Time.now.to_f - start.to_f