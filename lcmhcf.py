def gcd(num1,num2):
    if num2==0:
        return num1
    else:
        return gcd(num2,num1 % num2)
def main():
    print "enter 2 integers"
    num1=int(raw_input())
    num2=int(raw_input())
    hcf=gcd(num1,num2)
    lcm=(num1*num2)/hcf
    print hcf
    print lcm
main()
