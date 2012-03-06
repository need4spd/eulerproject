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

sub get_circular_list {
    my ($n) = @_;
    my @n_list = split //, $n;
    
    my @result_list=();
    my $loop_cnt = length $n - 1;
    
    push @result_list, $n;
    
    while ($loop_cnt > 0) {
        my $t = pop @n_list;
        unshift @n_list, $t;
        
        my $st = join(@n_list, "");
        push @result_list, $st;
        $loop_cnt -= 1;
    }
    
    return @result_list;
}

my @r_list = ();
foreach my $n ((0..999999)) {
    if ($n != 2 and $n =~ m/2/) {
        next;
    }
    
    if ($n =~ m/0/) {
        next;
    }
    
    my @c_list = get_circular_list($n);
    my $all_prime = 1;
    
    foreach my $c (@c_list) {
        unless (isPrime($c)) {
            $all_prime = 0;
            last;
        }
    }
    
    if ($all_prime) {
        push @r_list, $n;
    }
}

my $r = @r_list;
print "$r";