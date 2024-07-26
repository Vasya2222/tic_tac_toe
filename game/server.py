import requests
import asyncio



# Отправка данных на сервер
async def send_data_to_server(data, url):
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=data) as response:
            return await response.text()


async def main():
    url = 'http://localhost:8080/receive_data/'
    params = {'data': ''}
    response = await send_data_to_server(url, params)

    print(response)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())

# Получение данных с сервера

def receive_data_from_server():
    url = 'http://localhost:8080/receive_data/'
    params = {'data': ''}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        # Обработка полученных данных
        print('Получены данные с сервера:', data)
    else:
        print('Ошибка при получении данных с сервера')
