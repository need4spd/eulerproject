def isPandigital(n):
  if (len(n) == 9):
    temp_l = ''.join(sorted([ c for c in n]))
    if temp_1 = '123456789':
      return True;
  return False
  
  
  - 9 X (1,2) => too few digits
- 98 X (1,2) => too few digits (98196)
- 987 X (1,2) => too few digits (98196294)
- 9876 X (1,2) => 9 digits (987619752) !
- 9183 X (1,2) => 9 digits (918318366) !

918273645 is not the greatest. So for a 4-digits number M, the maximum is between 9183... and 9876...

for n = 3:

- 98 X (1,2,3) => 8 digits (98196294)
- 987 X (1,2,3) => 11 digits (98719742961)
- 919 X (1,2,3) => 11 digits (91918382757)

for n = 3, when we try with the minimal number M = 919 to give a pandigital number just after 918273645, we end up with 11 digits.

So M is clearly between 9183 and 9876, and n = 2.

final long time = currentTimeMillis();
for (int n = 9876; n >= 9183; n--) {
// equivalent to 100000*n + 2*n to create the concatenation of the pandigital number
final int number = (n << 5) * 3125 + (n << 1);
if (n % 5 != 0 && Maths.isPandigital(number, 10)) {
System.out.println(number);
}
}
out.println(" in " + (currentTimeMillis() - time) + "ms");