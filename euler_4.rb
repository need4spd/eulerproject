def myReverse(targetNum)
  
  numList=Array.new()
  targetNumStr=targetNum.to_s()
    
  return targetNumStr.reverse().to_i()
end

def isSymmetryNum(targetNum)
  reversedNum=myReverse(targetNum) 
  return reversedNum == targetNum
    
end

n1=Array.new(999) {|x| x+1}
n2=Array.new(999) {|x| x+1}

biggestNum=0

for i in n1 
  for j in n2
   r=i*j
   if isSymmetryNum(r) and biggestNum < r
     biggestNum=r
   end
 end
end

puts biggestNum

