require 'set'

t_n_set = Set.new
p_n_set = Set.new
h_n_set = Set.new

max_n = 100000
(1..max_n).each do |n|
  t_n_set.add(n*(n+1)/2)
  p_n_set.add(n*(3*n-1)/2)
  h_n_set.add(n*(2*n-1))
end

r = t_n_set & p_n_set & h_n_set

r.each { |n|
  puts n
}