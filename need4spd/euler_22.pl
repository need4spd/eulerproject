use strict;
use warnings;
use List::MoreUtils qw(first_index);

open PRB, "names.txt";

my $names_str;
while(defined(my $line=<PRB>)) {
    chomp($line);
    $names_str = $line;
}

$names_str =~ s/\"//g;

my @names_list=split /,/, $names_str;
@names_list = sort @names_list;

my @alpha_list=('A'..'Z');

my $index=0;
my $total_score=0;

foreach my $name (@names_list) {
    $index = first_index {$_ eq $name} @names_list;
    $index = $index + 1; #곱하기를 위함
    
    #이름 자체의 점수를 계산
    my $char_score_sum = 0;
    foreach my $byte (split //, $name) {
        my $char_score = first_index {$_ eq $byte} @alpha_list;
        print "byte : $byte , char_score : $char_score \n";        
        $char_score_sum = $char_score_sum + $char_score + 1;
    }
    
    print "name : $name, index : $index, $char_score_sum : $char_score_sum \n";
    #총 점수의 합
    $total_score = $total_score + ($char_score_sum * $index);
}

print "total_score : $total_score";