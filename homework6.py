my_list = {'Grisha': 2000,'Petya': 1992,'Misha': 2005}
print(my_list)
print(my_list['Misha'])
print(my_list.get('Kirill'))
my_list.update({'Sasha':1970,
               'Roma':2010})
a = my_list.pop('Petya')
print(a)
print(my_list)

my_set = {1,2,3,2,3,1,'str',5.6,"str",5.6}
print(my_set)
my_set.update([12,34])
my_set.remove(1)
print(my_set)