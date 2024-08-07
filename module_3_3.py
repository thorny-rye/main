def print_params(a=1, b='строка', c=True):
    print(a, b, c)
values_list = [2, 5.5, "sheep"]
values_dict = {"a": 55, "b": False, "c": 6.4}
values_list_2 = [54.32, 'Строка' ]
print_params()
print_params(2, 'string')
print_params(b = 25)
print_params(c = [1,2,3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)