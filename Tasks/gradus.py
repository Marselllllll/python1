from math import pi
def dgrad(grad, formats = 'string'):
    cel = int(grad)
    min = int((grad - cel) * 60)
    sec = ((grad - cel) * 60 - min)*60
    sec = round(sec, 5)
    if formats == 'string':
        answer = f'{cel}° {min}′ {sec}″ '
    elif formats =='num':
        answer = (cel, min, sec)
    else:
        answer = None
    return answer

def mgrad(cel,min,sec):
    grad = cel + min/60 + sec/3600
    return grad

print(dgrad(36.97))
print(mgrad(36, 58 ,12))

def ggrad(grad):
    rad = grad*pi/180
    return rad

def rgrad(rad):
    grad = rad*180/pi
    return grad

print(ggrad(90))
print(rgrad(ggrad(90)))