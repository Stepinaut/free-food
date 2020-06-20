# создание базы данных и таблиц для FREEFOOD

# импорт библиотек
import sqlite3
import os

db_file = open("db.sqlite", 'w')
db_file.close()

vegetables = ['абельмоша', 'ангурий', 'арракача', 'аррорут', 'артишок', 'базелла', 'базилик',
              'бамия', 'батат', 'белокопытник', 'капуста', 'бок-ча',
              'брокколи', 'брюква', 'буряк', 'габлиция', 'горох', 'горчица', 'дайкон', 'жерух',
              'зелень', 'ипомея', 'кабачок', 'каперс', 'картофель', 'катран', 'кислица', 'козлобородник',
              'колокольчик', 'колоцинт', 'кольраби', 'корнишон', 'кукуруза', 'лагенарий', 'латук',
              'лук', 'лук-порей', 'лук-шалот', 'майоран', 'мак', 'мелотрия', 'морковь',
              'настурция', 'нут', 'горох', 'огурец', 'пак-ча', 'капуста', 'пастернак', 'патиссон',
              'петрушка', 'плантан', 'радиккьо', 'ревень', 'редис', 'редька', 'репа',
              'романеско', 'руккола', 'салат', 'сарах', 'свёкла', 'сельдерей', 'спаржа',
              'томат', 'томаты', 'топинамбур', 'трихозант', 'турнепс', 'укроп', 'уллюко',
              'фенхель', 'хикама', 'хрен', 'чабёр', 'черри', 'помидор',
              'чеснок', 'чистец', 'чуфа', 'шнитта-лука', 'шпинат', 'щавель', 'эстрагон', 'якон', 'ям']

fruits = ['абиу', 'абрикос', 'авокадо', 'айва', 'аки', 'алиберция', 'алыча', 'амбарелла', 'орех', 'ананас', 'аннона',
          'черимола', 'крыжовник', 'апельсин', 'арабика', 'араз', 'арахис', 'арбуз', 'астрокариум',
          'тамаринд', 'бакау', 'баклажан', 'банан', 'баобаб', 'барбадин', 'гранадилла', 'вишня', 'яблоко', 'баэль',
          'сапот', 'бергамот', 'билимбить', 'бирсоним', 'блигия', 'фрукт', 'боярышник', 'сердце', 'вампить', 'ваниль',
          'виноград', 'воаванг', 'генипа', 'гибискус', 'гнетум', 'гнемона', 'слива', 'голуба', 'квандонг',
          'горлянка', 'гранадилла', 'маракуйа', 'барбадин', 'гранат', 'грейпфрут', 'грумичам', 'груша', 'гуайява',
          'гуарана', 'давидсония', 'пальчик', 'джекфрут', 'калебас', 'дук', 'дуриана',
          'дерево', 'дыня', 'жаботикаб', 'зизифус',
          'боб', 'инжир', 'миндаль', 'какао', 'кактус', 'каламондин',
          'калин', 'канариум', 'карамбола', 'кас', 'квини', 'кепель', 'кетамбилл', 'кивано', 'киви',
          'клементина', 'кокколоб', 'кокос', 'корилла', 'кранжи', 'кумквата',
          'купуасу', 'курбарил', 'горошек', 'лайм', 'лангсат', 'лансиум', 'леуцена',
          'либерик', 'ликание', 'лимон', 'мейер', 'осина', 'личить', 'лобия',
          'мангустан', 'лох', 'лукума', 'луть', 'люффа', 'маболо', 'макадамия',
          'тыква', 'мальпигия', 'мамметь', 'мамончилло', 'лайм', 'манго',
          'мангостан', 'мандарин', 'манилкара', 'маракуйя', 'плод', 'марула',
          'маш', 'мелинжо', 'моква', 'момбин', 'момордик', 'моринд', 'мунд',
          'мушмула', 'наранхилла', 'ням-нь', 'нектарин', 'подвид', 'персика', 'кешью', 'пальма', 'катеху',
          'папайя', 'папеда', 'паприка', 'пара-гуайява',
          'паркия', 'пассифлора', 'пекуи', 'пепино', 'перец', 'персик', 'питайя', 'питомба',
          'помело', 'померанец', 'помпельмус', 'плод', 'путерия', 'пуласан', 'ракум-салакка',
          'рамбай', 'рамбутан', 'робуста', 'роллиния', 'салакка', 'сантол',
          'саподилла', 'сатсума', 'свитя', 'сизигиум', 'аквеум', 'ямбоз', 'какаду',
          'сонсоя', 'соя', 'фасоль', 'страстоцвет', 'такако', 'тамарилло', 'танжерин', 'терминалия',
          'катапп', 'тукума', 'фейхоа',
          'ферония', 'физалис', 'филлантус', 'финик', 'флакурция', 'хурма',
          'циклантёр', 'цукини', 'чайот', 'чампедак', 'черешня', 'чили',
          'чилибуха', 'чупа', 'яблоко-кадить', 'яботикаб', 'ятоба']

