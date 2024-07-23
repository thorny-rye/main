immutable_var = (1, 1.2, 'печенька', True)
print(immutable_var)
#immutable_var[0]= 2
# значения элементов кортежа не изменяются, потому что он нужен для хранения упорядоченной последовательности элементов
# это делает его надежным хранителем данных
mutable_list = [1, 1.2, 'печенька', True]
mutable_list.append('элемент')
print(mutable_list)