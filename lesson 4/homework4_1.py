lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = [iterable for iterable in lst1 if type(iterable) == str]
print(lst2)
