import random
class Student:
    def __init__(self, name):
        self.name = name
        self.gladness= 40.0
        self.progress= 1
        self.money= 40
        self.eat= 10
        self.alive=True
    def to_study(self):
        print("Сделаю дз, что ли")
        self.progress+=0.5
        self.gladness-=3
    def to_sleep(self):
        print("ГГ, я ливаю спать")
        self.gladness+=2
        self.progress-=0.1
        self.eat-=0.1
    def to_chill(self):
        print("Пора повеселиться!")
        self.gladness+=8
        self.progress-=0.4
        self.money-=5
        self.eat+=0.3
    def to_eat(self):
        print("Ммм... Доширак")
        self.eat+=2.0
        self.gladness+=5
        self.money-=4
        self.progress+=0.2
    def to_work(self):
        print("Пойду поработаю")
        self.eat-=1
        self.money+=30
        self.gladness-=9
    def is_alive(self):
        if self.progress < -0.5:
            print("Вышвырнули, как псину, из универа...")
            self.alive=False
        if self.gladness<=0:
            print("Его погубила депресия")
            self.alive=False
        elif self.progress > 20:
            print("Закончил универ экстерном!")
            self.alive=False
        elif self.eat<=0:
            print("Умер с голоду")
            self.alive=False
        elif self.money < -10:
            print("Погряз в долгах")
            self.alive=False
    def end_of_day(self):
        print(f"Душевное состояние={self.gladness}")
        print(f"Прогресс учёбы={round(self.progress,2)}")
        print(f"Уровень голода={self.eat}")
        print(f"Кол-во денег={self.money} рублей")
    def live(self,day):
        day= "День " + str(day) + " из жизни студента " + self.name
        print(f"{day:=^50}")
        live_cube= random.randint(1,5)
        if self.eat<=0.5:
            self.to_eat()
        elif live_cube==1:
            self.to_study()
        elif live_cube==2:
            self.to_sleep()
        elif live_cube==3:
            self.to_chill()
        elif live_cube == 4:
            self.to_eat()
        elif live_cube == 5:
            self.to_work()
        self.end_of_day()
        self.is_alive()
nick=Student(name="Вити")
for day in range(1826):
    if day==365:
        print("Витя закончил 1 курс!")
    elif day==730:
        print("Витя закончил 2 курс!")
    elif day==1095:
        print("Витя закончил 3 курс!")
    elif day==1460:
        print("Витя закончил 4 курс!")
    elif day==1825:
        print("Витя закончил универ!!!")
        break
    elif nick.alive==False:
        break
    nick.live(day)