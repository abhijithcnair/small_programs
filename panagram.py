def panagram(check):
    length=len(check)
    alp=list('abcdefghijklmnopqrstuvwxyz')
    c=0
    for i in alp:
        if i not in check:
            c=1
    if c==1:
        print "it is not panagram"
    else:
        print "it is a panagram"

def main():
    print "enter a string:"
    check=raw_input()
    panagram(check)

main()

    
    
