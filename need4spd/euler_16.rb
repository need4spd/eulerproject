a=2**1000
l=a.to_s.split(//)

r = l.inject{|sum,x| sum.to_i + x.to_i}

p r