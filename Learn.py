import Gift
import operator # Импортируем нужный модуль

def main_learn():
  print ('Выберите задачу: ')
  print ('Задача номер 1, необходимо вывести цифры меньше 5 с массива')
  print ('Задачи номер 2, нужно обьединить 2 массива и сделать один с одинаковыми  элементами')
  print ('Задача номер 3, обьединить 3 словаря в 1')
  print ('Задача номер 4, отсортируйте словарь по значению в порядке возрастания и убывания.')
  print ('Задача номер 5, Найдите три ключа с самыми высокими значениями в словаре.')
  print ('Задача номер 6, Напишите код, который переводит целое число в строку, при том что его можно применить в любой системе счисления.')
  a = input('Введите номер задачи:  ')
  a = int(a)
  if a==1: 
    first_Lesson([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89])
  elif a==2:
    second_Lesson([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], [1, 2, 3, 4, 5, 6, 7,   8, 9, 10, 11, 12, 13])
  elif a==3:
    thirth_Lesson()
  elif a==4:
    fourth_Lesson()   
  elif a==5:
    fiveth_Lesson({'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20})  
  elif a==6:
    sixth_Lesson()    
  else: 
    print ('Извините, это не моя проблема')

def first_Lesson(mass):
  print('Старт: ', mass)
  i = 0
  for i in mass:
    if i < 5:
      print (i)
  print([elem for elem in mass if elem < 5])
  print('Задача выполнена')
def second_Lesson(mass_a,mass_b):
  print('Старт')
  print ('первый массив', mass_a)
  print ('второй массив', mass_b)
  mass_c = [] # обьявляем пустой массив, в который будем закидывать одинаковые файлы.
  for i in mass_a:
    for j in mass_b:
      if i == j:
        mass_c.append (i)
  print('Сам массив: ',mass_c)
  print ('Задача выполнена')
  print ('Старт задачи номер 3')
def thirth_Lesson():
  dict_all = {}
  Gift.add (dict_all, {1:'one', 2:'two'})
  Gift.add (dict_all, {3:'there', 4:'four'})
  Gift.add (dict_all, {5:'five', 6:'six'})
  Gift.show (dict_all)
def fourth_Lesson():
  print ('Сортируем в порядке возрастания:')
  slovar = {1: 1, 2: 2, 4: 4, 6: 6, 3: 3, 5: 5, 0: 0}
  result = dict(sorted(slovar.items(), key=operator.itemgetter(1)))
  print ('В порядке возрастания = ', result )
  result_anti = dict(sorted(slovar.items(), key=operator.itemgetter(1), reverse=True))
  print ('В порядке убывания = ', result_anti)
def fiveth_Lesson(my_dict):
  result = sorted(my_dict, key=my_dict.get, reverse=True)[:3]
  print (result)
def sixth_Lesson():
  print(str('Fuck', 13))

# for i in (dict_a, dict_b, dict_c):
#    dict_all.update(i)
#   print(dict_all)
# dict_all = {**dict_a, **dict_b, **dict_c}
# print(dict_all)
# dict_all = {**dict_a, **dict_b, **dict_c}
# print(dict_all)
