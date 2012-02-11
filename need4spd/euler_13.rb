numlist=[]
File.open("euler_13_problem.txt") do |file|
	while line=file.gets
		numlist.push(line)
	end
end

sum=0
numlist.each do |num|
	sum+=num.to_i
end

puts sum.to_s.slice(0, 10)