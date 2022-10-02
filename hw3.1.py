import json


"""создать атрибут _repr в классе-потомке и в него ввести то, что необходимо вывести по функции repr"""
class ColorizeMixin(object):
    repr_color_code = 35

    def __repr__(self):
        return "\033[1;0;%im%s" % (self.repr_color_code, self._repr)


"""fff"""
class AttributesDict(object):
    def __init__(self, original_dictionary):
        self.dictionary = {}
        for key, obj in original_dictionary.items():
            if type(obj) is not dict:
                self.dictionary[key] = obj
            else:
                self.dictionary[key] = AttributesDict(obj)
        self.__dict__.update(self.dictionary)
        self.__original_object = original_dictionary

    def __repr__(self):
        return str(self.__original_object)


class Advert(ColorizeMixin, object):
    def __init__(self, dictionary):
        a = AttributesDict(dictionary)
        self.__dict__.update(a.dictionary)
        if 'price' in self.__dict__:
            if self.price < 0:
                raise ValueError('Price must be >= 0')
        else:
            self.price = 0

        self._repr = f'{self.title} | {self.price} ₽'

    repr_color_code = 35


lesson_str = """{
"title": "python", "price": 0,
"location": {
"address": "город Москва, Лесная, 7",
"transport": {"metro_stations": ["Белорусская"], "buses": [1 ,2,3]}}
}"""

lesson = json.loads(lesson_str)
lesson_ad = Advert(lesson)
print(lesson_ad.title)
print(lesson_ad.price)
print(lesson_ad)
print(lesson_ad.location.transport)
print(lesson_ad.location.transport.metro_stations)
