def sumofsquare(numberList)
	result=0
	numberList.each do |number|
		result=result+(number**2)
	end
	
	return result
end

def squareofsum(numberList)
	result=0
	numberList.each do |number|
		result=result+number
	end
	
	result=result**2
	
	return result
end


r=sumofsquare(Array(1..100))
r2=squareofsum(Array(1..100))

puts r
puts r2
puts r2-r