breads = ['хлебобулочный', 'батскай', 'булочка', 'бейглый', 'брецель', 'бриошь', 'бурекас', 'выборгский',
         'крендель', 'выпечка', 'галета', 'гаш', 'далеб', 'дампфнудель', 'кайзерка', 'булка', 'калорийный', 'каттам',
         'краковский', 'бублик', 'краффина', 'круассан', 'лакума', 'лахох', 'липпский', 'соломенный', 'лукумадес',
         'мейсенский', 'фуммель', 'мигелитос', 'мука', 'грэм', 'пампушка', 'панфорт', 'рогалик',
         'роть-буайя', 'рулет', 'мак', 'сайка', 'хлеб', 'сангак', 'семл', 'симит', 'гренок', 'слоёный',
         'тесто', 'сметанник', 'смультринг', 'солёный', 'палочка', 'сушка', 'таралли', 'твейбак', 'фолара',
         'францбрётхен', 'цельнозерновый', 'шоколатин', 'эклсскай', 'слойк']

sweets = ['халва', 'козинаки', 'лукум', 'нуга', 'цукаты', 'чурчхела', 'грильяж', 'карамель', 'ирис', 'леденец',
         'помадка', 'мороженое', 'помадка', 'марципан', 'шоколад', 'конфета', 'сырок', 'йогурт', 'торт', 'пирожное',
         'вафли', 'печенье', 'пирог', 'ватрушка', 'пончик', 'бублик', 'варенье', 'мармелад', 'джем', 'желе', 'безе',
         'меренги', 'кремы', 'муссы', 'зефир', 'пастила', 'пряник', 'кекс', 'эклер', 'повидло', 'крем',
         'самбук', 'суфле', 'маффин', 'кулич', 'бабы', 'леденец', 'жвачка', 'чупа-чупс', 'батончик', 'пудинг',
         'тирамису', 'чуррос', 'варенье', 'мёд', 'мед']

waters = ['чай', 'кофе', 'сок', 'сидр', 'морс', 'вода', 'лимонад', 'фреш', 'каркаде', 'щербет', 'ласси',
          'массала', 'чампуррадо', 'нектар', 'моктейль', 'смузи', 'напиток', 'глинтвейн', 'коктейль', 'молоко',
          'компот', 'эль', 'смузи', 'кефир', 'пунш', 'кисель', 'сыворотка', 'какао', 'квас', 'ряженка', 'каркаде',
          'мате', 'сбитень', 'отвар', 'милкшейк', 'латте', 'сироп', 'экстракт']

meats = ['говядина', 'курятина', 'баранина', 'свинина', 'конина', 'козлятина', 'верблюжатина']

# подключение к db.sqlite
conn = sqlite3.connect("db.sqlite")
cursor = conn.cursor()

# создание таблицы в db.sqlite
cursor.execute("""CREATE TABLE users (id INTEGER PRIMARY KEY, city TEXT, categories TEXT, groups TEXT, status INTEGER)""")
cursor.execute("""CREATE TABLE foods (name TEXT, category TEXT)""")
cursor.execute("""CREATE TABLE cities (name TEXT)""")

# открываем файл city.txt
fcity = open('cities.txt', 'r', encoding='windows-1251')
city = fcity.read().splitlines()  # считываем файл с городами построчно

for i in city:
    query = "INSERT or REPLACE INTO cities VALUES ('{0}')".format(i)
    cursor.execute(query)

for vegetable in vegetables:
    query = """INSERT INTO foods (name, category)
        VALUES ('{0}', '{1}')
        """.format(vegetable, "Овощи")
    cursor.execute(query)

for fruit in fruits:
    query = """INSERT INTO foods (name, category)
        VALUES ('{0}', '{1}')
        """.format(fruit, "Фрукты")
    cursor.execute(query)

for bread in breads:
    query = """INSERT INTO foods (name, category)
        VALUES ('{0}', '{1}')
        """.format(vegetable, "Сдобное")
    cursor.execute(query)

for sweet in sweets:
    query = """INSERT INTO foods (name, category)
        VALUES ('{0}', '{1}')
        """.format(sweet, "Сладости")
    cursor.execute(query)

for water in waters:
    query = """INSERT INTO foods (name, category)
        VALUES ('{0}', '{1}')
        """.format(water, "Напитки")
    cursor.execute(query)

for meat in meats:
    query = """INSERT INTO foods (name, category)
        VALUES ('{0}', '{1}')
        """.format(meat, "Мясо")
    cursor.execute(query)

# закрываем соединение с db.sqlite
conn.commit()