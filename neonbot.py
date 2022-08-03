import telebot
import random
from telebot import types
from telegram import Bot
from telegram import Update
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler


from config import API_KEY

bot = telebot.TeleBot(API_KEY)
#
# @bot.message_handler(commands=['start'])
# def user_start(message):
#     if message.text == 'start':
#         msg = "Пользователь {} {} начал общение с NeonMBot \"{}\".".format(message.from_user.username, message.from_user.id)
#         bot.send_message('202908551', msg)
#         id_list.add(message.from_user.id)
#         print(id_list)


@bot.message_handler(commands=['start'])
def do_start(message):
    # if message.text == 'start':
    #     msg = "Пользователь {} {} начал общение с NeonMBot \"{}\".".format(message.from_user.username, message.from_user.id)
    #     bot.send_message('202908551', msg)
    #     id_list.add(message.from_user.id)
    #     print(id_list)
    # тут пытаюсь уведомлять, когда новый пользователь начинает общение с ботом, но это не работает/
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Заказать вывеску💡')
    item2 = types.KeyboardButton('Доставка📦')
    item3 = types.KeyboardButton('Контакты📍')
    item4 = types.KeyboardButton('Примеры работ🧩')
    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id,
                     text=f'Привет, {message.from_user.first_name}!\n'
                          f'"Moscow.neon" - это молодая, быстро развивающая компания по производству и продаже неоновых вывесок.'
                          f'Благодаря собственному производству и штату квалифицированных специалистов, у нас есть возможность предлагать цены до 40% ниже рынка!'
                          f'Здесь ты сможешь получить информацию по своему запросу и новости нашего магазина!',
                     reply_markup = markup)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'Заказать вывеску💡':
            bot.send_message(message.chat.id, 'Чтобы передать свои пожелания нашим мастерам, опишите идею, цвет и размер будущей вывески. Также, пожалуйста, напишите, как к вам можно обращаться и контактный номер телефона.')
            # то, что не отображается имя пользователя, пытаюсь решить способом прошения самого пользователя оставить свои контакты
            bot.register_next_step_handler(message, thnk_step)
        elif message.text == 'Доставка📦':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Способы доставки🛺')
            item2 = types.KeyboardButton('Стоимость доставки💸')
            item3 = types.KeyboardButton('Самовывоз🚘')
            item4 = types.KeyboardButton('Как отследить заказ?👀')
            item5 = types.KeyboardButton('Как быстро изготавливается заказ?⏳')
            item6 = types.KeyboardButton('Назад')
            markup.add(item1, item2, item3, item4, item5, item6)
            bot.send_message(message.chat.id, 'Здесь можно узнать подробную информацию о доставке. Выберите интересующий вас раздел.', reply_markup = markup)
        elif message.text == 'Контакты📍':
            bot.send_message(message.chat.id, 'Мы находимся по адресу: 109544, г.Москва, ул.Рабочая, д.91, стр.1.\n'
                                              'Телефон: +7 (977) 000-79-84 \n'
                                              'Email: help@moscowneon.ru \n'
                                              'С радостью ожидаем тебя в будние дни с 11.00 до 20.00')
        elif message.text == 'Способы доставки🛺':
            bot.send_message(message.chat.id, 'Заказы мы отправляем курьерской службой либо СДЭК (ПВЗ).'
                                              'Курьерская служба доступна по Москве и Московской области.'
                                              'СДЭК доставляет в любой уголок РФ. Благодаря ей любой житель России сможет получить вывески от Moscow Neon.'
                                              'Каждый заказ доставляется с разным промежутком времени в зависимости от удаленности вашего города от Москвы.')
        elif message.text == 'Стоимость доставки💸':
            bot.send_message(message.chat.id, 'Курьерская служба по Москве (в пределах МКАД) - 800 рублей;\n'
                                              'Курьерская служба по Московской области - 1200 рублей;\n\n'
                                              'СДЭК (ПВЗ) по Москве - 600 рублей;\n'
                                              'СДЭК (ПВЗ) по Московской области - 800 рублей;\n'
                                              'СДЭК по России от 2000 до 6000 рублей в зависимости от удаленности вашего города от Москвы.')
        elif message.text == 'Самовывоз🚘':
            bot.send_message(message.chat.id, 'Забрать заказ можно бесплатно с нашего склада после подтверждения о его готовности нашим менеджером '
                                              'по адресу: г. Москва, м. Площадь Ильича, ул. Рабочая 91 с1 '
                                              '(в будние дни с 11.00 до 20.00).\n '
                                              'Арендованные вывески можно получить в день оформления заказа.')
        elif message.text == 'Как отследить заказ?👀':
            bot.send_message(message.chat.id, 'Если Ваш заказ был отправлен через СДЭК ПВЗ, Вы получите уведомление о готовности заказа к выдаче. '
                                              'Если же Вы хотите отследить заказ до момента готовности к выдаче, напишите любым удобным способом нам, '
                                              'мы вышлем Вам уведомление с трек-номером для отслеживания. '
                                              'Введите его на официальном сайте службы доставки – и контролируйте весь путь вашей посылки')
        elif message.text == 'Как быстро изготавливается заказ?⏳':
            bot.send_message(message.chat.id, 'Вывески изготавливаются индивидуально для каждого Заказчика, '
                                              'срок изготовления 1 - 3 дня в зависимости от загруженности сотрудников.')
        elif message.text == 'Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Заказать вывеску💡')
            item2 = types.KeyboardButton('Доставка📦')
            item3 = types.KeyboardButton('Контакты📍')
            item4 = types.KeyboardButton('Примеры работ🧩')
            markup.add(item1, item2, item3, item4)
            bot.send_message(message.chat.id, 'Назад', reply_markup=markup)
        elif message.text == 'Примеры работ🧩':
            menu1 = types.InlineKeyboardMarkup()
            menu1.add(types.InlineKeyboardButton(text='Намекнуть на подарок', callback_data='first'))
            bot.send_message(message.chat.id, 'https://i.pinimg.com/236x/95/8f/86/958f8688ea5f7235b78e52166bf7c025.jpg')
            bot.send_message(message.chat.id, 'Пример вывески, реализованной нашими мастерами. Нам не страшны любые сложности, мы головой отвечаем за качество исполнения и даем гарантию изделию на год. \n Чтобы узнать подробности, оставьте сообщение в меню "Заказать вывеску"')
            if message.text == 'Намекнуть на подарок':
                bot.register_next_step_handler(message, gift1_step)
            # del pic_list_ok[0]
