use strict;
use warnings;
use List::Util qw(first sum);

sub getDivisors {
    
    my ($num) = @_;
    
    my @divisors=();
    my $start_num=1;
    
    if ($num == 1) {
        push @divisors, 1;
        return @divisors;
    }
    
    while(1) {
        if ($num % $start_num == 0) {
            push @divisors, $start_num;
        }
        
        $start_num+=1;
        
        if ($num == $start_num) {
            last;
        }
    }
    
    return @divisors;
}

my $target_num=10000;
my @result_list=();

while(1) {
    if(defined(first { $_ eq $target_num} @result_list)) {
        $target_num-=1;
        next;
    }
    
    print $target_num."\n";
    
    my @divisors=getDivisors($target_num);
    my $sum_of_divisors=sum @divisors;
    
    print "divisors=@divisors, sum_of_divisors=$sum_of_divisors \n";
    
    my @temp_divisors=getDivisors($sum_of_divisors);
    my $temp_sum_of_divisors=sum @temp_divisors;
    
    if ($target_num == $temp_sum_of_divisors and $target_num != $sum_of_divisors) {
        print "in result list";
        
        push @result_list, $target_num;
        push @result_list, $sum_of_divisors;
    }
    
    $target_num-=1;
    
    if ($target_num == 0) {
        last;
    }
}

print "@result_list";
my $r=sum @result_list;
print $r