# -*- coding: utf-8 -*-
import telebot
import requests
from telebot import types
import logging
import os

TOKEN = os.environ['TOKEN']
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    sent = bot.send_message(message.chat.id, message.from_user.first_name + ', привет! Если ты живешь в Строгино, то я самый полезный робот на свете для тебя :) Почему? Я помогу тебе найти все, что угодно в Строгино! \n Если тебя интересует медицина в Строгино, \n жми /med')

@bot.message_handler(commands=['help'])
def start(message):
    sent = bot.send_message(message.chat.id, message.from_user.first_name + ', я помогу тебе здесь разобраться. Вот команды, которые я знаю: \n \start - чтобы начать выбор одежды  \n \n \n \n')

#этот хендлер удобен в групповом чате, где сидят все и наш бот в том числе.
greeting=["привет", "всем привет", "здравствуйте", "привет!", "хеллоу", "приветики", "Привет", "Привет!"]
@bot.message_handler(func=lambda message: message.text in greeting)
def handle_message(message):
    bot.send_message(message.chat.id, 'Привет! Я робот! Добро пожалось в наш чатик! Чтобы ознакомится с ассортиментом одежды Картерс, жми /start')

@bot.message_handler(commands=['med'])
def default_test(message):
    bot.send_message(message.chat.id, 'Итак, тебя интересует медицина в Строгино!'
                                        '\nКакая именно?'
                                        '\nЕсли бесплатная, то жми /free_med'
                                        '\nЕсли платная, жми /money_med \nДетская бесплатная медицина, \nжми /det_free_med \nПлатная детская медицина, жми /det_money_med \nСтоматология - /dent \n Полезные телефоны - /phone ' )

@bot.message_handler(commands=['free_med'])
def default_test(message):
    bot.send_message(message.chat.id, '🔶 🔶 🔶Перед тобой список бесплатных бюджетных медицинских учреждений в Строгино')
    markup = types.ReplyKeyboardMarkup()
    markup.row('👉Городская пoликлиника № 180 Филиал № 1')
    markup.row('👉Городская поликлиникa № 180 Филиал № 2')
    markup.row('👉Женская кoнсультация')
    markup.row('👉Стoматологическая поликлиника № 60')
    bot.send_message(message.chat.id, 'Нажимай на ту, что тебе нужна, чтобы узнать адрес, телефон и получить карту', reply_markup=markup)

@bot.message_handler(regexp="пoликлиника")
def handle_message(message):
    bot.send_message(message.chat.id, '👉Городская поликлиника № 180 Филиал № 1 (ГП 96) \nул. Кулакова, д. 23 \nСтол справок: \n☎ 84957503971 \nПомощь на дому: \n☎ 84957503978  \nТравматологический пункт: \n☎84957581286 \nВызов неотложной помощи: \n☎84957500111 \nhttp://gp180.mos.ru \nРасаписание врачей по ссылке\nhttp://gp180.mos.ru/content/shedule/f1/')
    bot.send_message(message.chat.id, 'Вы можете проложить маршрут до поликлинки, нажав на карту')
    bot.send_location(message.chat.id, latitude=55.8021665, longitude=37.3940866)

@bot.message_handler(regexp="поликлиникa")
def handle_message(message):
    bot.send_message(message.chat.id, '👉Городская поликлиника № 180 Филиал № 2 (ГП 181) \nул. Исаковского, д. 16, корп. 2 \nСтол справок: \n☎ 8(495)758-99-13 \nПомощь на дому: \n☎ 8(495)758-40-59 \nhttp://gp180.mos.ru \nРасаписание врачей по ссылке \nhttp://gp180.mos.ru/content/shedule/f2/')
    bot.send_message(message.chat.id, 'Вы можете проложить маршрут до поликлинки, нажав на карту')
    bot.send_location(message.chat.id, latitude=55.8115728, longitude=37.4053682)

