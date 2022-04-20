class t26:
    mobility = 10
    armament = 5
    booking = 2
    crew = 3
class bt7(t26):
    mobility = 14
class t28(bt7):
    mobility = 8
    armament = 15
    crew = 8
class KV1(t28):
    booking = 15
    mobility = 6
    crew = 5
t26 = t26()
bt7 = bt7()
t28 = t28()
kv1 = KV1()
print("Танк | Мобильность | Вооружение | Бронирование | Кол-во членов экипажа")
print("Т-16 ",t26.mobility,t26.armament,t26.booking,t26.crew)
print("БТ-7 ",bt7.mobility,bt7.armament,bt7.booking,bt7.crew)
print("Т-28 ",t28.mobility,t28.armament,t28.booking,t28.crew)
print("КВ-1 ",kv1.mobility,kv1.armament,kv1.booking,kv1.crew)