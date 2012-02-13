"""
My solution uses a top down approach. For example for 1x1 grid, we can reach the corner from its neighboring nodes in 1 way.

2----1
|      |
1----0

So to reach it from the top left corner we have 2 ways.

now suppose a 2x1 grid

3----1
|      |
2----1
|      |
1----0

We can reach the bottom right corner, from the top left corner, by either taking the "down" route which has 2 ways, or the "right" way which has 1 way. 

So for any NxM grid construct a N+1 x M+1 matrix. Mark

matrix[N]=1
matrix[M]=1

Assuming indexing starts from 0.

The values for the rest of the cells can be evaluated by:

matrix[j]=matrix[i+1][j] + matrix[j+1]

where i=N-1 to 0 and j=M-1 to 0.
"""

l=[]
for i in range(21):
       l.append([])
       for j in range(21):
              l[i].append(0)
              
for i in range(21):
       l[20][i]=1
       l[i][20]=1
       
for i in range(19,-1,-1):
       for j in range(19,-1,-1):
              l[i][j]=l[i+1][j]+l[i][j+1]
              
print(l[0][0])