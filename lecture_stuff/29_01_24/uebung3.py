defaultdict = __import__('collections').defaultdict
count = defaultdict(int)

def fibonacci_result(n):
    count[n] += 1
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 1:
        return fibonacci_result(n-1) +fibonacci_result(n-2)
    

n = int(input("Enter a number: "))
result = fibonacci_result(n)
print(result)
for key in count:
    print("fibonacci of",key,"is calles", count[key], "times")

