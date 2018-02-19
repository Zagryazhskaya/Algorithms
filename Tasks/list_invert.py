def invert(l):
    l = list(l)
    if len(l)>0:
        return invert(l[len(l)-1] )

invert("jinja")