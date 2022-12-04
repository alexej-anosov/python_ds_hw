import json
import keyword


class ColorizeMixin:
    """создать  _to_repr в классе-потомке и в него ввести то, что необходимо вывести по функции repr"""
    repr_color_code = 0

    def __repr__(self):
        return "\033[1;0;%im%s\033[0m" % (self.repr_color_code, self._to_repr())


class AttributesDict:
    """если значение атрибута класса Advert это словарь, то он в аттрибуте хранится объект данного класса"""
    def __init__(self, original_dictionary):
        self.__dictionary = original_dictionary
        for key, value in original_dictionary.items():
            if keyword.iskeyword(key):
                key = f'{key}_'
            if type(value) is dict:
                setattr(self, key, AttributesDict(value))
            else:
                setattr(self, key, value)

    def __repr__(self):
        return str(self.__dictionary)


class Advert(ColorizeMixin):

    repr_color_code = 34
    _price = 0

    def __init__(self, dictionary):
        for key, value in dictionary.items():
            if keyword.iskeyword(key):
                key = f'{key}_'
            if type(value) is dict:
                setattr(self, key, AttributesDict(value))
            else:
                if key == 'price':
                    self._price = value
                else:
                    setattr(self, key, value)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price_value):
        if price_value < 0:
            raise ValueError('Price must be >= 0')
        self._price = price_value

    def _to_repr(self):
        return f'{self.title} | {self.price} ₽'


if __name__ == '__main__':

    lesson_str = """{
    "title": "python", "price": 1,
    "location": {
    "address": "город Москва, Лесная, 7",
    "transport": {"metro_stations": ["Белорусская"], "buses": [1,2,3]}}
    }"""

    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    print(lesson_ad.title)
    print(lesson_ad.price)
    lesson_ad.price = 2
    print(lesson_ad)
    print(lesson_ad.location.transport)
    print(lesson_ad.location.transport.metro_stations)
