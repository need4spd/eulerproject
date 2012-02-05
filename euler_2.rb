def fib_up_to(max)
  i1=1
  i2=1
  while i1<=max
    yield i1
    #i1, i2 = i2, i1+i2
    temp=i1
    i1=i2
    i2=temp+i2
  end
end

fibList=Array.new
fib_up_to(4000000) do
  |f1| 
  #print f1, " "
  if f1%2 == 0 
    fibList.push(f1)
  end
end

result=0
fibList.each{|num| result=result+num}
puts result

