from rest_framework import serializers

from retail.models import Network, Trader, Product


class NetworkSerializer(serializers.ModelSerializer):
    """Сериализатор для модели торговой сети"""

    class Meta:
        model = Network
        fields = '__all__'


class TraderSerializer(serializers.ModelSerializer):
    """Сериализатор для модели звена торговой сети
    Поле debt (задолженность перед поставщиком) доступно только для чтения,
    редактирование возможно через админ-панель для суперпользователей.
    Список продуктов выводится по названиям."""
    products = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Trader
        fields = '__all__'
        read_only_fields = ('debt',)


class ProductSerializer(serializers.ModelSerializer):
    """Сериализатор для модели продукта"""

    class Meta:
        model = Product
        fields = '__all__'
