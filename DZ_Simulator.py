import random
class auto:
    def __init__(self, name):
        self.name = name
        self.benz= 60.0
        self.progress= 1
        self.money= 40
        self.eat= 10
        self.koleso=4
        self.sapachkoleso=1
        self.gladness=10
        self.alive=True
    def to_go(self):
        print("Едем...")
        self.progress+=10
        self.benz-=1
        self.eat-=0.2
    def to_koleso(self):
        print("Колесо спустило, надо надуть")
        self.koleso-=1
        self.eat-=1
        self.gladness-=5
    def to_chill(self):
        print("Смотри какая!")
        self.gladness+=8
        self.money-=10
    def to_eat(self):
        print("Остановлюсь покушать")
        self.eat+=3.0
        self.gladness+=2
    def to_work(self):
        print("Поеду потаксую")
        self.eat-=1
        self.money+=40
        self.gladness-=6
    def to_buy_eat(self):
        print("Еда закончилась, остановлюсь и куплю")
        self.progress+=2
        self.money-=10
    def to_buy_lokeso(self):
        print("Надо запаску купить, малоли что")
        self.money-=20
        self.sapachkoleso+=1
    def to_polomka(self):
        print("Перегрелся что ли")
        self.gladness-=5
    def is_alive(self):
        if self.gladness<=0:
            print("Потерял смысл жизни")
            self.alive=False
        elif self.progress > 2000:
            print("Доехал!")
            self.alive=False
        elif self.eat<=0:
            print("Замучал голод")
            self.alive=False
        elif self.money < -10:
            print("Не осталось ни копейки на еду")
            self.alive=False
    def end_of_day(self):
        print(f"Настроение={self.gladness}")
        print(f"Проеханный путь={round(self.progress,2)}")
        print(f"Сытость={self.eat}")
        print(f"Кол-во денег={self.money} рублей")
    def live(self,day):
        day= "День " + str(day) + " из поездки " + self.name
        print(f"{day:=^50}")
        live_cube= random.randint(1,5)
        if self.eat<=0.5:
            self.to_eat()
        elif live_cube==1:
            self.to_buy_lokeso()
        elif live_cube==2:
            self.to_buy_eat()
        elif live_cube==3:
            self.to_chill()
        elif live_cube == 4:
            self.to_eat()
        elif live_cube == 5:
            self.to_work()
        elif live_cube == 6:
            self.to_go()
        elif live_cube == 7:
            self.to_polomka()
        self.end_of_day()
        self.is_alive()
nick=auto(name="Вити")
for day in range(1826):
    if nick.alive==False:
        print("Его путь окончен")
        break
    nick.live(day)