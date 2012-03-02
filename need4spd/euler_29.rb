require 'set'

r=Set.new

(2..100).each do |a|
  (2..100).each do |b|
    r.add(a**b)
  end
end

puts r.length