#         TypeError: 'NoneType' object is not subscriptable/ Возникает такая ошибка. Почему?? Если тип определен вроде как

@bot.message_handler(content_types=['text'])
def thnk_step(message):
    # if message.chat.type == 'private':
    #     if message == 'Заказать вывеску💡' or 'Доставка📦' or 'Контакты📍':
    bot.send_message(message.chat.id, 'Спасибо за заказ. Мы сохранили ваши пожелания. В ближайшее время наш менеджер свяжется с Вами для обсуждения деталей.\n'
                                        'Мы гарантируем 100% соответствие макета и вывески.'
                                        'На каждое изделие предоставляем длительную гарантию на 1 год независимо от Вашего местонахождения.')
    msg = "Пользователь {} {} написал \"{}\".".format(message.from_user.username, message.from_user.id, message.text)
    bot.send_message('202908551', msg)

@bot.callback_query_handler(func=lambda call: True)
def gift1_step(message):
    if call.data == 'first':
        bot.send_message(message.chat.id, 'Пожалуйста, напиши id адресата и мы отправим ему намек ;)')
        bot.register_next_step_handler(message, gift2_step)

@bot.callback_query_handler(func=lambda call: True)
def gift2_step(message):
    msg = f'Мы знаем, что ваш близкий человек мечтает об этом подарке! Только тссс..., https://i.pinimg.com/236x/95/8f/86/958f8688ea5f7235b78e52166bf7c025.jpg'
    bot.send_message(message, msg)

# имя пользователя отображается как None. Как сделать, чтобы отображалось нормально? Айди пользователя отображается корректно

# функция отправки ботом сообщений с примерами  работ, должна быть реализована от времени суток
# def mailing(message):
#     for id in id_list:
#         bot.send_message(message.chat.id, pic_list_ok[0])
#         bot.send_message(message.chat.id, 'Пример вывески, реализованной нашими мастерами. Нам не страшны любые сложности, мы головой отвечаем за качество исполнения и даем гарантию изделию на год. \n Чтобы узнать подробности, оставьте сообщение в меню "Заказать вывеску"')
#     del pic_list_ok[0]

