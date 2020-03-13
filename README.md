# last-digits-of-fibonacci


If one needs to calculate the last digits of a fibonacci number, One can calculate the fibonacci number and then take the last digits. However this gets infeasabile 
very quickly. 

However, The fibonacci sequence follows a pattern when it comes to the last digits. The last digit repeats every 60 numbers, the last 2 digits repeats every 300 numbers, the last 3 
digits repeats every 1500 numbers and so on [Source: https://mathworld.wolfram.com/FibonacciNumber.html].

We can codify this with a program. We can precompute the list and look up the last digits of the number we are interested in. 

To run the code, 
1. Install python3
2. Run ``` python3 last-digits-fibonacci-calculator.py ```
3. Enter the number you wish to compute the digits of
