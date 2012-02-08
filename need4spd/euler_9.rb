n=1
m=1

while true
	r=m**2 + m*n
	
	if r==500
		puts m,n
		break
	end
	
	m+=1
	
	if m==500
		n+=1
		m=n+1
	end
end

a=m**2 - n**2
b=2*m*n
c=m**2 + n**2

puts a*b*c