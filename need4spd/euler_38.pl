sub isPandigital {
    my ($n) = @_;
    if (length $n == 9) {
        my @temp_l = split //, $n;
        @temp_l = sort @temp_l;
        
        my $temp_s = join("", @temp_l);
        if ($temp_s =~ m/123456789/) {
            return 1;
        }
    }
    
    return 0;
}

my $result = 0;

foreach my $n ((9183..9877)) {
    my $a1 = ($n*1).($n*2);
    
    if (isPandigital($a1)) {
        if ($result < $a1) {
            $result = $a1;
        }
    }
}

print "$result";