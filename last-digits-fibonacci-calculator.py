# Python code to find last m
# digits of n-th Fibonacci number

def findPisanoPeriod(m):
    a = 0
    b = 1
    c = a + b
    for i in range(m * m):
        c = (a + b) % m
        a = b
        b = c
        if a == 0 and b == 1:
            return i + 1


# populating the list
def preComputedList(f, m, p):
    # 0th and 1st number of a fibonacci series are 0 and 1
    f.append(0)
    f.append(1)

    # we add the last 2 numbers in the series and store the last m digits
    # we perform a mod m as we just care about the last m digits
    for i in range(2, p):
        f.append((f[i - 1] + f[i - 2]) % m)


# Returns the last m digits of fibonacci sequence of a provided number
# the last m digits of a fibonacci sequence repeat every pisano period, hence we mod pisano period
def findLastDigit(f, n, p):
    return f[n % p]


# create a list
precomputed_list = list()

# input the last x number of digits to find in fibonacci sequence
number_of_last_digits = input("Input the number of trailing digits to find: ")

# find the pisano period
pisano_period = findPisanoPeriod(int(10 ** int(number_of_last_digits)))

# compute the list and populate it
preComputedList(precomputed_list, 10 ** int(number_of_last_digits), pisano_period)

# input a number to find the fibonacci sequence of
fibonacci_number = input("Enter a number to find the fibonacci sequence of{F(n}: ")

print("Last " + number_of_last_digits + " digits of fibonacci(" + fibonacci_number + ") = " +
      str(findLastDigit(precomputed_list, int(fibonacci_number), pisano_period)).zfill(int(number_of_last_digits)))


