
sampleFile=open("euler_18_problem.txt", "r")

triangle=[]

for l in sampleFile.readlines():
    l=l.rstrip('\n')
    raw_list=l.split(" ")
    
    temp_l=list()
    for y in raw_list:
        temp_l.append(int(y))
    
    triangle.append(temp_l)
    
# reverse.
triangle.reverse();

# add each row to row+1 and replace row
for row in range(0,14):
    for col in range(0, 14-row):
        first_sum = triangle[row][col] + triangle[row+1][col]
        second_sum = triangle[row][col+1] + triangle[row+1][col]
        max_of_two = max(first_sum, second_sum)
        
        triangle[row+1][col] = max_of_two
        
    print("triangle : {0}".format(triangle[row+1]))
