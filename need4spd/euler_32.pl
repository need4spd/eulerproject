use strict;
use warnings;
use Math::Complex;
 
sub getDivisors {
    my ($num) = @_;
    my %divisors_hash=(); #키가 약수
     
    my $l=sqrt($num)+1;
    foreach my $n ((1..$l)) {
        if ($num % $n == 0) {
            unless(exists ($divisors_hash{$num / $n})) {
                $divisors_hash{$num / $n}=1;
            }
             
            unless(exists ($divisors_hash{$n})) {
                $divisors_hash{$n}=1;
            }
        }
    }
    #print "num : $num, divisors : @{keys %divisors_hash} \n";
     
    my @divisors=();
    foreach my $key ( keys %divisors_hash ) {
        push @divisors, $key;
    }
    
    sort {$a <=> $b} @divisors;
}
 

my $r=0;
foreach my $n ((2..100000)) {
    if ($n =~ m/0/) {
        next;
    }
    
    my @l = getDivisors($n);
    
    print "n : $n, @l \n";
    
    my $end_offset = @l - 1;
    my $start_offset = 0;
    
    while ($start_offset != $end_offset and $start_offset <= $end_offset) {
        my $a=$l[$start_offset];
        my $b=$l[$end_offset];
        
        $start_offset+=1;
        $end_offset-=1;
        
        if ($a =~ m/0/ or $b =~ m/0/) {
            next;
        }
        
        my $joined_n = $a.$b.$n;
        
        #print "joined_n : $joined_n";
        
        if (length $joined_n == 9) {
            my @temp_l = split //, $joined_n;
            @temp_l = sort @temp_l;
            
            my $temp_s = join("", @temp_l);
            if ($temp_s =~ m/123456789/) {
                $r+=$n;
                
                print "$a, $b, $n \n";
                
                last;
            }
        }
    }
}

print "$r \n";