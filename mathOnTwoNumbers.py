def mathOfTwo(o,a,b):
    if o.upper() == "A":
        return(int(a)+int(b))
    elif o.upper() == "S":
        return(int(a)-int(b))
    elif o.upper() == "M":
        return(int(a)*int(b))
    elif o.upper() == "D":
        return (int(a)/int(b))
    else:
        return(0)