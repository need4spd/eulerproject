def trig(n)
	return ((n+1) * n) / 2
end

def count_div(n)
	lim = Math.sqrt(n).to_i
	ret = 2
	ret = 4 if n & 1 == 0 
	
	3.upto(lim-1) do |i|
		ret = ret + 2 if n.modulo(i) == 0		
	end
	
	ret = ret.next if n.modulo(lim) == 0
	ret
end

cur = 10000
while true
	break if count_div(trig(cur)) > 500
	cur = cur.next
end

puts cur, trig(cur)
