"""модуль призначено для роботи з файлами вхіднх даних
"""


def get_dovidniks():
    """повертає список довідник з файла 'dovidnik.txt`

    Returns:
       dovidniks_list : список довідника
    """
    
    with open("./data/dovidnik.txt") as dovidnik_file:
        from_file = dovidnik_file.readlines()

    # накопичувач
    dovidniks_list = []
    
    for line in from_file:
        line_list = line.split(';')
        dovidniks_list.append(line_list)

    return dovidniks_list

def get_means():
    """повертає список засобів з файла 'mean.txt`

    Returns:
       means_list : список клієнтів
    """
    
    with open("./data/mean.txt") as mean_file:
        from_file = mean_file.readlines()

    # накопичувач клієнтів
    means_list = []
    
    for line in from_file:
        line_list = line.split(';')
        means_list.append(line_list)

    return means_list

def show_dovidniks(dovidniks):
    """виводить на екран список довідник по заданій умові

    Args:
        dovidniks (list): список довідника
    """

#    dovidnik_code_from = input("З якого код? ")
#    dovidnik_code_to   = input("По який  код? ")

    # підрахунок кількості знайдених рядків
    kol_lines = 0
    
    for dovidnik in dovidniks:
       # if  dovidnik_code_from <= dovidnik[0] <= dovidnik_code_to:
        print("код: {:1} тип:{:16}".format(dovidnik[0], dovidnik[1]))
        kol_lines += 1
    
    if kol_lines == 0:
        print("По вашому запиту нічого не знайдено!")

def show_means(means):
    """ 
    виводить на екран список засобів по заданій умові

    Args:
        means (list): список засобів
    """

    mean_find = input("Оберіть код: ")
    

    # підрахунок кількості знайдених рядків
    kol_line = 0
    
    for mean in means:
         if  mean_find == mean[1]:
            print("Підприємство: {:15} тип: {:2} залишок: {:7} надійшло: {:7} вибуток: {:5}".format(mean[0], mean[1], mean[2], mean[3], mean[4]))
            kol_line += 1
    
    if kol_line == 0:
        print("По вашому запиту нічого не знайдено!")


#dovidniks = get_dovidniks()   
#show_dovidniks(dovidniks)

#means = get_means()
#show_means(means)