pic_list = ['https://i.pinimg.com/originals/8e/a8/fc/8ea8fc978efeef8203336061346f1633.jpg',
            'https://i.pinimg.com/280x280_RS/14/60/10/146010fe72b47948ea7bd1ab1461de8c.jpg',
            'https://i.pinimg.com/236x/54/fd/08/54fd08a89210b567b84dca0e6b508ebc.jpg',
            'https://i.pinimg.com/236x/a7/f6/3f/a7f63f1835be4bec69cd34f4b99eff27.jpg',
            'https://i.pinimg.com/236x/ff/f7/fe/fff7fedf4ebd444ea8e53ddcf8864736.jpg',
            'https://i.pinimg.com/236x/64/1e/0a/641e0a3a152aec1e12ec54e962b3f282.jpg',
            'https://i.pinimg.com/236x/13/07/f7/1307f791fc002692f19de5b82309f870.jpg',
            'https://i.pinimg.com/236x/75/cb/20/75cb208b3b25ab7e34dfe9ce797abe80.jpg',
            'https://i.pinimg.com/236x/5f/14/6d/5f146d3c7c11222298c811be4329433e.jpg',
            'https://i.pinimg.com/236x/48/11/ba/4811ba855081c86617ba08731f34ed0f.jpg',
            'https://i.pinimg.com/236x/c6/57/7d/c6577d190f245d293049d06d343e799d.jpg',
            'https://i.pinimg.com/236x/75/3e/c3/753ec31eff1625b41ef9a0b928ce7110.jpg',
            'https://i.pinimg.com/236x/18/41/ec/1841ecf9755ceb9bd9cc3c6dfc763435.jpg',
            'https://i.pinimg.com/236x/d2/d8/f2/d2d8f2a98e879637d4bc41fa17364c8a.jpg',
            'https://i.pinimg.com/236x/37/95/d0/3795d0fa681b42dea120cc21a5b6313d.jpg',
            'https://i.pinimg.com/236x/f6/c0/b9/f6c0b9ac9829fbf89cd46e61eedcde7c.jpg',
            'https://i.pinimg.com/236x/9e/31/76/9e317680b3898de3cac5f1ab5fbe0d86.jpg',
            'https://i.pinimg.com/236x/f2/f2/e9/f2f2e92284c051dbf201e980501767ea.jpg',
            'https://i.pinimg.com/236x/8e/34/76/8e3476555a58da3d932b3239bd8873d5.jpg',
            'https://i.pinimg.com/236x/54/52/d9/5452d9b2f7b075290fe290a0c9e122e6.jpg',
            'https://i.pinimg.com/236x/49/ed/41/49ed415d2c0207374ab80942ecc63ccd.jpg',
            'https://i.pinimg.com/236x/fe/d7/b1/fed7b145e74f8b7d5b84cdb03682e0d7.jpg',
            'https://i.pinimg.com/236x/14/d7/2f/14d72f30dcbeb24ee7a846fe85eecc73.jpg',
            'https://i.pinimg.com/236x/c2/50/68/c2506874955e28290ec1bc7b202d357d.jpg',
            'https://i.pinimg.com/236x/a8/05/1e/a8051e46a5cdc16edc2116a58e218768.jpg',
            'https://i.pinimg.com/236x/95/8f/86/958f8688ea5f7235b78e52166bf7c025.jpg',
            'https://i.pinimg.com/236x/dd/9f/22/dd9f22aaa8c1c08cc2aaa4a7b0608962.jpg',
            'https://i.pinimg.com/236x/6b/85/19/6b85193f09c9556aafdc000d447cd0cc.jpg']
#
# pic_list_o = random.shuffle(pic_list)
# pic_list_ok = list(pic_list_o)
# # TypeError: 'NoneType' object is not iterable/ АААААААААААААААААААААААААААААААААА??????????? ПОЧЕМУ?!
# id_list = set()



bot.enable_save_next_step_handlers(delay=2)

bot.load_next_step_handlers()

bot.polling(none_stop=True)
# def main():
#     bot = Bot(
#         token=API_KEY,
#     )
#     updater = Updater(
#         bot=bot,
#     )
#
#     # start_handler = CommandHandler('start', do_start)
#     #
#     # updater.dispatcher.add_handler(start_handler)
#     #
#     # updater.start_polling()
#     # updater.idle()
#
# if __name__ == '__main__':
#     main()

