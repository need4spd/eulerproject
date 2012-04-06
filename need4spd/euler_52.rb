def is_permutations(a,b)
  s_a = a.to_s.split(//).sort()
  s_b = b.to_s.split(//).sort()
   
  if s_a == s_b
    return true
  else
    return false
  end
end

n = 125874
while (true)
   
  if is_permutations(n, n*2) and is_permutations(n, n*3) and is_permutations(n, n*4) and is_permutations(n, n*5) and is_permutations(n, n*6)
      puts n 
  end
  
   n = n + 1

end
