def func():
    a,*b,c=["Car","Dog","Tiger","Bird","Lion"]
    item=b
    return("Dog" and "Tiger") in item or None
print(func())