require 'mathn'
primes = Prime.new
10_000.times { primes.next }
puts "Prime is #{ primes.next }."