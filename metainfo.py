# meta developer: @kanal_ikca and @cmert_hikki
from telethon import events
from .. import loader, utils
import asyncio

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
    async def helpic(self, message):
        """Использование: .helpic
        Показывает информацию о командах"""
        
        help_text = """📱 <b>Команды модуля:</b>

🔍 <b>.metainfo</b> - доксет лаха(лахашку)
   

👤 <b>.deanon</b> - деанонит нахуй
   

🔗 <b>.doxgram</b> - ссыока на доксграm
   Скачать DoxGram без наепа

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
• Твой хуй был деформирован
• Забран в полицейский департамент
• Ожидает судебного разбирательства

⚖️ Приговор: Пожизненное заключение в камере с решеткой"""
        
        # Отправляем сообщение
        await message.edit(swat_text, parse_mode='html') 