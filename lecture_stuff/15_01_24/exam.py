# def foo(a,b):
#     if a>b:
#         return a+b
#     elif a ==b:
#         return a*b
#     else:
#         return a-b
# print(foo(5,foo(5,5)))

# def bar(x):
#     if x%2==0:
#         return x//2
#     else:
#         return x*3+1
    
# n =10
# while n!= 1:
#     n=bar(n)
#     print(n,end=" ")

x = 0
y = 10
if x or y:
    x+=1
    if not x or y:
        x+=1
    else:x+=2
else:
    x+=3
print(x)