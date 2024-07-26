import requests


class DjangoClient:
    def __init__(self):
        self.base_url = 'http://192.168.0.30:8080/'

    def send_data(self, url, data=None, files=None):
        print(f'Sending {url} to {data}')
        self.base_url += url + '/'
        print(self.base_url)

        try:
            response = requests.get(self.base_url)
            if response.status_code == 200:
                print('Success', 'Data sent successfully!')
                return response.json()
            else:
                print('Error', 'Failed to send data.')
        except requests.exceptions.RequestException as e:
            print('Error', f'An error occurred: {e}')

    def post_data(self, url, data=None, files=None):

        self.base_url += url + '/'
        print(self.base_url, data)
        if not(data is None) and files is None:
            response = requests.post(self.base_url, data=data)
            print(response.status_code)
            if response.status_code == 200:
                print('Success', 'Data sent successfully!')
            else:
                print('Error', 'Failed to send data.')
        if not(data is None) and not(files is None):
            response = requests.post(self.base_url, files=files, data=data)
            print(response.status_code)
            if response.status_code == 200:
                print('Success', 'Data sent successfully!')
            else:
                print('Error', 'Failed to send data.')


    def get_data(self, url):
        url = 'http://localhost:8080/receive_data/'
        params = {'data': ''}
        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            # Обработка полученных данных
            print('Получены данные с сервера:', data)
        else:
            print('Ошибка при получении данных с сервера')