@bot.message_handler(regexp="кoнсультация")
def handle_message(message):
    bot.send_message(message.chat.id, '👉Женская консультация \nул. Катукова, д. 5 \nСтол справок: \n☎ 8(495)750-41-84 \nhttp://gp180.mos.ru \nРасаписание врачей по ссылке \nhttp://gp180.mos.ru/content/shedule/f3/')
    bot.send_message(message.chat.id, 'Вы можете проложить маршрут до поликлинки, нажав на карту')
    bot.send_location(message.chat.id, latitude=55.8128917, longitude=37.3951224)

@bot.message_handler(regexp="Стoматологическая")
def handle_message(message):
    bot.send_message(message.chat.id, '👉Стоматологическая поликлиника № 60 \n ул. Твардовского, д. 27\nСтол справок: \n☎ +7 (495) 756-69-98 \nhttp://sp60.mos.ru \nРасаписание врачей по ссылке \nhttp://sp60.mos.ru/content/shedule/')
    bot.send_message(message.chat.id, 'Вы можете проложить маршрут до поликлинки, нажав на карту')
    bot.send_location(message.chat.id, latitude=55.797848, longitude=37.4044913)

@bot.message_handler(commands=['phone'])
def default_test(message):
    bot.send_message(message.chat.id, '👉Вызов неотложной помощи для взрослых по СЗАО: \n☎ 8 (495) 948-89-60 \n☎ 8 (495) 949-76-08 ')
##############
    bot.send_message(message.chat.id, '👉Единая справочная служба города Москвы (в том числе по вопросам доступности и качества бесплатной медицинской помощи) \n☎ 8(495)777-77-77')
##############
    bot.send_message(message.chat.id, '👉Акушерско-гинекологическая помощь  \n☎ 8(495)620-41-70')
##############
    bot.send_message(message.chat.id, '👉Психиатрическая помощь \n☎ 8(495)620-42-30')
##############
    bot.send_message(message.chat.id, '👉Взрослая глазная скорая помощь \n☎ 8(495)699-61-28')
##############
    bot.send_message(message.chat.id, '👉Справочная служба ДЗМ по вопросам лекарственного обеспечения \n☎ 8(495)974-63-65 \n🕓часы работы: \nпн.–сб. c 08.00 до 20.00, \nвс. – выходные дни')
##############
    bot.send_message(message.chat.id, '👉«Горячая линия» Департамента здравоохранения города Москвы: \nпо вопросам медицинской помощи\n☎ 8 (499) 251-83-00 \n \nпо вопросам лекарственного обеспечения\n☎ 8 (499) 251-14-55 \n\nпо вопросам вакцинации\n☎  8 (499) 194-27-74 \n\n🕓часы работы: \nпн.–пт. c 08.00 до 20.00, \nсб. и вс. – выходнsе дни.\n \nДежурный (круглосуточно): \n☎ 8(499) 251-83-00')
##############
    bot.send_message(message.chat.id, '👉Экстренная медико-психологическая помощь в кризисных ситуациях \n☎ 8 (499) 791-20-50')
##############
    bot.send_message(message.chat.id, '👉«Телефон доверия» экстренной психологической помощи \n☎ 8 (495) 575-87-70')
##############
    bot.send_message(message.chat.id, '👉Психологическая помощь женщинам \n☎ 8 (495) 282-84-50')
##############
    bot.send_message(message.chat.id, '👉Независимый благотворительный центр помощи пережившим сексуальное насилие \n☎ 8 (499) 901-02-01')
##############
    bot.send_message(message.chat.id, '👉Для подростков и молодежи наркологический диспансер №3 \n☎ 8 (499) 192-40-95')
##############
    bot.send_message(message.chat.id, '👉«Телефон доверия» акушерской службы \n☎ 8 (495) 332-21-13 \n🕓работает с 9 до 18:00 в рабочие дни')
##############

