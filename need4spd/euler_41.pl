use List::Permutor;

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

our $result = 0;

sub getPrime {
    my ($number) = @_;
 
    while (my @p = $number->next) {
    my $str = join "", @p;
    if (isPrime($str)) {
        if($result < $str) {
            $result = $str;
        }
    }
}   
}

my $perm = new List::Permutor qw /1 2 3 4/;
&getPrime($perm);
$perm = new List::Permutor qw /1 2 3 4 5/;
&getPrime($perm);
$perm = new List::Permutor qw /1 2 3 4 5 6/;
&getPrime($perm);
$perm = new List::Permutor qw /1 2 3 4 5 6 7/;
&getPrime($perm);
$perm = new List::Permutor qw /1 2 3 4 5 6 7 8/;
&getPrime($perm);
$perm = new List::Permutor qw /1 2 3 4 5 6 7 8 9/;
&getPrime($perm);


print "$result";