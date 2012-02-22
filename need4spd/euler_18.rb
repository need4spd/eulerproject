triangle=[]

File.open("euler_18_problem.txt") do |file|
  while line=file.gets
    puts line
    r=line.scan(/\S+/).collect {|n| n.to_i}
    triangle.push(r)
  end
end

triangle = triangle.reverse

(0..13).each do |row|
  (0..13-row).each do |col|
    first_sum = triangle[row][col] + triangle[row+1][col]
    second_sum = triangle[row][col+1] + triangle[row+1][col]
    max_of_two = [first_sum, second_sum].max
    
    triangle[row+1][col] = max_of_two
  end
  
  triangle[row+1].each {|r| print r, " "}
  puts "\n"
end