"""Головний модуль додатку
   вивід на екран та в файл розрахункових даних
"""

import os
from process_data import create_ruh_list
from data_service import get_dovidniks, get_means, show_means, show_dovidniks

MAIN_MENU = \
    """
    ~~~~~~~~~~~~~ Обробка даних ~~~~~~~~~~~~~
    1-вивід руху коштів на екран
    2-запис заявок в файл
    3-вивід основних засобів
    0-завершити роботу
    _________________________________________
    """

TITLE = "АНАЛІЗ РУХУ ОСНОВНИХ ЗАСОБІВ"
HEADER = \
    '''
==============================================================================================================
| Підприємство     |  Вид основних засобів  |   Залишок   | Надійшло |  Вибуло  |   Залишок   |Зміни вартості|
|                  |                        | на 01.01.18 |  y 2018  |  y 2018  | на 01.01.19 |   за рік     |               
==============================================================================================================
    '''
FOOTER = \
    '''
==============================================================================================================
    '''

STOP_MESSAGE = "Нажміть будь-яку клавішу для продовження "

def show_ruh(ruh_list):
    """Виводить сформовані таблиці на екран

    Args:
        ruh_list ([type]): таблиці
    """
    print(f'\n\n{TITLE:^90}')
    print(HEADER)
    
    for ruh in ruh_list:
        print(f"{ruh['pidpr_name']:20}",
              f"{ruh['zasib_name']:25}",
              f"{float(ruh['zalyshok_2018']):>10.2f}",
              f"{float(ruh['nadiyshlo_2018']):>10.2f}",
              f"{float(ruh['vybulo_2018']):>10.2f}",
              f"{float(ruh['zalyshok_2019']):>11.2f}",
              f"{float(ruh['zmina_vartosti']):>11.2f}"
              )
    
    print(FOOTER)


while True:

    os.system('cls')
    print(MAIN_MENU)
    command_number = input('Введіть номер команди: ')

    # Обробка команд користувача
    if command_number == '0':
        print('\n Програма завершила роботу')
        exit(0)
    
    elif command_number == '1':
        ruh_list = create_ruh_list()
        show_ruh(create_ruh_list())
        input(STOP_MESSAGE)

