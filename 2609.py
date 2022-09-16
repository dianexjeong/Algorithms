x, y=map(int, input().split())

# 최대공약수 - 유클리트 호제법
def gcd(a, b):
    while (True):
        a, b=b, a%b
        if (b==0):
            return a
        


# 최소공배수
def lcm(a, b):
    return a*b//gcd(a, b)

print(gcd(x, y))
print(lcm(x, y))
