# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input().split()
m = input().split()
X = list(input().split())
A = set(input().split())
B = set(input().split())

happiness = 0
for e in X:
    if e in A:
        happiness += 1
    if e in B:
        happiness -= 1

print(happiness)
print("Hai")
