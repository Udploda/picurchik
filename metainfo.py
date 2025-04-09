# meta developer: @kanal_ikca and @cmert_hikki
from telethon import events
from .. import loader, utils
import asyncio
import requests
import json
from datetime import datetime
import pytz

class MetaInfoMod(loader.Module):
    """недоскрипт dox swat deanon"""
    
    strings = {"name": "писюрик"}
    
    def __init__(self):
        self.default_text = "паниолоф сосал кста"
    
    @loader.command()
    async def metainfo(self, message):
        """Использование: .metainfo (в ответ на сообщение)
        доксет лаха(лахашку)"""
        
        if not message.is_reply:
            await message.edit("❌ Ответьте на сообщение пользователя")
            return
            
        # Получаем информацию о пользователе
        user = await message.get_reply_message()
        user_info = await message.client.get_entity(user.sender_id)
        
        # Создаем сообщение с метаинформацией
        meta_text = f"""👤 <b>докс ипани:</b>

🆔 ID: <code>{user_info.id}</code>
👤 Имя: <code>{user_info.first_name}</code>
📝 Фамилия: <code>{user_info.last_name if user_info.last_name else 'Нет'}</code>
🔗 Username: <code>@{user_info.username if user_info.username else 'Нет'}</code>
📱 Телефон: <code>{user_info.phone if hasattr(user_info, 'phone') and user_info.phone else 'Нет'}</code>

💬 {self.default_text}"""
        
        # Отправляем сообщение
        await message.edit(meta_text, parse_mode='html')
    
    @loader.command()
    async def deanon(self, message):
        """Использование: .deanon (в ответ на сообщение)
        деанонит нахуй"""
        
        if not message.is_reply:
            await message.edit("❌ Ответьте на сообщение пользователя")
            return
            
        # Получаем информацию о пользователе
        user = await message.get_reply_message()
        user_info = await message.client.get_entity(user.sender_id)
        
        # Зеленая загрузка
        loading_steps = [
            "🟢⬜⬜⬜⬜⬜⬜⬜⬜⬜ 10%",
            "🟢🟢⬜⬜⬜⬜⬜⬜⬜⬜ 20%",
            "🟢🟢🟢⬜⬜⬜⬜⬜⬜⬜ 30%",
            "🟢🟢🟢🟢⬜⬜⬜⬜⬜⬜ 40%",
            "🟢🟢🟢🟢🟢⬜⬜⬜⬜⬜ 50%",
            "🟢🟢🟢🟢🟢🟢⬜⬜⬜⬜ 60%",
            "🟢🟢🟢🟢🟢🟢🟢⬜⬜⬜ 70%",
            "🟢🟢🟢🟢🟢🟢🟢🟢⬜⬜ 80%",
            "🟢🟢🟢🟢🟢🟢🟢🟢🟢⬜ 90%",
            "🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢 100%"
        ]
        
        for step in loading_steps:
            await message.edit(f"⏳ ДЕАНОН: {step}")
            await asyncio.sleep(0.5)
        
        # Формируем сообщение с информацией
        deanon_text = f"""│『😐』│｢Имя｣ - Дилдун

│『👨‍❤️‍💋‍👨』│｢Фамилия｣ - Гандонович

│『🤥』│｢Отчество｣- Эрондодонович

│『🤮』│｢юзернейм｣ - нету потому что бомж

│『👩‍🏫』│｢Мать｣ сосет хуи за 2.52 рубля

│『💩』│｢Отец｣ - Сникерс ебанный блядь

│『🗑️』│｢Проживание｣ - мусорка суслика 52

│『🩸』│｢id｣ - {user_info.id}"""
        
        # Отправляем сообщение
        await message.edit(deanon_text)
    
    @loader.command()
    async def doxgram(self, message):
        """Использование: .doxgram
        ссыока на доксграm"""
        
        # Длительная загрузка с разными этапами
        loading_steps = [
            "🔍 Проверка конфиденциальности...",
            "📂 Поиск файлов...",
            "🔒 Расшифровка данных...",
            "📊 Анализ информации...",
            "🔄 Загрузка файла...",
            "✅ Проверка целостности...",
            "🚀 Подготовка к отправке...",
            "📤 Отправка файла...",
            "✨ Очистка следов...",
            "🎉 Загрузка завершена!"
        ]
        
        for step in loading_steps:
            await message.edit(f"⏳ {step}")
            await asyncio.sleep(1.5)  # Более длительная задержка для эффекта
        
        # Формируем сообщение со ссылкой
        doxgram_text = f"""🔗 Держи ссылку чтобы скачать доксграм:

https://clck.ru/3LAQyk"""
        
        # Отправляем сообщение
        await message.edit(doxgram_text)
    
    @loader.command()
    async def time(self, message):
        """Использование: .time <город>
        Показывает время в указанном городе"""
        
        args = utils.get_args_raw(message)
        if not args:
            await message.edit("❌ Укажите город. Например: .time Москва")
            return
            
        try:
            # Получаем координаты города через OpenStreetMap API
            geocode_url = f"https://nominatim.openstreetmap.org/search?format=json&q={args}"
            geocode_response = requests.get(geocode_url, headers={'User-Agent': 'Telegram Bot'})
            geocode_data = geocode_response.json()
            
            if not geocode_data:
                await message.edit(f"❌ Город '{args}' не найден")
                return
                
            # Получаем часовой пояс по координатам
            lat = float(geocode_data[0]['lat'])
            lon = float(geocode_data[0]['lon'])
            
            timezone_url = f"https://api.timezonedb.com/v2.1/get-time-zone?key=YOUR_API_KEY&format=json&by=position&lat={lat}&lng={lon}"
            timezone_response = requests.get(timezone_url)
            timezone_data = timezone_response.json()
            
            if timezone_data['status'] != 'OK':
                await message.edit("❌ Не удалось определить часовой пояс")
                return
                
            # Получаем время в указанном городе
            timezone_name = timezone_data['zoneName']
            city_time = datetime.now(pytz.timezone(timezone_name))
            
            # Форматируем время
            time_text = f"""🕒 <b>Время в городе {args}:</b>

📅 Дата: <code>{city_time.strftime('%d.%m.%Y')}</code>
⏰ Время: <code>{city_time.strftime('%H:%M:%S')}</code>
🌍 Часовой пояс: <code>{timezone_name}</code>"""
            
            await message.edit(time_text, parse_mode='html')
            
        except Exception as e:
            await message.edit(f"❌ Ошибка: {str(e)}")
    
    @loader.command()
    async def weather(self, message):
        """Использование: .weather <город>
        Показывает погоду в указанном городе"""
        
        args = utils.get_args_raw(message)
        if not args:
            await message.edit("❌ Укажите город. Например: .weather Москва")
            return
            
        try:
            # Получаем погоду через OpenWeatherMap API
            api_key = "YOUR_API_KEY"  # Замените на ваш API ключ
            weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={args}&appid={api_key}&units=metric&lang=ru"
            weather_response = requests.get(weather_url)
            weather_data = weather_response.json()
            
            if weather_data.get('cod') != 200:
                await message.edit(f"❌ Город '{args}' не найден")
                return
                
            # Извлекаем данные о погоде
            temp = weather_data['main']['temp']
            feels_like = weather_data['main']['feels_like']
            humidity = weather_data['main']['humidity']
            wind_speed = weather_data['wind']['speed']
            description = weather_data['weather'][0]['description']
            
            # Форматируем сообщение о погоде
            weather_text = f"""🌤 <b>Погода в городе {args}:</b>

🌡 Температура: <code>{temp}°C</code>
🌡 Ощущается как: <code>{feels_like}°C</code>
💧 Влажность: <code>{humidity}%</code>
💨 Скорость ветра: <code>{wind_speed} м/с</code>
☁️ Облачность: <code>{description}</code>"""
            
            await message.edit(weather_text, parse_mode='html')
            
        except Exception as e:
            await message.edit(f"❌ Ошибка: {str(e)}")
    
    @loader.command()
    async def helpic(self, message):
        """Использование: .helpic
        Показывает информацию о командах"""
        
        help_text = """📱 <b>Команды модуля:</b>

🔍 <b>.metainfo</b> - доксет лаха(лахашку)
   

👤 <b>.deanon</b> - деанонит нахуй
   

🔗 <b>.doxgram</b> - ссыока на доксграm
   Скачать DoxGram без наепа

🚨 <b>.swat</b> - swat нахуй
   Отправка SWAT команды

📢 <b>.chan</b> - информация о канале
   Подписка и обновление

🕒 <b>.time</b> - время в городе
   Показывает текущее время

🌤 <b>.weather</b> - погода в городе
   Показывает текущую погоду

❤️ <b>.love</b> - анимация сердечек
   Показывает красивую анимацию

by x and paniolof"""
        
        # Отправляем сообщение
        await message.edit(help_text, parse_mode='html')
    
    @loader.command()
    async def swat(self, message):
        """Использование: .swat (в ответ на сообщение)
        swat нахуй"""
        
        if not message.is_reply:
            await message.edit("❌ Ответьте на сообщение пользователя")
            return
            
        # Получаем информацию о пользователе
        user = await message.get_reply_message()
        user_info = await message.client.get_entity(user.sender_id)
        
        # Загрузка с этапами swat операции
        loading_steps = [
            "🔍 Получение IP адреса...",
            "📱 Определение местоположения...",
            "🚔 Отправка патруля...",
            "👮 Подготовка SWAT команды...",
            "🚨 Окружение здания...",
            "💥 Взлом дверей...",
            "🔫 Зачистка помещения...",
            "👮‍♂️ Задержание подозреваемого...",
            "🚓 Доставка в участок...",
            "📝 Составление протокола..."
        ]
        
        for step in loading_steps:
            await message.edit(f"⏳ SWAT ОПЕРАЦИЯ: {step}")
            await asyncio.sleep(1.5)
        
        # Формируем сообщение с результатом
        swat_text = f"""🚨 <b>SWAT ОПЕРАЦИЯ ЗАВЕРШЕНА</b>

👮‍♂️ Подозреваемый: <code>{user_info.first_name}</code>
🆔 ID: <code>{user_info.id}</code>

📝 Результат операции:
• Твой хуй или писта был деформирован
• Забран в полицейский департамент
• Ожидает судебного разбирательства

⚖️ Приговор: Пожизненное заключение в камере с решеткой"""
        
        # Отправляем сообщение
        await message.edit(swat_text, parse_mode='html')
    
    @loader.command()
    async def chan(self, message):
        """Использование: .chan
        Показывает информацию о канале и обновлении"""
        
        chan_text = """📢 <b>Подпишитесь на наш канал</b>

Чтобы получать обновления и новые функции, подпишитесь на наш канал:
<a href="https://t.me/kanal_ikca">@kanal_ikca</a>

Или обновите код бота:
<code>.dlm https://raw.githubusercontent.com/Udploda/picurchik/refs/heads/main/metainfo.py</code>"""
        
        # Отправляем сообщение
        await message.edit(chan_text, parse_mode='html')
    
    @loader.command()
    async def love(self, message):
        """Использование: .love
        Показывает анимацию с сердечками"""
        
        # Анимация с сердечками разного размера
        heart_frames = [
            "❤️",
            "❤️❤️",
            "❤️❤️❤️",
            "❤️❤️❤️❤️",
            "❤️❤️❤️❤️❤️",
            "❤️❤️❤️❤️❤️❤️",
            "❤️❤️❤️❤️❤️❤️❤️",
            "❤️❤️❤️❤️❤️❤️❤️❤️",
            "❤️❤️❤️❤️❤️❤️❤️❤️❤️",
            "❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️",
            "❤️❤️❤️❤️❤️❤️❤️❤️❤️",
            "❤️❤️❤️❤️❤️❤️❤️❤️",
            "❤️❤️❤️❤️❤️❤️❤️",
            "❤️❤️❤️❤️❤️❤️",
            "❤️❤️❤️❤️❤️",
            "❤️❤️❤️❤️",
            "❤️❤️❤️",
            "❤️❤️",
            "❤️"
        ]
        
        # Показываем анимацию
        for frame in heart_frames:
            await message.edit(frame)
            await asyncio.sleep(0.3)
        
        # Финальное сообщение
        final_text = """❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️ ЛЮБОВЬ ❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️"""
        
        await message.edit(final_text) 
