r=Hash.new()

(1..1000).each do |a|
  (1..1000).each do |b|
    (1..1000).each do |c|
      
      if (a+b+c > 1000)
        break
      end
      
      temp = a**2 + b**2
      
      if (c**2 == temp)
        p=a+b+c
        
        if (r.has_key? p)
          r[p] = r[p]+1
        else
          r[p] = 1
        end
      end
    end
  end
end

#sorted_r = r.sort {|a, b| a[1] <=> b[1]}
#puts sorted_r

#puts "###################"

sorted_r = r.sort {|a, b| -(a[1] <=> b[1])}
puts sorted_r