@bot.message_handler(commands=['money_med'])
def default_test(message):
    bot.send_message(message.chat.id, '🔷 🔷 🔷Перед тобой список платных медицинских учреждений в Строгино')
    bot.send_message(message.chat.id, '💰Семейный медицинский центр IMMA \n💎ул. Маршала Катукова, 24 к5, 2 этаж  \n☎+7 (495) 536-19-99 \n☎+7 (495) 660-30-90 \n☎+7 (499) 969-24-83 \n🔗www.imma.ru \n🕓Время работы:\nежедневно: 09:00 - 21:00 \n✅стоматология \n✅педиатрия \n✅женская консультация')
    bot.send_message(message.chat.id, '\n⚕️Узнать прейскурант\n, нажимайте /price_imma')
    bot.send_message(message.chat.id, '📍Вы можете проложить маршрут до учреждения, нажав на карту')
    bot.send_location(message.chat.id, latitude=55.803049, longitude=37.4108843)
    bot.send_message(message.chat.id, '💰"Натали-Мед" \n💎ул. Маршала Катукова, 6  \n☎+7 (495) 114-60-11\n🔗http://www.natalimed.ru/ \n🕓Время работы:\nпн-сб: 08:00—20:00 \nвс: 09:00—17:00 \n⛔стоматология \n⛔педиатрия \n✅женская консультация')
    bot.send_message(message.chat.id, '\n⚕️Узнать прейскурант\n, нажимайте /price_natali')
    bot.send_message(message.chat.id, '📍Вы можете проложить маршрут до учреждения, нажав на карту')
    bot.send_location(message.chat.id, latitude=55.81027, longitude=37.3998993)
#####
    bot.send_message(message.chat.id, '💰"Доктор рядом" \n💎ул. Кулакова, д. 20, стр. 1Л, 6 этаж; 1 подъезд \nБЦ Технопарк Орбита \n☎+7 (499) 553-05-23 \n☎+7 (495) 281-48-68\n🔗https://www.drclinics.ru/ \n🕓Время работы:\nпн-пт: 08:00—21:00 \nсб-вс: 09:00—19:00 \n✅стоматология \n⛔педиатрия \n✅женская консультация')
    bot.send_message(message.chat.id, '📍Вы можете проложить маршрут до учреждения, нажав на карту')
    bot.send_location(message.chat.id, latitude=55.805215, longitude=37.3908153)
#####
    bot.send_message(message.chat.id, '💰Медицинский центр "Лечу.ру" \n💎ул. Кулакова, 10, к.1. \n☎+7 (495) 642-62-63 \n☎+7 (800) 100-62-63 \n☎+7 (495) 276-17-75\n🔗www.lechy.ru \n🕓Время работы:пн-пт: 07:30—20:00 \nсб: 07:30—17:00 \nвс: 09:00—15:00  \n⛔стоматология \n⛔педиатрия \n✅женская консультация')
    bot.send_message(message.chat.id, '📍Вы можете проложить маршрут до учреждения, нажав на карту')
    bot.send_location(message.chat.id, latitude=55.811832, longitude=37.3950693)
#####
    bot.send_message(message.chat.id, '💰"Клиника Studio Smile" \n💎Строгинский бульвар д. 10 корп. 3 \n☎+7 (499) 740-17-15 \n☎+7 (495) 942-77-90\n🔗http://studiosmile.ru/ \n🕓Время работы:\nпн-пт: 08:00—21:00; \nсб: 09:00—20:00 \nвс: 10:00—18:00  \n✅стоматология \n✅педиатрия \n✅женская консультация')
    bot.send_message(message.chat.id, '\n⚕️Узнать прейскурант\n http://studiosmile.ru/Nashi-ceny/')
    bot.send_message(message.chat.id, '📍Вы можете проложить маршрут до учреждения, нажав на карту')
    bot.send_location(message.chat.id, latitude=55.802754, longitude=37.3941872)
