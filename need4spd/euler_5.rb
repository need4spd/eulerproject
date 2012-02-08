numList=Array.new(20) {|x| x+1}

num=1

while true
  isSearch=true

  for i in numList
    r=num%i
    if r!=0 
      isSearch=false
      num+=1
      break
    end
  end

  if isSearch
    print(num)
    break
  end
end
 



