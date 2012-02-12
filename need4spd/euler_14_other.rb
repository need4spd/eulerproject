def chain(n)
	return 1 if n == 1
	n.even? ? chain(n/2)+1 : chain(3*n + 1)+1
end
p (1..1_000_000).map{ |n| [n, chain(n)] }.max{|a,b| a[1] <=> b[1]}