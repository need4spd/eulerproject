map={1=>"one",
2=>"two",
3=>"three",
4=>"four",
5=>"five",
6=>"six",
7=>"seven",
8=>"eight",
9=>"nine",
10=>"ten",
11=>"eleven",
12=>"twelve",
13=>"thirteen",
14=>"fourteen",
15=>"fifteen",
16=>"sixteen",
17=>"seventeen",
18=>"eighteen",
19=>"nineteen",
20=>"twenty",
30=>"thirty",
40=>"forty",
50=>"fifty",
60=>"sixty",
70=>"seventy",
80=>"eighty",
90=>"ninety",
}

sumofwordlen=0

(1..1000).each do |x|
	if x > 0 and x <= 20
		sumofwordlen+=map[x].length
	elsif x > 20 and x <= 99
		t=x.to_s[0,1]
		o=x.to_s[1,2]
		key=t+"0"
		
		temp1=map[key.to_i]
		temp2=map[o.to_i]
		
		sumoflen = 0
		
		if o.to_i == 0
			sumoflen=temp1.length
			sumofwordlen+=sumoflen
		else
			sumoflen = temp1.length + temp2.length
			sumofwordlen+=sumoflen
			
			map[x]=temp1+temp2
		end
	elsif x > 99 and x < 1000
		h=x.to_s[0,1]
		t=x.to_s[1,3]
		
		temp1=map[h.to_i]
		temp2="hundred"
		temp3=map[t.to_i]
		
		sumoflen=0
		
		if t.to_i == 0
			sumoflen = temp1.length + temp2.length
			sumofwordlen+=sumoflen
		elsif
			temp2+="and"
			sumoflen = temp1.length + temp2.length + temp3.length
			sumofwordlen+=sumoflen
		end
	else
		sumofwordlen+="onethousand".length
	end
end

puts sumofwordlen