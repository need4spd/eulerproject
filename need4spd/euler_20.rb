a=(1..100).inject(:*)
l=a.to_s.split(//)
 
r = l.inject{|sum,x| sum.to_i + x.to_i}
 
p r