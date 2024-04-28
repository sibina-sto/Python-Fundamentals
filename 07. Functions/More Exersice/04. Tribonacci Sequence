# 04-03. FUNCTIONS [More Exercises]
# 04. Tribonacci Sequence

def tribonacci(num):
    prev1 = 0
    prev2 = 0
    prev3 = 0

    for i in range(num):
        tribonacci_sum = prev1 + prev2 + prev3
        if tribonacci_sum == 0:
            tribonacci_sum = 1
        print(tribonacci_sum, end=' ')
        prev1 = prev2
        prev2 = prev3
        prev3 = tribonacci_sum


tribonacci(int(input()))
