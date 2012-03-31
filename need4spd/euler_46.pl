use strict;
use warnings;
use Math::Complex;

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
 
sub get_prime_number {
    my($offset) = @_;
    my $target_num = 2;
    my $number_of_prime_num = 0;
    
    my @result_list=();
    while (1) {
        my $r = is_prime_number($target_num);
         
        if ($r) {
            $number_of_prime_num+=1;
            push @result_list, $target_num;
             
            if ($number_of_prime_num == $offset) {
                return @result_list;
            }
        }
         
        $target_num+=1;
    }
     
    return @result_list;
}


sub any {
    my(@p_list) = @_;
    
    foreach my $b (@p_list) {
        if ($b) {
            return 1;
        }
    }
    
    return 0;
}

my $x = 5;

while (1) {
    #print "123123213123";
    
    my @prime_list = &get_prime_number($x);
    
    #print "@prime_list, $x \n";
    my $tt=grep(/^$x$/, @prime_list);
    
    print "tt=$tt, x=$x \n";
    
    if (grep(/^$x$/, @prime_list)) {
        $x += 2;
        #print "next\n";
        next;
    }
    
    #print "d";
    my @temp_list = ();
    foreach my $n (1..sqrt($x)) {
        foreach my $p (@prime_list) {
            my $temp_x = $p + 2 * ($n**2);
            
            if ($temp_x > $x) {
                last;
            }
            
            if ($temp_x == $x) {
                push @temp_list, 1;
            } else {
                push @temp_list, 0;
            }
        }
    }
    
    if (!any(@temp_list)) {
        print "result=$x";
        last;
    }
    
        
    $x += 2;
    
    print "x=$x";
    
}