use strict;
use warnings;

sub primefactors {
     
    my $num = shift @_;
     
    my $start_num = 2;
    my @prime_numbers = ();
     
    my $quota = 0;
    my $rest = 0;
     
    while (1) {
        $quota = $num / $start_num;
        $rest = $num % $start_num;
         
        if ($rest == 0) {
            unless (grep(/^$start_num$/, @prime_numbers)) {
                push @prime_numbers, $start_num;
            }
            
            ($start_num, $num) = (2, $quota);
        } else {
            $start_num+=1;
        }
         
        if ($quota == 1 and $rest == 0) {
            last;
        }
    }
     
    @prime_numbers;
}

my $n = 2;
my $cnt_of_continue = 0;

while(1) {
    my @prime_factors = primefactors($n);
    
    if (scalar @prime_factors == 4) {
        $cnt_of_continue += 1;
    } else {
        $cnt_of_continue = 0;
    }
    
    if ($cnt_of_continue == 4) {
        print $n-3;
        last;
    }
    
    $n += 1;
}