
print((lambda a:lambda v:a(a,v))(lambda s,x:1 if x==0 else x*s(s,x-1))(2))