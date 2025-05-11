import requests
from bs4 import BeautifulSoup

from api import bot
base_url = "https://starvisor.ru"

city_map = {
    "Азеево": f"{base_url}/azv/", 
    "Айхал": f"{base_url}/ayk/",
    "Альметьевск": f"{base_url}/almet/",
    "Васкелово": f"{base_url}/spbd/",
    "Багдарин": f"{base_url}/bag/",
    "Березники": f"{base_url}/brz/",
    "Вологда": f"{base_url}/vlg/",
    "Гулькевичи": f"{base_url}/gul/",
    "Воркута": f"{base_url}/vrk/",
    "Провидения": f"{base_url}/prv/",
    "Ирбит": f"{base_url}/irb/",
    "Калининград": f"{base_url}/kln/",
    "Калуга": f"{base_url}/klg/",
    "Каменск-Уральский": f"{base_url}/kur/", 
    "Краснодар": f"{base_url}/nov/",
    "Москва": f"{base_url}/msc/",
    "Остроленский": f"{base_url}/ost/",
    "Пермь": f"{base_url}/prm/",
    "Попово": f"{base_url}/ppv/",
    "Пятиречье": f"{base_url}/ptr/",
    "Русское": f"{base_url}/rus/",
    "Рязань": f"{base_url}/rzn/",
    "Стрежевой": f"{base_url}/str/",
    "Тула": f"{base_url}/tula/",
    "Уткино": f"{base_url}/utk/",
    "Челябинск": f"{base_url}/chb/",
    "Юрга": f"{base_url}/yur/",
    "Ярославль": f"{base_url}/yar/", 
    "Тырнауз": f"https://gw.cmo.sai.msu.ru/webcam6.jpg"
}

def get_camera_image(city):
    URL = city_map[city]
    response = requests.get(URL)
    if city == "Тырнауз":
        if response.status_code == 200:
            return response.content
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        camera_image = soup.find('img', class_='single-city-image')  
        if camera_image:
            image_url = camera_image['src']
            if not image_url.startswith('http'):
                image_url = URL + image_url
            image_response = requests.get(image_url)
            if image_response.status_code == 200:
                return image_response.content
    return None

def send_image_to_telegram(image_bytes, id):
    try:
        bot.send_photo(id, photo=image_bytes)
    except e:
        print(f"Error: Could not send photo to {i}. Further details:\n{e}")
