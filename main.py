import telebot
import random


    # Замени 'TOKEN' на токен твоего бота
    # Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot("8576505057:AAEL0FWMAh5onzAbs-Bvqm2vhHRw5q1HuHw")
random_facts = ['За последние 150 лет средняя температура на планете выросла примерно на 1,1C.','Уровень Мирового океана поднялся на 20 см из‑за таяния ледников и нагрева воды.','Концентрация CO₂ в атмосфере превысила доиндустриальный уровень на 50 % (2022 год).','20 самых тёплых лет в истории наблюдений пришлись на период с 1981 года.','Ледники Большого Кавказа за 2000–2020 годы сократились почти на четверть.','Экстремальные погодные явления (жара, наводнения, пожары) стали чаще и интенсивнее.','Вечная мерзлота занимает до 65 % территории России — её таяние угрожает инфраструктуре.','К концу века температура может вырасти на 2,4–4,4C, если не сократить выбросы.']

info = {
    '/start':'приветствие',
    '/hello':'приветствие',
    '/random_facts':'выводит рандомный факт о глобальном потеплении',
    '/global_warming':'выводит информацию что такое глобальное потепление'
}
error = {'start','hello','random_facts','global_warming'}


@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, f'Привет! Я бот {bot.get_me().first_name}!')

@bot.message_handler(commands=['info', 'information'])
def send_info(message):
    text = "📋 Доступные команды:\n\n"
    for cmd, desc in info.items():
        text += f"🔹 {cmd}\n   {desc}\n\n"
    bot.reply_to(message, text)

@bot.message_handler(commands=['random_facts'])
def random_fact(message):
    fact = random.choice(random_facts)
    bot.reply_to(message, f'Вот один рандомный факт о глобальном потеплении: {fact}!')

@bot.message_handler(commands = ['global_warming'])
def global_warming(message):
    bot.reply_to(message,'Что такое глобальное потепление:Из‑за добычи ископаемого топлива в атмосферу ежегодно попадают миллиарды тонн CO₂. По данным ВМО (2019), температура уже превысила доиндустриальный уровень минимум на 1 °C. Парижское соглашение (2015) ставит цель удержать рост температуры ниже 2 °C, желательно — в пределах 1,5 °C. Без сокращения выбросов к 2100 году потепление может достичь 3 °C. Таяние ледников повышает уровень моря — под угрозой затопления окажутся прибрежные города, где живут сотни миллионов человек.')

def command_exists(command: str) -> bool:
    return command.strip().lower().lstrip("/") in error

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if command_exists(message.text):
        bot.reply_to(message, "Такая команда существует ✅")
    else:
        bot.reply_to(message, "Такой команды нет, обратитесь к функции /info ❌")

bot.polling()