#####
    bot.send_message(message.chat.id, '💰Офтальмологическая клиника "Окомед" \n💎ул. Таллинская, 26 \n☎+7 (495) 942-92-34 \n☎+7 (495) 942-84-40\n🔗www.okomed.ru \n🕓Время работы:\nпн-сб: 10:00—20:00 \nвс: 10:00—18:00')
    bot.send_message(message.chat.id, '\n⚕️Узнать прейскурант\n http://www.okomed.ru/price.html')
    bot.send_message(message.chat.id, '📍Вы можете проложить маршрут до учреждения, нажав на карту')
    bot.send_location(message.chat.id, latitude=55.799497, longitude=37.4056226)
#####
    bot.send_message(message.chat.id, '💰Косметологическая клиника MDElena \n💎ул. Твардовского, 12 к2 \n☎+7 (495) 744-78-45 \n☎+7 (925) 825-00-50\n🔗www.mdelena.ru \n🕓Время работы:\nежедневно: 10:00 - 23:00 \nпо предварительной записи')
    bot.send_message(message.chat.id, '\n⚕️Узнать прейскурант\n https://mdelena.ru/tseni/')
    bot.send_message(message.chat.id, '📍Вы можете проложить маршрут до учреждения, нажав на карту')
    bot.send_location(message.chat.id, latitude=55.7931817, longitude=37.39532)
#####
    bot.send_message(message.chat.id, '💰Реабилитационная клиника восстановительной медицины "Эвексия" \n💎ул. 2-я Лыковская улица, 67А \n☎+7 (495) 120-25-32\n🔗www.evexia.ru \n🕓Время работы:\nпн-пт: 09:00—17:00 \nпредварительная запись по телефону')
    bot.send_message(message.chat.id, '📍Вы можете проложить маршрут до учреждения, нажав на карту')
    bot.send_location(message.chat.id, latitude=55.790428, longitude=37.3815293)
#####
    bot.send_message(message.chat.id, '💰Психиатрическая клиника доктора Минутко «Психическое здоровье» \n💎Строгинский бульвар, 1 \nБЦ «Дарья», 4 этаж \n☎+7 (966) 330-11-66\n🔗https://psyclinic-center.ru \n🕓Время работы:\nкруглосуточно')
    bot.send_message(message.chat.id, '\n⚕️Узнать прейскурант\n https://psyclinic-center.ru/stoimost')
    bot.send_message(message.chat.id, '📍Вы можете проложить маршрут до учреждения, нажав на карту')
    bot.send_location(message.chat.id, latitude=55.8060025, longitude=37.3933675)
#####
    bot.send_message(message.chat.id, '💰Центр практической психологии "Эквалайс" \n💎Строгинский бульвар, 14к3, 1 этаж \n☎+7 (495) 760-59-29 \n☎+7 (495) 750-06-55\n🔗www.psyequal.ru \n🕓Время работы:\nежедневно: 09:00 - 21:00 \n✅детский центр')
    bot.send_message(message.chat.id, '\n⚕️Узнать прейскурант\n https://www.psyequal.ru/raspisanie-zanyatij')
    bot.send_message(message.chat.id, '📍Вы можете проложить маршрут до учреждения, нажав на карту')
    bot.send_location(message.chat.id, latitude=55.803303, longitude=37.3973733)
#####
    bot.send_message(message.chat.id, '💰Флебологический городской Центр Лазерной Хирургии \n💎ул. Таллинская, 13 к1, 2 этаж \n☎+7 (495) 649-09-57 \n☎+7 (499) 190-31-18\n🕓Время работы:\nпн-сб: 10:00—19:00')
    bot.send_message(message.chat.id, '📍Вы можете проложить маршрут до учреждения, нажав на карту')
    bot.send_location(message.chat.id, latitude=55.7998703, longitude=37.3986406)
