import requests

ddate = '2023-05-15'
dtime = '15:30'
city_id = '15'
r = requests.get(
    f'https://bodygraph.online/api_v1/bodygraph_fractal_min.php?dkey=test_public_key&ddate=2004-07-15&dtime=15:30&dcity=15')
soup = r.json()

print(soup)
list_ = {'status': 1,
         'descr': 'Authorized',
         'data': {'header': {'city': 'Москва, Россия',
                             'local_birthdate': '2023-05-15 15:30',
                             'api_url': 'bodygraph_fractal_min.php',
                             'bodygraph_id': '31804'},
                  'details': {'subject_type_id': '5',
                              'subject_type_name': 'Манифестирующий Генератор',
                              'personal_line_id': '6',
                              'personal_line_name': 'Ролевая Модель',
                              'design_line_id': '3',
                              'design_line_name': 'Мученик',
                              'profile_id': '11',
                              'profile_name': 'Ролевая Модель - Мученик',
                              'subject_authority_id': '2',
                              'subject_authority_name': 'Эмоциональный авторитет'}
                  },
         'request': {'dkey': 'test_public_key',
                     'ddate': '2023-05-15',
                     'dtime': '15:30',
                     'dcity': '15',
                     'received_at': '2023-11-09 18:12:42',
                     'received_from': '92.39.219.249'}
         }
print(list_['data']['header']['city'])