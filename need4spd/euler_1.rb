numbers=(1..999)
result=0
numbers.each do |number|
  if number%3 == 0 or number%5 == 0
    result = result + number
   # print number
  end
end

puts result

