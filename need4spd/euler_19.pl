#!/usr/bin/perl

use DateTime;
use strict;
use warnings;

my $start_date = DateTime->new(
    year=>1901,
    month=>1,
    day=>1,
    
);

my $end_date = DateTime->new(
    year=>2000,
    month=>12,
    day=>31,
    
);

my $count_of_sunday = 0;

while (1) {
    if(DateTime->compare($start_date, $end_date) == 0) {
        last;
    }
    
    if ($start_date->day == 1 and $start_date->day_of_week == 7) {
        $count_of_sunday+=1;
        print "$start_date";
    }
    
    $start_date->add(days=>1);
}

print "$count_of_sunday";
