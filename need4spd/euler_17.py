map={1:"one",
2:"two",
3:"three",
4:"four",
5:"five",
6:"six",
7:"seven",
8:"eight",
9:"nine",
10:"ten",
11:"eleven",
12:"twelve",
13:"thirteen",
14:"fourteen",
15:"fifteen",
16:"sixteen",
17:"seventeen",
18:"eighteen",
19:"nineteen",
20:"twenty",
30:"thirty",
40:"forty",
50:"fifty",
60:"sixty",
70:"seventy",
80:"eighty",
90:"ninety",
}

sumofwordlen=0

for x in range(1, 1001):
	
	if 0 < x <= 20:
		sumofwordlen+=len(map.get(x))
		
	elif 20 < x <= 99:
		t=str(x)[0:1] #십의자리
		o=str(x)[1:2] #일의자리
		key=t+"0" #key
		
		temp1=map.get(int(key))
		temp2=map.get(int(o))
		
		sumoflen=0
		
		if int(o) == 0:
			sumoflen = len(temp1)
			sumofwordlen+=sumoflen
			
		else:
			sumoflen = len(temp1) + len(temp2)
			sumofwordlen+=sumoflen
			
			#이걸 다시 map에 넣는다
			map[x]=temp1+temp2
		
	elif 99 < x < 1000:
		h=str(x)[0:1] #백의자리
		t=str(x)[1:3] #뒤의두자리
		
		temp1=map.get(int(h))
		temp2="hundred"
		temp3=map.get(int(t))
		
		sumoflen=0
		
		if int(t) == 0:
			sumoflen = len(temp1) + len(temp2)
			
			sumofwordlen+=sumoflen
		else:
			temp2+="and"
			sumoflen = len(temp1) + len(temp2) + len(temp3)
			
			sumofwordlen+=sumoflen
		
	else :
		sumofwordlen+=len("onethousand")

print(sumofwordlen)
		