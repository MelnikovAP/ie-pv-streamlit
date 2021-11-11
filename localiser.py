langs = ["RU","ENG"]

td = {
    'name': {
        'ENG':'PV cloud model',
        'RU':'Солнечная энергетика',
    },
    'sidebar_selector': {
        'ENG':'Choose the work: ',
        'RU':'Выберете работу: ',
    },
    'works': {
        'ENG': [
                'Introduction',
                'Work #1: I-V curves', 
                'Work #2: Influence of different light conditions on the solar cell work', 
                'Work #3: Influence of temperature on the solar cell work',
                'Further reading'
                ],
        'RU': [
                'Введение', 
                'Работа №1: Характеристические кривые солнечных панелей', 
                'Работа №2: Влияние различных световых условий на выработку солнечных панелей', 
                'Работа №3: Влияние температуры на выработку солнечных панелей',
                'Полезная литература'
                ],
    },
    'work0': {
        'introduction':{
            'ENG':[ '''
                    to translate
                    ''',
                    '''
                    to translate
                    ''',
                    '''
                    to translate
                    ''',
                ],
            'RU': [ '''
                    Первыми живыми организмами на земле, которые научились напрямую поглощать 
                    солнечную энергию и накапливать её, были, скорее всего, растения. Энергию, 
                    которую переносит солнечный свет от единственной звезды нашей системы – 
                    Солнца, – растения используют при фотосинтезе, улавливая углекислый газ 
                    из атмосферы и возвращая в неё кислород. Углерод при этом остается в 
                    растении, формирую его *«зелёную массу»*. Но солнечная энергия преобразуется 
                    не только в энергию химических связей в растениях. Практически вся энергия 
                    на нашей планете так или иначе связана с солнечной активностью, и человек 
                    научился преобразовывать её в электрическую.
                    ''',
                    '''
                    Из-за разницы температур воздушных масс возникает разность давления и 
                    появляется ветер, который может крутить лопасти ветрогенератора. Нагревая 
                    землю и водные ресурсы планеты, солнце в атмосферу выпаривает огромное 
                    количество воды, которая переносится на сотни и тысячи километров, 
                    выпадая в виде осадков или замерзая в ледниках. Потоки воды образуют 
                    реки, а человек снова извлекает из этого пользу, используя гидроэлектростанции.
                    ''',
                    '''
                    С конца **XIX века**, когда учёные открыли фотоэлектрический эффект, у 
                    человечества появился способ прямого преобразования солнечного света в 
                    электричество. Важность технологии получения электричества напрямую от 
                    солнечного света и понимание принципов, лежащих в её основе, нашли своё 
                    отражение и в, пожалуй, самой известной награде в области науки – 
                    Нобелевской премии. В течение **XX века** различные учёные, работы 
                    которых важны для данной технологии, несколько раз становились лауреатами 
                    Нобелевской премии. К концу **50-х годов XX века** были разработаны солнечные 
                    панели, которые позволяли получать электроэнергию в достаточном количестве 
                    для работы маломощных устройств. Практически сразу же солнечные панели нашли 
                    своё применение в разнообразных космических аппаратах. В этой области они 
                    оказались незаменимыми. К началу **XXI века** технологии солнечных панелей 
                    развились достаточно для того, чтобы найти себе промышленное применение в 
                    земных условиях. По состоянию на сегодняшний день есть отдельные регионы 
                    например, некоторые территории Индии), где строительство электростанции, 
                    на солнечных панелях, является самым дешевым и эффективным способом 
                    электрификации местности. Даже в нашей, казалось бы, достаточно северной 
                    и не самой солнечной стране введён в эксплуатацию целый ряд солнечных электростанций.
                    ***
                    '''
                ]
        },
        'basics':{
            'ENG': [ '''
                    ### The principle of solar cell operation  
                    ''',
                    '''
                    Let's take a look at how a solar cell works.   
                    ''',
                    '''
                    Figure 1. Schematic diagram of a solar cell
                    ''',
                ],
            'RU': [ '''
                    ### Принцип работы солнечной панели  
                    ''',
                    '''
                    Давайте разберём, как же работает солнечная панель.    
                    ''',
                    '''
                    Рисунок 1. Принципиальная схема фотоэлемента
                    ''',
                ],
        },
        'theory':{
            'ENG': [ '''
                    to translate  
                    ''',
                    '''
                    to translate     
                    ''',
                    '''
                    to translate
                    ''',
                    '''
                    to translate
                    ''',
                ],
            'RU': [ '''
                    Фотоэлемент на основе полупроводников состоит из двух очень тонких слоёв  
                    (чтобы они были проницаемы для фотонов) толщиной обычно  **~0,2 мм** с 
                    разным типом проводимости, совместно образующих так называемый *p-n-переход*. 
                    К слоям с разных сторон подведены металлические контакты, которые подключены 
                    к внешней цепи. Роль катода играет слой с *n-проводимостью* (применяется 
                    материал с избытком валентных электронов, то есть характеризуемый электронной 
                    проводимостью), роль анода – *p-слой* (материал с дырочной проводимостью; 
                    «дырка» – это квазичастица, в данном контексте это условное «место» в веществе, 
                    где нет электрона, но в котором электрон может оказаться; направленное движение 
                    электронов, когда они занимают такие «свободные» места, принято называть 
                    электрическим током в веществе с дырочной проводимостью). 
                    ''',
                    '''
                    При поглощении фотона в веществе может появится «пара» - «валентный» электрон 
                    и «дырка». Упрощённо можно считать, что при поглощении фотона его энергия 
                    идет на то, чтобы «выбить» электрон из того «места», которое он занимал в 
                    веществе, в результате чего и образуется такая «пара». На границе внутри 
                    *p-n-перехода* есть небольшое электрическое поле. Такой эффект имеет место 
                    при контакте между любыми двумя веществами и в случае проводников называется 
                    контактной разностью потенциалов. Оказавшись в области, где действует такое 
                    электрическое поле, «пара» может «распасться» и под действием электрического 
                    поля электрон и «дырка» окажутся по разные стороны от границы.
                    ''',
                    '''
                    В результате такого процесса в *n-* и *p-областях* накапливаются электроны 
                    и дырки соответственно, что означает, что между этими областями есть разность 
                    потенциалов. Замкнув цепь с помощью металлических контактов и внешней цепи, 
                    можно получить электрический ток.
                    ''',
                    '''         
                    Величина потенциала, достигаемая на одном фотоэлементе на основе кремния, 
                    маленькая и составляет **~0,5 В**, а сила тока через фотоэлемент изменяется 
                    пропорционально его площади и количеству поглощённых им фотонов. Для получения 
                    солнечных панелей с достаточным для практических целей напряжением единичные 
                    фотоэлементы соединяют последовательно в нужном количестве (обычно несколько 
                    десятков элементов), а для повышения силы тока параллельно или сразу производят 
                    фотоэлемент с большой площадью поверхности. Таким образом, комбинацией соединений 
                    можно добиться требуемых значений силы тока и напряжения, а следовательно, и мощности. 
                    ***
                    ''',
                ],
        },
        'what_next':{
            'ENG':[ '''
                    ### Further steps
                    ''',
                    '''
                    Please select a work from the sidebar.
                    Recommended reference list and useful web-links can be found in the "Further reading" tab.
                    ''',
                ],
            'RU':[  '''
                    ### Дальнейшие шаги
                    ''',
                    '''
                    Пожалуйста, выберете работу на панели слева.  
                    Рекомендуемый список литературы и полезные web-ресурсы можно найти во вкладке «Полезная литература».
                    ''',
                ],
        },
    },
    'work1': {
        'sidebar_subheader':{
            'ENG':'Model parameters',
            'RU':'Параметры модели',
        },
        'sidebar_selectbox':{
            'ENG':'Choose the solar panel: ',
            'RU':'Выберете солнечную панель: ',
        },
        'sidebar_button':{
            'ENG':'Calculate',
            'RU':'Расчёт',
        },
        'introduction':{
            'ENG':['''
                    ### Introduction and theory basics
                    ''',
                    '''
                    The main characteristic of solar cell is current-voltage characteristic or I-V curve (IVC)
                    ''',
                    '''
                    to translate
                    ''',
                    '''
                    to translate
                    ''',
                    '''
                    to translate
                    ''',

            ],
            'RU':[ '''
                    ### Введение и элементы теории  
                    ''',
                    '''
                    Основной характеристикой солнечных панелей является их вольт-амперная характеристика (ВАХ).
                    ''',
                    '''
                    **Вольт-амперной характеристикой (ВАХ)** называют функцию (а также её график), 
                    задающую зависимость тока, протекающего через двухполюсник, от напряжения на нём. 
                    Двухполюсником называют любой элемент электрической цепи, содержащий два контакта 
                    для соединения с другими электрическими цепями.  
                    ''',
                    '''
                    Основной рабочей характеристикой солнечной батареи является максимальная мощность, 
                    которую выражают в Ваттах (Вт). Эта характеристика показывает выходную мощность 
                    батареи в оптимальных условиях: солнечном излучении *1 кВт/м²*, температуре окружающей 
                    среды 25 °C, стандартизованном солнечном спектре АМ1,5 (солнечный спектр на широте 45°). 
                    В обычных условиях достичь таких показателей удается крайне редко, т.к. освещенность ниже, 
                    а модуль нагревается выше (до 60–70 °C).
                    ''',
                    '''
                    К характеристикам солнечных панелей также относятся следующие:  
                    - **Напряжение открытой цепи** − это максимальное напряжение, создаваемое солнечным элементом, 
                    возникающее при нулевом токе. Оно равно прямому смещению, соответствующему изменению напряжения 
                    p–n-перехода при появлении светового тока. Напряжение холостого хода солнечного элемента мало 
                    меняется при изменении освещенности. 
                    - **Ток короткого замыкания** − это ток, протекающий через солнечный элемент, когда напряжение 
                    равно нулю (то есть когда солнечный элемент замкнут накоротко). Ток короткого замыкания можно 
                    считать максимальным током, который способен создать солнечный элемент. Кроме того, он прямо 
                    пропорционально зависит от интенсивности света.
                    - **Фактор заполнения** - параметр, который в сочетании с напряжением холостого хода и током 
                    короткого замыкания определяет максимальную мощность солнечного элемента. Он вычисляется, 
                    как отношение максимальной мощности солнечного элемента к произведению напряжения холостого 
                    хода и тока короткого замыкания. Фактор заполнения ВАХ является одним из основных параметров, 
                    по которому можно судить о качестве фотоэлектрического преобразователя. Чем больше коэффициент 
                    заполнения ВАХ, тем меньше потери в элементе из-за внутреннего сопротивления.
                    - **Коэффициент полезного действия (КПД)** является самым распространенным параметром, по которому 
                    можно сравнить производительность двух солнечных элементов. Он определяется как отношение мощности, 
                    вырабатываемой солнечным элементом, к мощности падающего солнечного излучения. Кроме собственно 
                    производительности солнечного элемента, **КПД** также зависит от спектра и интенсивности падающего 
                    солнечного излучения и температуры солнечного элемента. Поэтому для сравнения двух солнечных 
                    элементов нужно тщательно выполнять принятые стандартные условия. КПД солнечного элемента 
                    определяется как часть падающей энергии, преобразованной в электричество.
                    ''',
            ]
        }

    },
    'work2': {
        
    },
    'work3': {
        
    },
    'work4': {
        
    }
}



