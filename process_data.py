"""Аналіз руху основних засобів
"""

from data_service import get_dovidniks, get_means

#структура вихідних даних
ruh = {
    'pidpr_name' : '',     #назва підприємства
    'zasib_name' : '',     #вид оновних засобів
    'zalyshok_2018' : 0,   #залишок на 1.01.2018
    'nadiyshlo_2018' : 0,  #надійшло у 2018
    'vybulo_2018' : 0,     #вибуло у 2018
    'zalyshok_2019' : 0,  #залишок на 1.01.2019
    'zmina_vartosti' : 0  #зміни вартості за рік 
}

def create_ruh_list():
    """формування списку руху коштів
    """

    def get_zasib_name(zasib_code):
        """Повертає назву основного засобу

        Args:
            zasib_code ([type]): код засобу 
        """

        for dovidnik in dovidniks:
            if int(zasib_code) == int(dovidnik[0]):
                return dovidnik[1]
        
        return "Назва не знайдена"

    ruh_list = []

    means = get_means()
    dovidniks = get_dovidniks()

    # послідовна обробка рядків масиву "Mean"
    for mean in means:

        # зробити робочий список
        ruh_work = ruh.copy()

        # заповнити робочими значеннями
        ruh_work['pidpr_name'] = mean[0]
        ruh_work['zasib_name'] = get_zasib_name(mean[1])
        ruh_work['zalyshok_2018'] = mean[2]
        ruh_work['nadiyshlo_2018'] = mean[3]
        ruh_work['vybulo_2018'] = mean[4]
        ruh_work['zalyshok_2019'] = float(ruh_work['zalyshok_2018']) + float(ruh_work['nadiyshlo_2018']) - float(ruh_work['vybulo_2018'])
        ruh_work['zmina_vartosti'] = float(ruh_work['nadiyshlo_2018']) - float(ruh_work['vybulo_2018'])

        # накопичити сформований рядок
        ruh_list.append(ruh_work)
    
    return ruh_list

test_list = create_ruh_list()



