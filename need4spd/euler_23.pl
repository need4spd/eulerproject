use strict;
use warnings;
use Math::Complex;
use List::Util qw (sum);

sub getDivisors {
    my ($num) = @_;
    my %divisors_hash=(); #키가 약수
    
    my $l=sqrt($num)+1;
    foreach my $n ((1..$l)) {
        if ($num % $n == 0) {
            unless(exists ($divisors_hash{$num / $n})) {
                $divisors_hash{$num / $n}=1;
            }
            
            unless(exists ($divisors_hash{$n})) {
                $divisors_hash{$n}=1;
            }
        }
    }
    #print "num : $num, divisors : @{keys %divisors_hash} \n";
    
    my @divisors=();
    foreach my $key ( keys %divisors_hash ) {
        unless ($key == $num) {
            push @divisors, $key;
        }
    }
    
    print "num : $num, divisors : @divisors \n";
    return @divisors;
}

sub isAbundant {
    my ($num) = @_;
    my @divisors = getDivisors($num);
    my $total = sum @divisors;
    
    if ($total > $num) {
        #print "num : $num, total : $total \n";
        return 1;
    } else {
        return 0;
    }
}   
    
my $limit = 28123;
my @abundantList=();

foreach (12..$limit-1) {
    if (isAbundant($_)) {
        push @abundantList, $_;
    }
}

#print "a : @abundantList";
my %sumOfAbundant=();

foreach my $i (@abundantList) {
    foreach my $j (@abundantList) {
        my $t=$i+$j;
        if ($t < $limit and (!exists ($sumOfAbundant{$t}))) {
            $sumOfAbundant{$t}=1;
        }
    }
}

#print "sum_of_abundant : @{keys %sumOfAbundant}";

my $result = 0;
foreach (keys %sumOfAbundant) {
   $result += $_; 
}

$result = sum (1..$limit-1) - $result;
print"total : $result";