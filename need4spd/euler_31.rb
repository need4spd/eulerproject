n=0

(0..200).each do |p1|
  (0..100).each do |p2|
    if (p1 + 2*p2) % 5 != 0
      next
    end
    (0..40).each do |p5|
      (0..20).each do |p10|
        (0..10).each do |p20|
          if (p1 + 2*p2 + 5*p5 + 10*p10 + 20*p20) % 50 != 0
            next
          end
          (0..4).each do |p50|
            (0..2).each do |p100|
              (0..1).each do |p200|
                if (p1 + 2*p2 + 5*p5 + 10*p10 + 20*p20 + 50*p50 + 100*p100 + 200*p200) == 200
                  n+=1
                end
              end
            end
          end
        end
      end
    end
  end
end

puts n
