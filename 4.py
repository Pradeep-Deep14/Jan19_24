ages=[5,10,15,20,25,30]

def func(age):
    if age < 18:
        return False
    else:
        return True

allowed_driving=filter(func,ages)

for x in allowed_driving:
    print(x)