from settings import settings
import requests 
import json



class Car():
    
    #добавить машину
    def create_record(self):
        print('Creating new info about car...')
        obj = { 'fields':
                {'brand': str(input('Введите название марки машины: ')),
                'model': str(input('Введите модель машины: ')),
                'year': int(input('Введите дату производства машины: ')),
                'volume': float(input('Введите объем двигателя машины: ')),
                'color': str(input('Введите цвет машины: ')),
                'type': str(input('Введите тип кузова машины: ')),
                'mileage': int(input('Введите пробек машины(км): ')),
                'price': float(input('Введите цену машины($): '))
                },
                'typecast': True}
        obj = json.dumps(obj)
        req = requests.post(settings.get_url, headers=settings.TOKEN, data=obj)
        return req.json()

    #лист машин
    def listing_records(self):
        print('List of car')
        req = requests.get(
            settings.get_url,
            headers={'Authorization': settings.TOKEN_UNI})
        return req.text

    #информация об одной машине по id
    def retrieve_record(self):
        print('Retrieving info about car...')
        print('Введите id машины , или получите полный список авто')
        id_ = input('Введите id машины что узнать информацию: ')
        req = requests.get(settings.get_url + f'/{id_}', headers=settings.TOKEN)
        return req.json()

    #обновить информацию о машине
    def update_record(self):
        print('Updating info about car...')
        id_ = input('Введите id машины для изменения информации: ')
        data = {'fields':
                {'brand': str(input('Введите название марки машины: ')),
                'model': str(input('Введите модель машины: ')),
                'year': int(input('Введите дату производства машины: ')),
                'volume': float(input('Введите объем двигателя машины: ')),
                'color': str(input('Введите цвет машины: ')),
                'type': str(input('Введите тип кузова машины: ')),
                'mileage': int(input('Введите пробек машины(км): ')),
                'price': float(input('Введите цену машины($): '))
                },
                'typecast': True}
        data =json.dumps(data)
        req = requests.put(settings.get_url + f'/{id_}', headers=settings.TOKEN, data=data)
        return req.text

    #удаление информации об машине
    def delete_record(self):
        print('Удалени будет безвозвратным !')
        id_ = input('Введите id для удаленние информации o машине: ')
        req = requests.delete(
        settings.get_url + f'/{id_}', 
        headers={'Authorization': settings.TOKEN_UNI}, 
        data=f'records[]={id_}')
        print('Car is deleting')
        return req.json()    

 

