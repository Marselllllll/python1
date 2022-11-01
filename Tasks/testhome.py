from lib_deg import function_for_deg as fun
def f(*args, **kwargs):
    numb = 0
    lst_args = []
    lst_kwargs = []
    for i in args:
        result_deg_1 = fun.deg_to_gms(i)
        numb += 1
        tup_1 = (f'Point_{numb}', result_deg_1)
        lst_args.append(tup_1)
    for im, ch in kwargs.items():
        result_deg_2 = fun.deg_to_gms(ch)
        tup_2 = (im, result_deg_2)
        lst_kwargs.append(tup_2)
    lst_args.extend(lst_kwargs)
    return lst_args

print(f(45,34,23,v=44,n=21))