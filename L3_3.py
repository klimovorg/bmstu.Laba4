#
#   Шаг 0. Создание полносвязного графа с весами размера N
#
#   Шаг 1. Создание первоначальной популяции размером L в L_array
#
#   Шаг 2.  Расчет текущих экземпляров
#
#   Шаг 3. Отбрасываем слабейших (вес больше среднего) + добавляем мутантов до кол-ва L :)
#
#   Шаг 4. Возращаемся ко 2-му шагу
#
import datetime
import random
import itertools
import math
import matplotlib.pyplot as plt


#Темная магия создания весов путей размера NxN
def creatinggraph(N):
    for row in range(N):
        temp = []
        for element in range(N):
            temp.append(random.random()*10+1)
        ROUTEs.append(temp)

    for i in range(N):
        ROUTEs[i][i] = 0

    ROUTEs[Start][Finish] = 10


def createnewmutant():
    item = []
    item.append(Start)
    for i in range(N-2):
        item.append(math.trunc(random.random()*(N-2)+1))
    item.append(Finish)
    return item

def mutation(item):
    for _ in range(int(random.random()*(N/2))):
        item[int(random.random()*(N-2)+1)] = int(random.random()*(N-2)+1)
    return item

#
#   Мини настрока
#


N = int(input('Кол-во вершин - '))  #кол-во вершин графа
Start = int(input('Старт - '))
Finish = int(input('Финиш - '))
L = 5000 #размер первоначальной популяции

best_L = None #Текущий лучший из популяции
best_L_weight = None #Вес текущего лучшего из популяции

#инфа для остановки работы скрипта
cur_minute = 3
cur_hour = 42


#
#   Шаг 0. Создание полносвязного графа с весами размера N
#


ROUTEs = [] #массив весов перехода
creatinggraph(N)

experiment = int(input('Кол-во экспериментов: '))
pokolenie = int(input('Введите кол-во поколений: '))

for exp in range(experiment):

    #
    #   Шаг 1. Создание первоначальной популяции размером L в L_array
    #

    L_array = []

    for i in range(L):
        L_array.append(createnewmutant())

    #
    #   Шаг 2.  Расчет текущих экземпляров
    #
    L_array_weight = []

    flag = True
    for y in range(pokolenie):
        for l in L_array:
            weight_temp = 0

            for i in range(N - 1):
                weight_temp += ROUTEs[l[i]][l[i + 1]]

            L_array_weight.append(int(weight_temp))

        if flag:
            # инициализация
            best_L = L_array[0]
            best_L_weight = L_array_weight[0]
            flag = False

        the_arithmetic_mean = 0

        for i in range(len(L_array)):
            the_arithmetic_mean += L_array_weight[i]
            if int(str(L_array_weight[i])) < int(str(best_L_weight)):
                best_L = L_array[i]
                best_L_weight = L_array_weight[i]

        the_arithmetic_mean = the_arithmetic_mean / len(L_array)

        # print('Итерация',y,', лучший - ',best_L,best_L_weight)

        plt.scatter(y, best_L_weight, color='g')

        #
        #   Шаг 3. Отбрасываем слабейших (вес больше среднего) + добавляем мутантов до кол-ва L
        #

        # отсев слабых
        new_L_array = []

        for i in range(0, len(L_array) - 1):
            if L_array_weight[i] < the_arithmetic_mean:
                new_L_array.append(L_array[i])

        # мутация
        while len(new_L_array) < L:
            # new_L_array.append(createnewmutant())
            new_L_array.append(mutation(L_array[int(random.random() * (len(L_array)))]))

        L_array = new_L_array
        L_array_weight = []

    plt.show()
    plt.clf()
    print('Эксперимент', exp, ', лучший - ', best_L, best_L_weight)