#####
    bot.send_message(message.chat.id, '💰Реабилитационный центр для наркозависимых "12 Шагов" \n💎ул. Исаковского, 39 \n☎+7 (926) 092-63-95 \n☎+7 (499) 398-27-19\n🔗www.narkozavisimyh-reabilitaciya.su \n🕓Время работы:\nкруглосуточно')
    bot.send_message(message.chat.id, '📍Вы можете проложить маршрут до учреждения, нажав на карту')
    bot.send_location(message.chat.id, latitude=55.8061741, longitude=37.4227159)

#стоматология в строгино
@bot.message_handler(commands=['dent'])
def default_test(message):
    bot.send_message(message.chat.id, '💰Стоматология "Санация" \n💎ул. Кулакова, 20, 1 этаж \n☎+7 (495) 488-25-70\n🔗http://sanacia.ru \n🕓Время работы:\nпн-сб: 10:00—20:00 \nвс: 10:00—18:00')
    bot.send_message(message.chat.id, '\n⚕️Узнать прейскурант\n http://sanacia.ru/ceny-na-uslugi/')
    bot.send_message(message.chat.id, '📍Вы можете проложить маршрут до учреждения, нажав на карту')
    bot.send_location(message.chat.id, latitude=55.8050949, longitude=37.3896074)
####
    bot.send_message(message.chat.id, '💰Стоматология MiaDent \n💎ул. Таллинская, д. 8 \n☎+7 (495) 756-26-79 \n☎+7 (495) 772-33-99\n🔗www.mia-dent.ru \n🕓Время работы:\nкруглосуточно')
    bot.send_message(message.chat.id, '\n⚕️Узнать прейскурант\n http://www.mia-dent.ru/prices/')
    bot.send_message(message.chat.id, '📍Вы можете проложить маршрут до учреждения, нажав на карту')
    bot.send_location(message.chat.id, latitude=55.798975, longitude=37.3937721)
#####
    bot.send_message(message.chat.id, '💰Стоматология "Волшебная улыбка" \n💎ул. Твардовского, д. 12 \n☎+7 (499) 681-15-31\n🔗http://волшебная-улыбка.рф \n🕓Время работы:\nежедневно: 10:00 - 21:00 \n✅детская стоматология')
    bot.send_message(message.chat.id, '\n⚕️Узнать прейскурант\n ')
    bot.send_message(message.chat.id, '📍Вы можете проложить маршрут до учреждения, нажав на карту')
    bot.send_location(message.chat.id, latitude=55.794073, longitude=37.3953223)
#####

#детские
@bot.message_handler(commands=['det_money'])
def default_test(message):
    bot.send_message(message.chat.id, '💰Театр песни "Фантазия" \nподразделение Центра практической психологии "Эквалайс" \n💎ул. Твардовского, д.4, к.2 \n☎+7 (495) 757 44 43 \n☎+7 (985) 760 59 29\n🔗https://www.psyequal.ru ')
    bot.send_message(message.chat.id, '📍Вы можете проложить маршрут до учреждения, нажав на карту')
    bot.send_location(message.chat.id, latitude=55.79711, longitude=37.3889523)
#####
    bot.send_message(message.chat.id, '💰Студия раннего развития для детей с аутистическими особенностями \nподразделение Центра практической психологии "Эквалайс" \n💎ул. Твардовского, д.4, к.2 \n☎+7 (495) 757 44 43 \n☎+7 (985) 760 59 29\n🔗https://www.psyequal.ru ')
    bot.send_message(message.chat.id, '📍Вы можете проложить маршрут до учреждения, нажав на карту')
    bot.send_location(message.chat.id, latitude=55.79711, longitude=37.3889523)
#####
    bot.send_message(message.chat.id, '💰Логопедический центр "Аксон" \n💎ул. Твардовского, 12 к1 \n☎+7 (499) 137-94-01\n☎+7 (495) 774-55-08\n🔗http://akson2000.ru/ \n🕓Время работы:\nпн-пт: 10:00—19:00')
    bot.send_message(message.chat.id, '\n⚕️Узнать прейскурант\n ')
    bot.send_message(message.chat.id, '📍Вы можете проложить маршрут до учреждения, нажав на карту')
    bot.send_location(message.chat.id, latitude=55.794195, longitude=37.3981263)
