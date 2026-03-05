a = 'on'
b = 'no'

if len(a)!=len(b):
    print("False")
else:

    freq1 = {}
    freq2 = {}
    for ch in a :
        if ch in freq1:
            freq1[ch] +=1
        else:
            freq1[ch] = 1
        
    for ch in b:
        if ch in freq2:
            freq2[ch]+=1
        else:
            freq2[ch] = 1

    if freq1==freq2:
        print("yes")
    else:
        print("no")
    