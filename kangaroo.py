def kangaroo(x1, v1, x2, v2):
    if v1-v2==0:
        return "NO"
    result=(x2-x1)/(v1-v2)
    if result<0:
        return "NO"
    if result.is_integer():
        return "YES"
    else:
        return "NO"
