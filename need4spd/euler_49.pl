use strict;
use warnings;

sub is_prime_number {
    my($num) = @_;
      
    my $t=2;
      
    while ($t <= $num) {
        my $rest = $num % $t;
          
        if ($rest==0 and $t==$num) {
            return 1;
        } elsif ($rest == 0 and $t != $num) {
            return 0;
        } else {
            $t+=1;
        }
          
    }
      
    0;
}


sub is_permutations {
    my ($a, $b, $c) = @_;
    
    #print "$a, $b, $c \n";
    my @s_a = split //, $a;
    @s_a = sort @s_a;
    my $a_str = join "", @s_a;
    
    my @s_b = split //, $b;
    @s_b = sort @s_b;
    my $b_str = join "", @s_b;
    
    my @s_c = split //, $c;
    @s_c = sort @s_c;
    my $c_str = join "", @s_c;
    
    #print "@s_a, @s_b, @s_c \n";
    if ($a_str == $b_str && $b_str == $c_str) {
        return 1;
    } else {
        return 0;
    }
}

my @prime_list;
foreach my $n ((1000..9999)) {
    if (is_prime_number($n)) {
        push @prime_list, $n;
    }
}
@prime_list = sort @prime_list;

foreach my $a (@prime_list) {
    foreach my $b (@prime_list) {
        foreach my $c (@prime_list) {
            if (($b-$a == $c-$b) && !($b-$a == 0)) {
                if (is_permutations($a, $b, $c)) {
                    print "$a, $b, $c \n";
                    last;
                }
            }
        }
    }
}