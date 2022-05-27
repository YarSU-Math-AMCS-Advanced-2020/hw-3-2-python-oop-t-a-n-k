from product import Product
from productShopAvailability import ProductShopAvailability, ProductInOrder
from promocode import Promocode
from uuid import UUID
from typing import List, Union
from review import Review
from review import Star_mark


class Client:

    def __init__(self, client_id: UUID, name: str, surname: str,
                 address: str, mail: str, phone: str):
        self.id = client_id
        self.name = name
        self.surname = surname
        self.address = address
        self.mail = mail
        self.phone = phone
        self._cart_list: List[ProductInOrder] = []
        self._promo_list: List[Promocode] = []

    @property
    def cart_list(self):
        return self._cart_list

    @cart_list.setter
    def cart_list(self, cart: List[ProductInOrder]):
        self._cart_list = cart

    @property
    def promo_list(self):
        return self._promo_list

    @promo_list.setter
    def promo_list(self, promo: List[Promocode]):
        self._promo_list = promo

    # добавление отзыва на конкретный продукт
    def write_review(self, product: Product,
                     mark_star: Star_mark, review_text: str) -> None:
        review = Review(name=self.name, surname=self.surname,
                        text=review_text, star=mark_star)
        product.add_review(review)

    def add_to_cartlist(self, product: ProductShopAvailability,
                        count: int) -> None:
        if self._cart_list:
            if product.shop != self._cart_list[0].shop or \
                    product.amount == 0:
                raise TypeError(f"You can't add such product {product}")
            else:
                self._cart_list.append(ProductInOrder(product, count))
        else:
            self._cart_list.append(ProductInOrder(product, count))

    def del_from_cartlist(self,
                          product: Union[ProductInOrder,
                                         ProductShopAvailability]) -> None:
        cart_dict = {prod.id: i for i, prod in enumerate(self._cart_list)}
        if product.id in cart_dict:
            del self._cart_list[cart_dict[product.id]]
        else:
            raise IndexError(f"No such product in cart_list {product}")

    def clean_cart_list(self) -> None:
        self._cart_list = []

    def add_promo(self, promo: Promocode) -> None:
        self._promo_list += [promo]

    def del_from_promolist(self, promo: Promocode) -> None:
        promo_dict = {it_promo.promocode_id: i for i, it_promo
                      in enumerate(self._promo_list)}
        if promo.promocode_id in promo_dict:
            del self._cart_list[promo_dict[promo.promocode_id]]
        else:
            raise IndexError(f"No such promo in promo_list {promo}")

    def __str__(self):
        return f"{self.name}\n{self.surname}\n{self.mail}"
