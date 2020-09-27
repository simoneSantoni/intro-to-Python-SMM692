

Whereas a for loop is established for a fixed number of iterations, statements within the block of a while loop execute only and as long as some condition holds: >>> i = 0 >>> while i<10: ... i += 1 ...
print(i, end=’.’)
... >>> print()
1.2.3.4.5.6.7.8.9.10.
The counter i is initialized to 0,whichis lessthan10 so the while loop begins. On each iteration, i is incremented by one and its value printed. When i reaches 10,onthe following iteration i < 10 is False:the loop ends and execution continues afterthe loop,
