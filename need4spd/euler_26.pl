use strict;
use warnings;
use List::MoreUtils qw(first_index);

sub check_cycle {
    my ($d) = @_;
    my $n = 0;
    my @remain_list=();
    my $dividend = 1;
    
    while (1) {
        my $remain = $dividend % $d;
              
        my $index = first_index {$_ eq $remain} @remain_list;
        if ($index > -1) {
                    
            return $n - $index;
        } else {
            push @remain_list, $remain;
            $dividend = $remain * 10;
            $n+=1;
        }
    }
}

my $max_d = 0;
my $d = 2;
my $max_n = 0;

while ($d < 1000) {
    my $temp = check_cycle($d);
    if ($temp > $max_n) {
        $max_n = $temp;
        $max_d = $d;
    }
    
    $d+=1;
}

print "$max_d";