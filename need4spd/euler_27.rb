require 'mathn'

def isPrime(n)
  return n.prime?
end

def getResult(a,b,n)
    r = n**2 + (a*n) + b
    
    return r
end

max_n = 0
max_a = 0
max_b = 0

(-999..999).each do
  |a|
  (-999..999).each do
    |b|
    n = 0
    
    while (true)
      if (isPrime(a+b+1) and isPrime(b))
        r = getResult(a,b,n)
        if (isPrime(r))
          n+=1
        else
          break
        end
      else
        break
      end
    end
    
    if (n > max_n)
      puts "a : #{a}, b : #{b}, n : #{n}"
      max_n = n
      max_a = a
      max_b = b
    end
    
  end
end
puts max_a*max_b