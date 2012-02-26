use List::Permutor;

use strict;
use warnings;

my $perm = new List::Permutor qw /0 1 2 3 4 5 6 7 8 9/;
my $count = 0;
while (my @set = $perm->next) {
    $count+=1;
    print "count = $count \n";
    if($count == 999999) {
        print "@set";
        last;
    }
}