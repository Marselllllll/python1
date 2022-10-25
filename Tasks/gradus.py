from math import pi
def dgrad(grad, formats = 'string'):
    """

    :param grad: Параметр, подающий на вход угловые градусы в виде рационального числа.
    :param formats:Параметр, подающий на вход значение формата вывода данных. Может принимать два строковых значения: "string" и "num". Без указаний ставится "string".
    :return:Число, возвращаемое функцией в виде десятичных градусов в формате "Градусы, минуты, секунды".
    """
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
    """

    :param cel: Параметр, подающий на вход значение градусов формата десятичного градусого представления.
    :param min: Параметр, подающий на вход значение минут формата десятичного градусого представления.
    :param sec: Параметр, подающий на вход занчение секунд формата десятичного градусого представления.
    :return: Число, возвращаемое функцией в виде угловых градусов.
    """
    grad = cel + min/60 + sec/3600
    return grad

print(dgrad(36.97))
print(mgrad(36, 58 ,12))

def ggrad(grad):
    """

    :param grad: Параметр, подающий на вход угловые градусы в виде рационального числа.
    :return: Число, возвращаемое функцией в виде радионной меры угла.
    """
    rad = grad*pi/180
    return rad

def rgrad(rad):
    """

    :param rad: Параметр, подающий на вход радианную меру угла в виде рационального числа.
    :return: Число, возвращаемое функцией в виде угловых градусов.
    """
    grad = rad*180/pi
    return grad

print(ggrad(90))
print(rgrad(ggrad(90)))