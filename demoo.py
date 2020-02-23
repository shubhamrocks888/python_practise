
def prime(n):
    l=[]

    for i in range(2,n+1):
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                break
        else:
            l.append(i)

            k = l.index(i)
            if l[k]+l[k]==n:
                return l[k],l[k]
            if k!=0:
                if l[k]+l[k-1]==n:
                    return l[k-1],l[k]

print(prime(2))
