from abc import ABC, abstractmethod


class BaseProduct(ABC):

    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs):
        '''Создан абстрактный метод для ввода нового продукта'''
        pass

