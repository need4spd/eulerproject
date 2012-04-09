def fact(n)
  if n<= 1
    1
  else
    n * fact( n - 1 )
  end
end

def get_number_of_cases(n, r)
  r = fact(n) / (fact(r) * fact(n-r))
end

cnt = 0
(23..100).each do |n|
  (1..n-1).each do |r|
    if get_number_of_cases(n, r) > 1000000
      cnt += 1
    end
  end
end

puts cnt
