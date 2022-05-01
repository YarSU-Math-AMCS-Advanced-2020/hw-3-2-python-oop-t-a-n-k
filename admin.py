from promocode import Promocode
from client import Client
# Класс администроатора


def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance


@singleton
class Admin:
    def __init__(self):
        pass

    def generate_promocode(self, promo_id, percent):
        return Promocode(promo_id, [], percent)

    def send_promocode(self, client, promocode):
        client.promo_list(promocode)


c_a = Admin()
c_b = Admin()
print(c_a == c_b)
client1 = Client("Ali", "Michu", "+79038210575", "meow.mail")
# promo1 = c_a.generate_promocode("000001", "15")
# print(f"{promo1.promocode_id()} for {promo1.percent()}% discount")
# c_a.send_promocode(client1, promo1)
# print(f"client {client1.name} {client1.surname} has promos:")
# promo = client1.promo_list()[0]
# print(f"{promo.promocode_id()} for {promo.percent()}% discount")