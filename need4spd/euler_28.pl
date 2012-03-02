use strict;
use warnings;

my $sum=1;
my $rows=1001;

foreach my $n ((3..1001)) {
    if($n % 2 ==0) {
        next;
    }
    
    my $up_r = $n * $n;
    my $up_l = $up_r - ($n-1);
    my $dn_l = $up_l - ($n-1);
    my $dn_r = $dn_l - ($n-1);
    
    print "$up_r, $up_l, $dn_l, $dn_r \n";
    $sum = $sum + $up_r + $up_l + $dn_l + $dn_r;
}

print $sum;