#####
    bot.send_message(message.chat.id, '💰Логопедический центр "Детская академия речи" \n💎Строгинский б-р, д. 14, корп. 3, 7 подъезд \n☎+7 (495) 215-23-42 \n☎+7 (495) 758-31-98\n🔗www.logoakademia.ru \n🕓Время работы:\nпн-пт: 09:00—00:00 \nсб: 10:00—15:00')
    bot.send_message(message.chat.id, '\n⚕️Узнать прейскурант\n ')
    bot.send_message(message.chat.id, '📍Вы можете проложить маршрут до учреждения, нажав на карту')
    bot.send_location(message.chat.id, latitude=55.803303, longitude=37.3973733)
#####

############################################

@bot.message_handler(commands=['price_natali'])
def default_test(message):
    bot.send_message(message.chat.id, 'Акушерство и гинекология \n http://www.natalimed.ru/ftpgetfile.php?id=83')
    bot.send_message(message.chat.id, 'Урология \n http://www.natalimed.ru/ftpgetfile.php?id=89')
    bot.send_message(message.chat.id, 'Кардиология и терапия \n http://www.natalimed.ru/ftpgetfile.php?id=84')
    bot.send_message(message.chat.id, 'Специалисты \n http://www.natalimed.ru/ftpgetfile.php?id=85')
    bot.send_message(message.chat.id, 'Гастроэнтерология \n http://www.natalimed.ru/ftpgetfile.php?id=82')
    bot.send_message(message.chat.id, 'Лабораторная диагностика \n http://www.natalimed.ru/ftpgetfile.php?id=62')
    bot.send_message(message.chat.id, 'УЗИ \n http://www.natalimed.ru/ftpgetfile.php?id=88')
    bot.send_message(message.chat.id, 'Отоларингология (ЛОР) \n http://www.natalimed.ru/ftpgetfile.php?id=86')
    bot.send_message(message.chat.id, 'Процедурный кабинет \n http://www.natalimed.ru/ftpgetfile.php?id=69')
    bot.send_message(message.chat.id, 'Офтальмология \n http://www.natalimed.ru/ftpgetfile.php?id=87')
    bot.send_message(message.chat.id, 'Рентгенология \n http://www.natalimed.ru/ftpgetfile.php?id=68')
    bot.send_message(message.chat.id, 'Программы обследования \n http://www.natalimed.ru/programmy-obsledovanija')

@bot.message_handler(commands=['det_free_med'])
def default_test(message):
    bot.send_message(message.chat.id, '🔷 🔷 🔷Перед тобой список бесплатных детских поликлиник в Строгино')
    bot.send_message(message.chat.id, '🔷 🔷 🔷Детская городская поликлиника № 58  ')
    bot.send_message(message.chat.id, 'ул. Твардовского, д. 5, корп. 4\n💎  \nДежурный администратор: \n☎8 (965) 207-47-18 \nСправочная: \n☎8 (495) 756-22-39\nЗапись к специалистам: \n☎8 (495) 539-30-00 \nВызов врача на дом:\n☎8 (495) 758-33-25 \n🔗http://dgp58dzm.ru/')
    bot.send_message(message.chat.id, '📍Вы можете проложить маршрут до учреждения, нажав на карту')
    bot.send_location(message.chat.id, latitude=55.797342, longitude=37.3928013)

