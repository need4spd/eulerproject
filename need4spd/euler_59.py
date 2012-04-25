# ascii - a(97) to z(122)

cipher = open("cipher1.txt", "rb")
 
 
cipherlist = []
tmp = cipher.read()
for num in tmp.split(','):
	cipherlist.append(int(num))
	
