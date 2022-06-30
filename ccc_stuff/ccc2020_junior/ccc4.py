def cyclicshifts(t,s):
    word = s

    for i in range(0,len(s)):    
        if word in t:
            return "yes"
        word = s[1+i:] + s[:1+i]
        
    return "no"

    


t = input()
s = input()

print(cyclicshifts(t,s))