@bot.message_handler(content_types=["бесплатно", "бюджетно"])
def default_test(message):
    bot.send_message(message.chat.id, '👉Городская поликлиника № 180 Филиал № 1 (ГП 96) \nул. Кулакова, д. 23 \nСтол справок: \n☎ 84957503971 \nПомощь на дому: \n☎ 84957503978  \nТравматологический пункт: \n☎84957581286 \nВызов неотложной помощи: \n☎84957500111 \nhttp://gp180.mos.ru \nРасаписание врачей по ссылке\nhttp://gp180.mos.ru/content/shedule/f1/')
    bot.send_message(message.chat.id, 'Вы можете проложить маршрут до поликлинки, нажав на карту')
    bot.send_location(message.chat.id, latitude=55.8021665, longitude=37.3940866)
    #поликлиника
    bot.send_message(message.chat.id, '👉Городская поликлиника № 180 Филиал № 2 (ГП 181)')
    bot.send_message(message.chat.id, 'ул. Исаковского, д. 16, корп. 2 \nСтол справок: \n☎ 8(495)758-99-13 \nПомощь на дому: \n☎ 8(495)758-40-59 \nhttp://gp180.mos.ru \nРасаписание врачей по ссылке \nhttp://gp180.mos.ru/content/shedule/f2/')
    bot.send_message(message.chat.id, 'Вы можете проложить маршрут до поликлинки, нажав на карту')
    bot.send_location(message.chat.id, latitude=55.8115728, longitude=37.4053682)
    #поликлиника
    bot.send_message(message.chat.id, '👉Женская консультация')
    bot.send_message(message.chat.id, 'ул. Катукова, д. 5 \nСтол справок: \n☎ 8(495)750-41-84 \nhttp://gp180.mos.ru \nРасаписание врачей по ссылке \nhttp://gp180.mos.ru/content/shedule/f3/')
    bot.send_message(message.chat.id, 'Вы можете проложить маршрут до поликлинки, нажав на карту')
    bot.send_location(message.chat.id, latitude=55.8128917, longitude=37.3951224)
##############
    bot.send_message(message.chat.id, '👉Стоматологическая поликлиника № 60')
    bot.send_message(message.chat.id, 'ул. Твардовского, д. 27\nСтол справок: \n☎ +7 (495) 756-69-98 \nhttp://sp60.mos.ru \nРасаписание врачей по ссылке \nhttp://sp60.mos.ru/content/shedule/')
    bot.send_message(message.chat.id, 'Вы можете проложить маршрут до поликлинки, нажав на карту')
    bot.send_location(message.chat.id, latitude=55.797848, longitude=37.4044913)
#############
    bot.send_message(message.chat.id, '👉Детская городская поликлиника № 58  ')
    bot.send_message(message.chat.id, 'ул. Твардовского, д. 5, корп. 4\n💎  \nДежурный администратор: \n☎8 (965) 207-47-18 \nСправочная: \n☎8 (495) 756-22-39\nЗапись к специалистам: \n☎8 (495) 539-30-00 \nВызов врача на дом:\n☎8 (495) 758-33-25 \n🔗http://dgp58dzm.ru/')
    bot.send_message(message.chat.id, '📍Вы можете проложить маршрут до учреждения, нажав на карту')
    bot.send_location(message.chat.id, latitude=55.797342, longitude=37.3928013)

@bot.message_handler(content_types=["стоматология", "стоматолог", "зубы", "зуб", "стаматология", "стаматолог"])
def default_test(message):
    bot.send_message(message.chat.id, '👉Стоматологическая поликлиника № 60 (бесплатная)')
    bot.send_message(message.chat.id, 'ул. Твардовского, д. 27\nСтол справок: \n☎ +7 (495) 756-69-98 \nhttp://sp60.mos.ru \nРасаписание врачей по ссылке \nhttp://sp60.mos.ru/content/shedule/')
    bot.send_message(message.chat.id, 'Вы можете проложить маршрут до поликлинки, нажав на карту')
    bot.send_location(message.chat.id, latitude=55.797848, longitude=37.4044913)

@bot.message_handler(content_types=["дура", "сука", "блядь", "хуй"])
def default_test(message):
    bot.send_message(message.chat.id, "Не надо материться!")


if __name__ == '__main__':
    bot.polling(none_stop=True)
