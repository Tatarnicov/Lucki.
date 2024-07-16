my_dict = {'Yar': 2000, 'Vano': 1995, 'Misha': 2005}
print(my_dict)
print(my_dict['Yar'])
my_dict['Yasha'] = 1990
my_dict.update({'Alex': 1999,
                'Sergo': 2010})
print(my_dict)
del my_dict ['Yasha']
print(my_dict)

my_set= {1, 2, 3, 4, 5, 3, 4, 1, 2, 7, 5}
print(my_set)
my_set.add((10, 3.14))
my_set.remove(3)
print(my_set)