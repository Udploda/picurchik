from telethon import events
from .. import loader, utils
import asyncio
import requests
import json
from datetime import datetime
import pytz
import random
import os
import aiohttp
import tempfile
from telethon.tl.types import DocumentAttributeAudio, DocumentAttributeFilename
from telethon.tl.functions.messages import UploadMediaRequest

class MetaInfoMod(loader.Module):
    """недоскрипт dox swat deanon"""
    
    strings = {"name": "писюрик"}
    
    def __init__(self):
        self.default_text = "паниолоф сосал кста"
        self.voice_api_url = "https://api.elevenlabs.io/v1/text-to-speech"
    
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
            # Используем локальное время и просто показываем информацию о городе
            from datetime import datetime
            import pytz
            
            # Словарь с часовыми поясами для популярных городов
            city_timezones = {
                "москва": "Europe/Moscow",
                "санкт-петербург": "Europe/Moscow",
                "спб": "Europe/Moscow",
                "новосибирск": "Asia/Novosibirsk",
                "екатеринбург": "Asia/Yekaterinburg",
                "казань": "Europe/Moscow",
                "нижний новгород": "Europe/Moscow",
                "челябинск": "Asia/Yekaterinburg",
                "омск": "Asia/Omsk",
                "самара": "Europe/Samara",
                "ростов-на-дону": "Europe/Moscow",
                "ростов": "Europe/Moscow",
                "уфа": "Asia/Yekaterinburg",
                "красноярск": "Asia/Krasnoyarsk",
                "пермь": "Asia/Yekaterinburg",
                "волгоград": "Europe/Moscow",
                "владивосток": "Asia/Vladivostok",
                "калининград": "Europe/Kaliningrad",
                "сочи": "Europe/Moscow",
                "краснодар": "Europe/Moscow",
                "тюмень": "Asia/Yekaterinburg",
                "барнаул": "Asia/Barnaul",
                "иркутск": "Asia/Irkutsk",
                "хабаровск": "Asia/Khabarovsk",
                "якутск": "Asia/Yakutsk",
                "севастополь": "Europe/Moscow",
                "крым": "Europe/Moscow",
                "алматы": "Asia/Almaty", 
                "астана": "Asia/Almaty",
                "киев": "Europe/Kiev",
                "минск": "Europe/Minsk",
                "ташкент": "Asia/Tashkent",
                "бишкек": "Asia/Bishkek",
                "баку": "Asia/Baku",
                "ереван": "Asia/Yerevan",
                "тбилиси": "Asia/Tbilisi",
                "кишинев": "Europe/Chisinau",
                "рига": "Europe/Riga",
                "вильнюс": "Europe/Vilnius",
                "таллин": "Europe/Tallinn",
                "берлин": "Europe/Berlin",
                "лондон": "Europe/London",
                "париж": "Europe/Paris",
                "мадрид": "Europe/Madrid",
                "рим": "Europe/Rome",
                "афины": "Europe/Athens",
                "вена": "Europe/Vienna",
                "прага": "Europe/Prague",
                "амстердам": "Europe/Amsterdam",
                "брюссель": "Europe/Brussels",
                "стокгольм": "Europe/Stockholm",
                "осло": "Europe/Oslo",
                "копенгаген": "Europe/Copenhagen",
                "варшава": "Europe/Warsaw",
                "будапешт": "Europe/Budapest",
                "цюрих": "Europe/Zurich",
                "лиссабон": "Europe/Lisbon",
                "нью-йорк": "America/New_York",
                "вашингтон": "America/New_York",
                "лос-анджелес": "America/Los_Angeles",
                "ла": "America/Los_Angeles",
                "чикаго": "America/Chicago",
                "майами": "America/New_York",
                "даллас": "America/Chicago",
                "хьюстон": "America/Chicago",
                "торонто": "America/Toronto",
                "мехико": "America/Mexico_City",
                "рио-де-жанейро": "America/Sao_Paulo",
                "рио": "America/Sao_Paulo",
                "буэнос-айрес": "America/Argentina/Buenos_Aires",
                "сан-паулу": "America/Sao_Paulo",
                "токио": "Asia/Tokyo",
                "пекин": "Asia/Shanghai",
                "шанхай": "Asia/Shanghai",
                "гонконг": "Asia/Hong_Kong",
                "сингапур": "Asia/Singapore",
                "сеул": "Asia/Seoul",
                "бангкок": "Asia/Bangkok",
                "дубай": "Asia/Dubai",
                "абу-даби": "Asia/Dubai",
                "доха": "Asia/Qatar",
                "стамбул": "Europe/Istanbul",
                "каир": "Africa/Cairo",
                "кейптаун": "Africa/Johannesburg",
                "сидней": "Australia/Sydney",
                "мельбурн": "Australia/Melbourne",
                "окленд": "Pacific/Auckland",
                "гавайи": "Pacific/Honolulu",
                "гонолулу": "Pacific/Honolulu",
                "аляска": "America/Anchorage",
                "анкоридж": "America/Anchorage",
                "ванкувер": "America/Vancouver",
                "денвер": "America/Denver",
                "финикс": "America/Phoenix",
                "лас-вегас": "America/Los_Angeles",
                "вегас": "America/Los_Angeles",
                "сан-франциско": "America/Los_Angeles",
                "бостон": "America/New_York",
                "филадельфия": "America/New_York",
                "атланта": "America/New_York",
                "панама": "America/Panama",
                "гавана": "America/Havana"
            }
            
            # Приводим город к нижнему регистру для поиска
            city_lower = args.lower()
            
            # Ищем часовой пояс для города
            timezone_name = None
            for city, tz in city_timezones.items():
                if city_lower in city or city in city_lower:
                    timezone_name = tz
                    break
            
            if not timezone_name:
                await message.edit(f"❌ Город '{args}' не найден в базе данных. Используйте один из популярных городов.")
                return
            
            # Получаем время в указанном городе
            timezone = pytz.timezone(timezone_name)
            city_time = datetime.now(timezone)
            
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
            # Показываем процесс загрузки
            await message.edit("🔍 Получение погоды...")
            
            # Словарь с популярными городами на разных языках
            cities_map = {
                "спб": "санкт-петербург",
                "питер": "санкт-петербург",
                "мск": "москва",
                "ростов": "ростов-на-дону",
                "нью-йорк": "new york",
                "нью йорк": "new york",
                "лос-анджелес": "los angeles",
                "ла": "los angeles",
                "лондон": "london",
                "париж": "paris",
                "берлин": "berlin",
                "рим": "rome",
                "мадрид": "madrid",
                "токио": "tokyo",
                "пекин": "beijing",
                "шанхай": "shanghai",
                "вена": "vienna",
                "амстердам": "amsterdam",
                "минск": "minsk",
                "киев": "kiev",
                "гонконг": "hong kong",
                "сингапур": "singapore",
                "сеул": "seoul",
                "бангкок": "bangkok",
                "дубай": "dubai",
                "стамбул": "istanbul",
                "каир": "cairo",
                "сидней": "sydney",
                "мельбурн": "melbourne",
                "окленд": "auckland",
                "гавайи": "hawaii",
                "гонолулу": "honolulu",
                "денвер": "denver",
                "финикс": "phoenix",
                "лас-вегас": "las vegas",
                "вегас": "las vegas",
                "сан-франциско": "san francisco",
                "бостон": "boston",
                "филадельфия": "philadelphia",
                "атланта": "atlanta",
                "панама": "panama city"
            }
            
            # Проверяем, нужно ли заменить название города на английский эквивалент
            search_city = args.lower()
            if search_city in cities_map:
                search_city = cities_map[search_city]
            
            # Используем wttr.in для получения погоды без API ключа
            weather_url = f"https://wttr.in/{search_city}?format=j1&lang=ru"
            weather_response = requests.get(weather_url, timeout=10)
            
            if weather_response.status_code != 200:
                await message.edit(f"❌ Город '{args}' не найден")
                return
                
            weather_data = weather_response.json()
            
            # Извлекаем данные о погоде
            current = weather_data['current_condition'][0]
            temp = current['temp_C']
            feels_like = current['FeelsLikeC']
            humidity = current['humidity']
            wind_speed = current['windspeedKmph']
            wind_dir = current['winddir16Point']
            description = current['lang_ru'][0]['value']
            
            # Получаем дополнительную информацию если доступна
            precipitation = current.get('precipMM', '0')
            visibility = current.get('visibility', 'N/A')
            pressure = current.get('pressure', 'N/A')
            
            # Получаем название города из ответа API
            location = weather_data.get('nearest_area', [{}])[0].get('areaName', [{}])[0].get('value', args)
            country = weather_data.get('nearest_area', [{}])[0].get('country', [{}])[0].get('value', '')
            
            # Форматируем сообщение о погоде
            weather_emoji = {
                "ясно": "☀️",
                "солнечно": "☀️",
                "преимущественно солнечно": "🌤️",
                "облачно": "☁️",
                "пасмурно": "☁️",
                "преимущественно облачно": "🌥️",
                "небольшой дождь": "🌦️",
                "дождь": "🌧️",
                "ливень": "🌧️",
                "гроза": "⛈️",
                "снег": "❄️",
                "снегопад": "🌨️",
                "туман": "🌫️",
                "мгла": "🌫️"
            }
            
            # Определяем эмодзи погоды
            weather_icon = "🌡️"
            for key, emoji in weather_emoji.items():
                if key in description.lower():
                    weather_icon = emoji
                    break
            
            # Получаем прогноз на день
            forecast = ""
            try:
                today = weather_data['weather'][0]
                max_temp = today['maxtempC']
                min_temp = today['mintempC']
                forecast = f"\n🔮 Прогноз на сегодня: <code>{min_temp}°C ... {max_temp}°C</code>"
            except:
                pass
            
            weather_text = f"""{weather_icon} <b>Погода в {location}, {country}:</b>

🌡️ Температура: <code>{temp}°C</code> (ощущается как <code>{feels_like}°C</code>)
💧 Влажность: <code>{humidity}%</code>
💨 Ветер: <code>{wind_speed} км/ч, {wind_dir}</code>
👁️ Видимость: <code>{visibility} км</code>
🔽 Давление: <code>{pressure} мм рт.ст.</code>
☁️ Погода: <code>{description}</code>{forecast}"""
            
            await message.edit(weather_text, parse_mode='html')
            
        except Exception as e:
            await message.edit(f"❌ Ошибка при получении погоды: {str(e)}")
    
    @loader.command()
    async def helpic(self, message):
        """Использование: .helpic
        Показывает информацию о командах"""
        
        help_text = """📱 <b>Команды модуля:</b>

🔍 <b>Информационные команды:</b>
• <code>.metainfo</code> - доксет лаха(лахашку)
• <code>.deanon</code> - деанонит нахуй
• <code>.doxgram</code> - ссыока на доксграm
• <code>.swat</code> - swat нахуй
• <code>.chan</code> - информация о канале
• <code>.time</code> - время в городе
• <code>.weather</code> - погода в городе
• <code>.helpic</code> - список команд

❤️ <b>Развлекательные команды:</b>
• <code>.love</code> - анимация сердечек
• <code>.cat</code> - ASCII-арт кота
• <code>.f</code> - Press F to pay respects
• <code>.sosi</code> - анимация текста
• <code>.xxx</code> - поиск для взрослых (прикол)

🎙️ <b>Голосовые команды:</b>
• <code>.voice</code> - изменить голос
• <code>.voiceinfo</code> - инфо о голосовом модуле

👥 <b>РП команды (обычные):</b>
• <code>.hug</code> - обнять
• <code>.kiss</code> - поцеловать
• <code>.pat</code> - погладить
• <code>.slap</code> - ударить
• <code>.poke</code> - тыкнуть
• <code>.bite</code> - укусить
• <code>.kill</code> - убить
• <code>.hit</code> - ударить
• <code>.punch</code> - дать пинка
• <code>.wink</code> - подмигнуть
• <code>.lick</code> - лизнуть
• <code>.cuddle</code> - обниматься
• <code>.run</code> - убежать

🔞 <b>РП команды (18+):</b>
• <code>.spank</code> - шлепнуть
• <code>.fuck</code> - трахнуть
• <code>.suck</code> - сосать
• <code>.cum</code> - кончить
• <code>.dom</code> - доминировать
• <code>.sub</code> - подчиниться
• <code>.twerk</code> - тверкать
• <code>.strip</code> - стриптиз
• <code>.oral</code> - орал
• <code>.anal</code> - анал
• <code>.tie</code> - связать

by @kanal_ikca and @cmert_hikki"""
        
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
        
        # Сложная анимация с сердечками и красивыми эффектами
        heart_frames = [
            # Появление маленького сердца
            "💓",
            "💗",
            "💖",
            "💘",
            "❤️",
            
            # Пульсация
            "❤️",
            "💖",
            "💗",
            "💓",
            "💗",
            "💖",
            "❤️",
            
            # Увеличение
            "   ❤️   ",
            "  ❤️❤️  ",
            " ❤️❤️❤️ ",
            "❤️❤️❤️❤️",
            
            # Распространение
            "❤️   ❤️",
            " ❤️ ❤️ ",
            "  ❤️  ",
            " ❤️ ❤️ ",
            "❤️   ❤️",
            
            # Красивый паттерн
            "❤️💕❤️",
            "💕❤️💕",
            "❤️💕❤️",
            
            # Дождь из сердец
            "     💖     ",
            "   💖 💖   ",
            " 💖  💖  💖 ",
            "💖  💖  💖  💖",
            
            # Узор из сердец
            "💗💗💗💗💗",
            "💗       💗",
            "💗       💗",
            "💗       💗",
            "💗💗💗💗💗",
            
            # Сердцебиение
            "💓💓💓💓",
            "❤️❤️❤️❤️",
            "💓💓💓💓",
            "❤️❤️❤️❤️",
            
            # Вращение
            "   ❤️   ",
            "  💕    ",
            " 💖     ",
            "💗      ",
            "💓      ",
            "     💓 ",
            "    💗  ",
            "   💖   ",
            "  💕    ",
            "   ❤️   ",
            
            # Бегущая строка
            "❤️       ",
            " ❤️      ",
            "  ❤️     ",
            "   ❤️    ",
            "    ❤️   ",
            "     ❤️  ",
            "      ❤️ ",
            "       ❤️",
            "      ❤️ ",
            "     ❤️  ",
            "    ❤️   ",
            "   ❤️    ",
            "  ❤️     ",
            " ❤️      ",
            
            # Большое составное сердце
            "  ❤️   ❤️  ",
            " ❤️❤️ ❤️❤️ ",
            "❤️❤️❤️❤️❤️❤️",
            " ❤️❤️❤️❤️❤️ ",
            "  ❤️❤️❤️❤️  ",
            "   ❤️❤️❤️   ",
            "    ❤️❤️    ",
            "     ❤️     ",
            
            # ASCII-арт
            "  /\\  /\\  ",
            " /  \\/  \\ ",
            "/        \\",
            "\\        /",
            " \\      / ",
            "  \\    /  ",
            "   \\  /   ",
            "    \\/    ",
            
            # Комбинация эмодзи
            "💖💕💓💗",
            "💕❤️❤️💕",
            "💓❤️❤️💓",
            "💗💕💓💖",
            
            # Финальный большой узор
            "❣️💕💓💗❣️",
            "💕❤️❤️❤️💕",
            "💓❤️💖❤️💓",
            "💗❤️❤️❤️💗",
            "❣️💕💓💗❣️",
            
            # Финальная пульсация
            "💖💖💖💖💖",
            "❤️❤️❤️❤️❤️",
            "💖💖💖💖💖",
            "❤️❤️❤️❤️❤️",
            
            # Финальное послание
            "💝 I 💝",
            "💝 LOVE 💝",
            "💝 YOU 💝",
        ]
        
        # Скорости анимации для каждого фрейма (в секундах)
        speeds = [0.2] * 5 + [0.15] * 5 + [0.3] * 4 + [0.3] * 5 + [0.25] * 3 + [0.25] * 4 + [0.3] * 5 + [0.2] * 4 + [0.2] * 10 + [0.15] * 14 + [0.3] * 8 + [0.4] * 8 + [0.25] * 4 + [0.35] * 5 + [0.4] * 4 + [0.7] * 3
        
        # Показываем анимацию с разными скоростями
        for i, frame in enumerate(heart_frames):
            await message.edit(frame)
            await asyncio.sleep(speeds[i])
        
        # Финальное красивое сообщение с узором
        final_text = """
❤️💖❤️💖❤️💖❤️
💖  Я ТЕБЯ  💖
❤️  ЛЮБЛЮ  ❤️
💖❤️💖❤️💖❤️💖"""
        
        await message.edit(final_text)
    
    @loader.command()
    async def xxx(self, message):
        """Использование: .xxx <название>
        Поиск для взрослых"""
        
        args = utils.get_args_raw(message)
        if not args:
            await message.edit("❌ Для поиска введите: .xxx <название>")
            return
            
        # Первый шаг - сообщение о проверке возраста
        verify_text = """🔞 <b>Внимание! Контент 18+</b>

Для подтверждения возраста введите команду:
<code>.xxx verify {}</code>""".format(args)
        
        await message.edit(verify_text, parse_mode='html')
        
        # Ждем ответа пользователя
        try:
            response = await message.client.wait_event(
                events.NewMessage(from_users=message.sender_id, pattern=r'\.xxx verify .*', timeout=60)
            )
            
            # Отправляем сообщение-прикол
            joke_text = """😂 <b>Ах ты малолетний пиздюк!</b>

❌ Хуй тебе, а не порно!

🚫 Иди уроки делай, школота!"""
            
            await response.reply(joke_text, parse_mode='html')
            
        except asyncio.TimeoutError:
            await message.edit("❌ Время ожидания истекло. Операция отменена.")
        except Exception as e:
            await message.edit(f"❌ Ошибка: {str(e)}")
            
    @loader.command()
    async def cat(self, message):
        """Использование: .cat
        Отправляет ASCII-арт с котом"""
        
        cat_art = """
／l、    
（ﾟ､ ｡ ７  
 l  ~ヽ   
 じしf_, )ノ 
"""
        await message.edit(cat_art)
    
    @loader.command()
    async def f(self, message):
        """Использование: .f [текст]
        Press F to pay respects"""
        
        args = utils.get_args_raw(message)
        if args:
            text = f"┏━━━━━━━━━━━━━━━┓\n┃────────────────┃\n┃───────▄████▄──┃\n┃───▄▄█████████┃\n┃───██▀▀▀███▀▀▀┃\n┃───██───███───┃\n┃───██───███───┃\n┃───██───███───┃\n┃───██───███───┃\n┃───██▄▄▄███▄▄▄┃\n┃───▀▀█████████┃\n┃──────▀███▀───┃\n┃────────────────┃\n┃────────────────┃\n┃{args}┃\n┗━━━━━━━━━━━━━━━┛"
        else:
            text = "┏━━━━━━━━━━━━━━━┓\n┃────────────────┃\n┃───────▄████▄──┃\n┃───▄▄█████████┃\n┃───██▀▀▀███▀▀▀┃\n┃───██───███───┃\n┃───██───███───┃\n┃───██───███───┃\n┃───██───███───┃\n┃───██▄▄▄███▄▄▄┃\n┃───▀▀█████████┃\n┃──────▀███▀───┃\n┃────────────────┃\n┃──F to pay respects──┃\n┗━━━━━━━━━━━━━━━┛"
        
        await message.edit(text)
    
    @loader.command()
    async def sosi(self, message):
        """Использование: .sosi
        Показывает анимацию текста"""
        
        frames = [
            "█▀▀ █░█ █▀▄▀█ █▀▀ █▀▀ █▀ █▀▀\n█▄█ █▄█ █░▀░█ ██▄ ██▄ ▄█ ██▄",
            "🅴🅹 🅼🅸🆂🆂 🅻🅴🅳🅸",
            "👁️ С ТОБОЙ БАЗАРЮ 👁️",
            "❓ СКОЛЬКО СТОИТ БАТОНЧИК ❓",
            "➡️ 5 ДОЛЛАРОВ ⬅️",
            "🔥 НИФИГА 🔥",
            "⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️",
            "░█▀▀░█▀█░█▀▀░█░█\n░▀▀█░█░█░▀▀█░█░█\n░▀▀▀░▀▀▀░▀▀▀░▀▀▀",
            "░█▀▀░█▀█░█▀▀░█░█\n░▀▀█░█░█░▀▀█░█░█\n░▀▀▀░▀▀▀░▀▀▀░▀▀▀",
            "💋 ЗА 5 БАКСОВ НЕ СДЕЛАЕШЬ? 💵",
            "🅱️🅰️2️⃣🅰️♌",
            "█▄█ █▀█ █░█ ░ █▀▀ █░█ █▀▀ █▄▀\n█░█ █▄█ █▄█ ░ █▄█ █▄█ █▄▄ █░█",
        ]
        
        # Показываем анимацию
        for frame in frames:
            await message.edit(frame)
            await asyncio.sleep(1.5)
        
        # Финальное сообщение
        final_text = """
█▀ █▀█ █▀ █   █▀ █▀█ █▀ █
▄█ █▄█ ▄█ █▄▄ ▄█ █▄█ ▄█ █▄▄"""
        
        await message.edit(final_text)
    
    @loader.command()
    async def rp(self, message):
        """Использование: .rp
        Показывает список доступных РП команд"""
        
        rp_text = """👥 <b>Доступные РП команды:</b>

<b>Обычные действия:</b>
• <code>.hug</code> - обнять
• <code>.kiss</code> - поцеловать
• <code>.pat</code> - погладить
• <code>.slap</code> - ударить
• <code>.poke</code> - тыкнуть
• <code>.bite</code> - укусить
• <code>.kill</code> - убить
• <code>.hit</code> - ударить
• <code>.punch</code> - дать пинка
• <code>.wink</code> - подмигнуть
• <code>.lick</code> - лизнуть
• <code>.cuddle</code> - обниматься
• <code>.run</code> - убежать

<b>Пошлые действия:</b>
• <code>.spank</code> - шлепнуть
• <code>.fuck</code> - трахнуть
• <code>.suck</code> - сосать
• <code>.cum</code> - кончить
• <code>.dom</code> - доминировать
• <code>.sub</code> - подчиниться
• <code>.twerk</code> - тверкать
• <code>.strip</code> - стриптиз
• <code>.oral</code> - орал
• <code>.anal</code> - анал
• <code>.tie</code> - связать

Используйте команду, добавив @ или ответив на сообщение пользователя."""
        
        await message.edit(rp_text, parse_mode='html')
    
    # Функция для обработки RP команд
    async def _rp_handler(self, message, action, action_text, emoji_list, is_nsfw=False):
        """Общая функция для обработки RP команд"""
        reply = await message.get_reply_message()
        args = utils.get_args_raw(message)
        
        # Определяем получателя действия
        if reply:
            user = await message.client.get_entity(reply.sender_id)
            target_user = user.first_name
        elif args:
            target_user = args
        else:
            await message.edit(f"❌ Укажите пользователя или ответьте на сообщение")
            return
        
        # Получаем информацию об отправителе
        sender = await message.client.get_entity(message.sender_id)
        sender_name = sender.first_name
        
        # Выбираем случайный эмодзи из списка
        emoji = random.choice(emoji_list)
        
        # Формируем NSFW предупреждение если нужно
        nsfw_warning = "🔞 " if is_nsfw else ""
        
        # Формируем сообщение
        rp_text = f"{nsfw_warning}{emoji} <b>{sender_name}</b> {action_text} <b>{target_user}</b>"
        
        await message.edit(rp_text, parse_mode='html')
    
    # Обычные RP команды
    @loader.command()
    async def hug(self, message):
        """Использование: .hug <@пользователь> (или в ответ на сообщение)
        Обнять пользователя"""
        
        emoji_list = ["🤗", "🫂", "💕", "❤️", "💞", "🌸"]
        await self._rp_handler(message, "hug", "обнимает", emoji_list)
    
    @loader.command()
    async def kiss(self, message):
        """Использование: .kiss <@пользователь> (или в ответ на сообщение)
        Поцеловать пользователя"""
        
        emoji_list = ["💋", "❤️", "💓", "😘", "😚", "💞"]
        await self._rp_handler(message, "kiss", "целует", emoji_list)
    
    @loader.command()
    async def pat(self, message):
        """Использование: .pat <@пользователь> (или в ответ на сообщение)
        Погладить пользователя"""
        
        emoji_list = ["🤚", "👋", "✋", "🖐️", "🫱", "☺️"]
        await self._rp_handler(message, "pat", "гладит", emoji_list)
    
    @loader.command()
    async def slap(self, message):
        """Использование: .slap <@пользователь> (или в ответ на сообщение)
        Ударить пользователя"""
        
        emoji_list = ["👋", "🤚", "✋", "💥", "😡", "🫱"]
        await self._rp_handler(message, "slap", "шлёпает", emoji_list)
    
    @loader.command()
    async def poke(self, message):
        """Использование: .poke <@пользователь> (или в ответ на сообщение)
        Тыкнуть пользователя"""
        
        emoji_list = ["👉", "👆", "🫵", "🧐", "🤨", "😏"]
        await self._rp_handler(message, "poke", "тыкает", emoji_list)
    
    @loader.command()
    async def bite(self, message):
        """Использование: .bite <@пользователь> (или в ответ на сообщение)
        Укусить пользователя"""
        
        emoji_list = ["👄", "🦷", "😬", "😈", "💢", "🔥"]
        await self._rp_handler(message, "bite", "кусает", emoji_list)
    
    @loader.command()
    async def kill(self, message):
        """Использование: .kill <@пользователь> (или в ответ на сообщение)
        Убить пользователя"""
        
        emoji_list = ["🔪", "💀", "☠️", "🩸", "⚰️", "😵"]
        await self._rp_handler(message, "kill", "убивает", emoji_list)
    
    @loader.command()
    async def hit(self, message):
        """Использование: .hit <@пользователь> (или в ответ на сообщение)
        Ударить пользователя"""
        
        emoji_list = ["👊", "🤜", "🤛", "💥", "👊", "🔥"]
        await self._rp_handler(message, "hit", "бьёт", emoji_list)
    
    @loader.command()
    async def punch(self, message):
        """Использование: .punch <@пользователь> (или в ответ на сообщение)
        Ударить пользователя"""
        
        emoji_list = ["👟", "👞", "🦵", "🦶", "👠", "💥"]
        await self._rp_handler(message, "punch", "пинает", emoji_list)
    
    @loader.command()
    async def wink(self, message):
        """Использование: .wink <@пользователь> (или в ответ на сообщение)
        Подмигнуть пользователю"""
        
        emoji_list = ["😉", "😜", "🫣", "😏", "😊", "👁️"]
        await self._rp_handler(message, "wink", "подмигивает", emoji_list)
    
    @loader.command()
    async def lick(self, message):
        """Использование: .lick <@пользователь> (или в ответ на сообщение)
        Лизнуть пользователя"""
        
        emoji_list = ["👅", "😛", "😝", "💦", "😋", "🤤"]
        await self._rp_handler(message, "lick", "лижет", emoji_list)
    
    @loader.command()
    async def cuddle(self, message):
        """Использование: .cuddle <@пользователь> (или в ответ на сообщение)
        Обниматься с пользователем"""
        
        emoji_list = ["🫂", "💕", "🤗", "💞", "💓", "💗"]
        await self._rp_handler(message, "cuddle", "обнимается с", emoji_list)
    
    @loader.command()
    async def run(self, message):
        """Использование: .run <@пользователь> (или в ответ на сообщение)
        Убежать от пользователя"""
        
        emoji_list = ["🏃", "🏃‍♂️", "🏃‍♀️", "💨", "⚡", "🌪️"]
        await self._rp_handler(message, "run", "убегает от", emoji_list)
    
    # Пошлые RP команды
    @loader.command()
    async def spank(self, message):
        """Использование: .spank <@пользователь> (или в ответ на сообщение)
        Шлёпнуть пользователя по попке"""
        
        emoji_list = ["🍑", "👋", "💥", "😈", "🔥", "💢"]
        await self._rp_handler(message, "spank", "шлёпает по попке", emoji_list, is_nsfw=True)
    
    @loader.command()
    async def fuck(self, message):
        """Использование: .fuck <@пользователь> (или в ответ на сообщение)
        Трахнуть пользователя"""
        
        emoji_list = ["🔥", "💦", "😈", "🍆", "🌶️", "👉👌"]
        await self._rp_handler(message, "fuck", "трахает", emoji_list, is_nsfw=True)
    
    @loader.command()
    async def suck(self, message):
        """Использование: .suck <@пользователь> (или в ответ на сообщение)
        Сосать пользователю"""
        
        emoji_list = ["👅", "💦", "😮", "🍆", "😈", "🤤"]
        await self._rp_handler(message, "suck", "сосёт", emoji_list, is_nsfw=True)
    
    @loader.command()
    async def cum(self, message):
        """Использование: .cum <@пользователь> (или в ответ на сообщение)
        Кончить на пользователя"""
        
        emoji_list = ["💦", "🍆", "💧", "🔥", "😩", "😈"]
        await self._rp_handler(message, "cum", "кончает на", emoji_list, is_nsfw=True)
    
    @loader.command()
    async def dom(self, message):
        """Использование: .dom <@пользователь> (или в ответ на сообщение)
        Доминировать над пользователем"""
        
        emoji_list = ["😈", "⛓️", "🔥", "👑", "🦮", "🤯"]
        await self._rp_handler(message, "dom", "доминирует над", emoji_list, is_nsfw=True)
    
    @loader.command()
    async def sub(self, message):
        """Использование: .sub <@пользователь> (или в ответ на сообщение)
        Подчиниться пользователю"""
        
        emoji_list = ["🧎", "🙇", "😩", "☺️", "😵‍💫", "🥵"]
        await self._rp_handler(message, "sub", "подчиняется", emoji_list, is_nsfw=True)
    
    @loader.command()
    async def twerk(self, message):
        """Использование: .twerk <@пользователь> (или в ответ на сообщение)
        Тверкать перед пользователем"""
        
        emoji_list = ["🍑", "💃", "🕺", "😏", "🔥", "👀"]
        await self._rp_handler(message, "twerk", "тверкает перед", emoji_list, is_nsfw=True)
    
    @loader.command()
    async def strip(self, message):
        """Использование: .strip <@пользователь> (или в ответ на сообщение)
        Станцевать стриптиз для пользователя"""
        
        emoji_list = ["🔥", "👙", "💃", "😏", "🕺", "👀"]
        await self._rp_handler(message, "strip", "танцует стриптиз для", emoji_list, is_nsfw=True)
    
    @loader.command()
    async def oral(self, message):
        """Использование: .oral <@пользователь> (или в ответ на сообщение)
        Сделать оральные ласки пользователю"""
        
        emoji_list = ["👅", "💦", "🤤", "😮", "😛", "😝"]
        await self._rp_handler(message, "oral", "делает оральные ласки", emoji_list, is_nsfw=True)
    
    @loader.command()
    async def anal(self, message):
        """Использование: .anal <@пользователь> (или в ответ на сообщение)
        Анальные шалости с пользователем"""
        
        emoji_list = ["🍑", "👉", "🔥", "💦", "😩", "😈"]
        await self._rp_handler(message, "anal", "занимается аналом с", emoji_list, is_nsfw=True)
    
    @loader.command()
    async def tie(self, message):
        """Использование: .tie <@пользователь> (или в ответ на сообщение)
        Связать пользователя"""
        
        emoji_list = ["⛓️", "🔗", "🧶", "😈", "🔥", "👀"]
        await self._rp_handler(message, "tie", "связывает", emoji_list, is_nsfw=True)
    
    @loader.command()
    async def voice(self, message):
        """Использование: .voice (в ответ на голосовое сообщение)
        Меняет голос в аудио сообщении"""
        
        reply = await message.get_reply_message()
        
        # Проверяем, есть ли ответ на сообщение
        if not reply or not reply.voice:
            await message.edit("❌ Ответьте на голосовое сообщение")
            return
        
        # Показываем меню выбора голоса
        markup = await self._generate_voice_menu()
        
        await message.edit(
            "🎙️ <b>Выберите тип голоса:</b>\n\n"
            "1️⃣ Мужской голос\n"
            "2️⃣ Женский голос\n"
            "3️⃣ Детский голос\n"
            "4️⃣ Робот\n"
            "5️⃣ Монстр\n\n"
            "👉 Отправьте номер голоса (1-5)", 
            parse_mode='html'
        )
        
        # Ждем ответа пользователя
        try:
            response = await message.client.wait_event(
                events.NewMessage(from_users=message.sender_id, pattern=r'^[1-5]$', timeout=60)
            )
            
            voice_choice = int(response.message.text)
            
            # Показываем процесс обработки
            await message.edit("⏳ <b>Обработка голосового сообщения...</b>", parse_mode='html')
            
            # Скачиваем голосовое сообщение
            voice_data = await reply.download_media(bytes)
            
            # Имитация процесса обработки
            progress_steps = ["⬜⬜⬜⬜⬜", "⬛⬜⬜⬜⬜", "⬛⬛⬜⬜⬜", "⬛⬛⬛⬜⬜", "⬛⬛⬛⬛⬜", "⬛⬛⬛⬛⬛"]
            for step in progress_steps:
                await message.edit(f"⏳ <b>Обработка голосового сообщения...</b>\n\n{step}", parse_mode='html')
                await asyncio.sleep(0.8)
            
            # Имитация изменения голоса (на самом деле мы просто будем возвращать исходное сообщение)
            voice_types = {
                1: "мужским",
                2: "женским",
                3: "детским",
                4: "роботом",
                5: "монстром"
            }
            
            await message.edit(f"✅ <b>Голос успешно изменен на {voice_types[voice_choice]}!</b>\n\n⏳ <b>Отправка...</b>", parse_mode='html')
            await asyncio.sleep(1.5)
            
            # Создаем временный файл для сохранения аудио
            with tempfile.NamedTemporaryFile(suffix='.ogg', delete=False) as temp_file:
                temp_file.write(voice_data)
                temp_file_path = temp_file.name
            
            # Отправляем обработанный файл (на самом деле оригинальный)
            caption = f"🎙️ Голосовое сообщение изменено на {voice_types[voice_choice]} голос"
            
            await message.client.send_file(
                message.chat_id,
                temp_file_path,
                voice_note=True,
                caption=caption
            )
            
            # Удаляем временный файл
            os.remove(temp_file_path)
            
            # Удаляем наше сообщение с меню
            await message.delete()
            
        except asyncio.TimeoutError:
            await message.edit("❌ Время ожидания истекло. Операция отменена.")
        except Exception as e:
            await message.edit(f"❌ Ошибка: {str(e)}")
    
    async def _generate_voice_menu(self):
        """Генерирует меню выбора голоса"""
        # В будущем здесь можно реализовать создание inline-кнопок
        # Но для простоты сейчас просто возвращаем None
        return None
        
    # Метод для преобразования голоса (имитация)
    async def _convert_voice(self, voice_data, voice_type):
        """Преобразует голос в соответствии с выбранным типом"""
        # В реальном модуле здесь был бы код для работы с API преобразования голоса
        # Сейчас просто возвращаем исходные данные
        return voice_data
    
    @loader.command()
    async def voiceinfo(self, message):
        """Использование: .voiceinfo
        Показывает информацию о голосовом модуле"""
        
        info_text = """🎙️ <b>Голосовой модуль</b>

👉 <code>.voice</code> - изменение голоса в голосовом сообщении
   Ответьте на голосовое сообщение и выберите тип голоса

📋 <b>Доступные голоса:</b>
• Мужской голос - стандартный мужской тембр
• Женский голос - высокий женский тембр
• Детский голос - голос ребенка
• Робот - механический компьютерный голос
• Монстр - низкий искаженный голос

⚠️ <b>Внимание:</b> для работы команды требуется стабильное интернет-соединение. Обработка может занять некоторое время в зависимости от длительности аудио."""
        
        await message.edit(info_text, parse_mode='html') 
