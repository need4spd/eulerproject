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
30:"thrty",
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
	elif 20 < x < 100:
		t=str(x)[0:1] #십의자리
		o=str(x)[1:2] #일의자리
		key=t+"0" #key
		
		print(t, o, key)
		
		temp1=map.get(int(key))
		temp2=map.get(int(o))
		
		print(temp1, temp2)
		
		if int(o) == 0:
			sumofwordlen+=len(temp1)
			
		else:
			sumofwordlen+=len(temp1)
			sumofwordlen+=len(temp2)
			
			#이걸 다시 map에 넣는다
			map[x]=temp1+temp2
		
		
	elif 100 < x < 1000:
		h=str(x)[0:1] #백의자리
		t=str(x)[1:3] #뒤의두자리
		
		print(x, h, t)
		
		temp1=map.get(int(h))
		temp2="hundredand"
		temp3=map.get(int(t))
		
		print(temp1, temp2, temp3)
		
		if int(t) == 0:
			sumofwordlen+=len(temp1)
			sumofwordlen+=len(temp2)
		else:
			sumofwordlen+=len(temp1)
			sumofwordlen+=len(temp2)
			sumofwordlen+=len(temp3)
	else :
		sumofwordlen+=len("onethousand")

print(sumofwordlen)
		