use strict;
use warnings;

sub isPrime
{
    my ($number) = @_;
    $number = abs $number;
    
    if ($number == 1) {
        return 0;
    }
    
    my $sqrt = sqrt $number;
    my $d = 2;
    while (1)
    {
        return 0 if ( $number % $d == 0 );
        return 1 if ( $d > $sqrt );
        $d++;
    }
}

my $result_cnt=0;
my $result_sum=0;
my $n=9;

while ($result_cnt < 11) {
    my $all_prime = 1;
    my $n_len = length $n;
    
    my $temp = "";
    my $temp2 = "";
    
    foreach my $i ((0..$n_len-1)) {
        $temp2 = substr $n, $i, 1;
        $temp = $temp.$temp2;
        
        if (!isPrime($temp)) {
            $all_prime = 0;
            last;
        }
    }
    
    my $n_reverse = reverse $n;
    
    $temp = "";
    foreach my $i ((0..$n_len-1)) {
        $temp2 = substr $n_reverse, $i, 1;
        $temp = $temp2.$temp;
        
        if (!isPrime($temp)) {
            $all_prime=0;
            last
        }
    }
    
    if ($all_prime) {
        
        $result_cnt+=1;
        $result_sum+=$n;
    }
    $n+=1;
}

print "$result_sum";