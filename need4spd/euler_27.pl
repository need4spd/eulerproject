use strict;
use warnings;

sub isPrime
{
    my ($number) = @_;
    $number = abs $number;
    
    my $sqrt = sqrt $number;
    my $d = 2;
    while (1)
    {
        return 0 if ( $number % $d == 0 );
        return 1 if ( $d > $sqrt );
        $d++;
    }
}

my $max_a = 0;
my $max_n = 0;
my $max_b = 0;

foreach my $a ((-999..999)) {
    foreach my $b ((-999..999)) {
        my $n = 0;
        
        while(1) {
            my $r = ($n**2) + ($n*$a) + $b;
            
            if(isPrime($r)) {
                $n+=1;
            } else {
                last;
            }
        }
        
        if( $n > $max_n) {
            print "a : $a, b : $b, n : $n \n";
            $max_n = $n;
            $max_a = $a;
            $max_b = $b;
        }
    }
}

print "{($max_a*$max_b)}";