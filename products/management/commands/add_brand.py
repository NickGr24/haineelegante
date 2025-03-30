from django.core.management.base import BaseCommand
from products.models import Brand

BRANDS = [
    "Abbi", "ACCENT", "Achosa", "AG Green", "AGATTI", "Aira Style", "AIRIN", "Alani Collection", "Alena Goretskaya", "ALEZA",
    "Algranda by Новелла Шарм", "Allma", "Allure", "AltaModa", "Amberа", "Amberа Style", "AMIE by Ma Сherie", "AMORI",
    "AMUAR", "Anastasia", "ANASTASIA MAK", "Andina", "Andina city", "Andrea Fashion", "Anelli", "Angelina & Сompany",
    "ANIDEN", "Anna Majewska", "ANNETE", "AnnLine", "AREOLA", "Art Ribbon", "ARTiMODA", "ArtMio", "ASV", "Atelero",
    "ATTIKA", "AURA of the day", "AVA fashion", "Avanti", "AVE RARA", "AVEEVA", "Avenue Fashion", "Avila", "Avord",
    "AVRIL", "AXXA", "AYZE", "Azet", "Azzara", "BARBARA", "Barbara Geratti by Elma", "Barti", "Bazalini", "Beautiful&Free",
    "Because", "BegiModa", "Belarusachka", "Belaruski Len", "Belinga", "Bell Bimbo", "BLAKIT", "Bliss", "Bonna Image",
    "BRAVO", "BRELA", "Bugalux", "BUNABOUTIQUE", "BURO", "BURVIN", "Butеr", "Camelia", "Celentano", "Celentano lite",
    "Cherire", "Chumakova Fashion", "Claire Cosmetics", "Classic Moda", "COCKTAIL", "COCOCO", "Colibri",
    "Colors of PAPAYA", "Colors of PAPAYA NEW", "Condra", "Conte Elegant", "Continental Fashion", "Cool Flax", "DaLi",
    "Daloria", "Danaida", "DAVA", "DAVYDOV", "Deesses", "Delford", "DEVITA", "Dilana VIP", "DiLiaFashion", "DILIS",
    "Diva", "Djerza", "DNM", "DOGGI", "DOMINION", "Domna", "DOV", "Edibor", "Elady", "ElectraStyle", "Elema",
    "ELLETTO LIFE", "Elod", "ElPaiz", "ELVIRA", "EMSE", "EMWE", "ENZA", "EOLA", "ERTANNO", "ESKA brand", "Etereo Amor",
    "Euromoda", "EVA GRANT", "EZER", "F de F", "FAMA", "Fantazia Mod", "FASHION CENTRE", "Faufilure", "Favorini",
    "Felice Woman", "Femme & Devur", "Fita", "FLAIM", "Fortuna. Шан-Жан", "FOXY FOX", "Frank&Co", "Friends",
    "FS - Viasna", "FunFun", "Ga-Ta Style", "Galanteya", "Galean Style", "Gallant Touch", "Gamma Gracia", "Garsonnier",
    "Gizart", "GlasiO", "GO", "Gold Style", "Golden Valley", "Grace for you", "GRATTO", "HELEN BIRCH", "HIT",
    "i3i Fashion", "Individual design", "INPOINT.", "InterFino", "INVITE", "IUKONA", "IVA", "IVARI", "Ivera", "Jolie",
    "JRSy", "Juliet Style", "JuNi Brand", "Jurimex", "Kaloris", "Karina deLux", "KaVaRi", "Ketty", "KIARA Collection",
    "Kivviwear", "Kiwi", "Klever", "Koketka i K", "KOKOdea", "KORTNI", "KOSKA", "LA LIBERTE", "La rouge", "LadisLine",
    "LADO", "Lady Line", "Lady Secret", "Lady Smile", "Lady Style Classic", "LadyThreeStars", "LAGENTE", "Laikony",
    "Lakbi", "LaKona", "LANSUA", "LARICI", "Latynka", "LaVeLa", "Le Collect", "Le Rina", "LEANNA-STYLE", "LECIEL",
    "Legend Style", "LeNata", "LEVEL", "LIBERTY", "Liliana", "LindaLux", "Liona Style", "Lissana", "Listelle", "LIZET",
    "LLC", "LM", "LM.Wear", "Lokka", "LoveLace", "Lucky mum", "LUDMILA LABKOVA", "Luitui", "Luna", "Lyushe",
    "Ma Vie", "Ma Сherie", "MadameRita", "Madech", "MAKKI", "MALI", "Manika Belle", "MARIKA", "MariSt", "MARKELL",
    "Marshop", "MarSo", "MASHA SKORINA", "Masstige", "Matini", "MAX", "MG Wear", "Mia-Moda", "Michel chic", "Mido",
    "MILA ROSH", "Milady", "Milavitsa", "MilMil", "Mira Fashion", "Mirolia", "MIRSINA FASHION", "Mislana", "Mita",
    "Mixan", "Moda Versal", "Modema", "Modum", "MOLVA", "MONA STYLE FASHION&DESIGN", "MONMU", "Morozov Amavie",
    "Motif", "Moveri by Larisa Balunova", "MOZART", "MSTEFA", "MT.Style", "MUA", "Mubliz", "MY AiR",
    "А2ГА", "АМУЛЕТ", "АРТПОСТЕЛЬ", "АРТУС", "Асолия", "БагираАнТа", "БАГРЯНИЦА", "БелЭльСтиль", "Диомант", "Дорофея",
    "Ивелта плюс", "Купалинка", "Ларс Стиль", "ЛЕДИ ГРАНД", "Леди Леда", "Линия Л", "Магия моды", "Магия Стиля",
    "Мастер Мод", "Медея и К", "Мехофф", "Милора-стиль", "Мишель стиль", "Мода Юрс", "Ника", "Ольга Стиль", "Орхидея",
    "Панда", "Пинск-Стиль", "Полесье", "Ружана", "Соджи", "СонМаркет", "Стильная леди", "Сч@стье", "Таир-Гранд",
    "Твой имидж", "ТОЧНО", "Файбертек", "Франтишка", "Элль-стиль"
]

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        for brand in BRANDS:
            Brand.objects.get_or_create(name=brand)
        self.stdout.write(self.style.SUCCESS("✅ Все бренды успешно добавлены в базу!"))
