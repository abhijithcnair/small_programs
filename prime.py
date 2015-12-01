def test(value):
    i=2
    l1=[]
    l2=[]
    while(i<value):
        j=2
        while (j<=value):
            if i*j<value and i*j not in l1:
                l1.append(i*j)
            j=j+1
        i=i+1
    for j in range(2,value):
        if j not in l1:
            l2.append(j)
    print l1
def main():
    print "enter a value"
    value=int(raw_input())
    test(value)
main()



                
        
