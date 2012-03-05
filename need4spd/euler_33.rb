#10n + i / 10i + d = n/d
#9nd = 10in - di
#i = remove num, d=bunmo, n=bunja
# 0 < i < 10

multi_of_d=1
multi_of_n=1

(1..9).each do
  |i|
    (1..9).each do
      |n|
        (n+1..9).each do
          |d|
            if (9*n*d == ((10*i*n)-(i*d)))
              t=10*i+d
              t2=10*n+i
              puts "n : #{n}, d : #{d}, i : #{i}"
              
              multi_of_d = multi_of_d * t
              multi_of_n = multi_of_n * t2
            end
        end
    end
end

puts "#{multi_of_d}, #{multi_of_n}, #{multi_of_d/multi_of_n}"
