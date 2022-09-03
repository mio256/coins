d={
    10000:0,
    5000:0,
    1000:0,
    500:0,
    100:0,
    50:0,
    10:0,
    5:0,
    1:0,
}

a=int(input('jpy>'))

for k in d:
    while a>k:
        d[k]+=1
        a-=k

for k,v in d.items():
    print(k,v)