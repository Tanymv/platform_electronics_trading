from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Network(models.Model):
    """Модель торговой сети"""
    title = models.CharField(max_length=255, verbose_name='Наименование')
    factory = models.ForeignKey('Trader', on_delete=models.SET_NULL, related_name='factory',
                                verbose_name='Производитель', **NULLABLE)
    provider = models.ForeignKey('Trader', on_delete=models.SET_NULL, related_name='provider', verbose_name='Поставщик',
                                 **NULLABLE)
    trader = models.ForeignKey('Trader', on_delete=models.SET_NULL, related_name='trade', verbose_name='Продавец',
                               **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Торговая сеть"
        verbose_name_plural = "Торговые сети"


class Product(models.Model):
    """Модель продукта"""

    title = models.CharField(max_length=200, verbose_name='Название')
    mod = models.CharField(max_length=50, verbose_name='модель')
    released_at = models.DateField(verbose_name='Дата выхода на рынок')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class Trader(models.Model):
    """Модель звена торговой сети"""

    LEVEL_CHOICES = [
        ('0', 'Производитель'), ('1', 'Поставщик'), ('2', 'Продавец')
    ]

    TYPE_CHOICES = [
        ('factory', 'Завод'), ('retail', 'Розничная сеть'), ('individual', 'Индивидуальный предприниматель')
    ]

    trader_level = models.CharField(choices=LEVEL_CHOICES, max_length=1, verbose_name='Уровень в иерархии', default='0')
    trader_type = models.CharField(choices=TYPE_CHOICES, max_length=20, verbose_name='Тип звена', default='factory')

    title = models.CharField(max_length=200, unique=True, verbose_name='Название')
    email = models.EmailField(unique=True, verbose_name='Почта', **NULLABLE)

    country = models.CharField(max_length=150, verbose_name='Страна')
    city = models.CharField(max_length=150, verbose_name='Город')
    street = models.CharField(max_length=150, verbose_name='Улица')
    house = models.CharField(max_length=50, verbose_name='Дом(номер, литера, помещение)')

    supplier = models.ForeignKey('Trader', on_delete=models.SET_NULL, verbose_name='Поставщик', **NULLABLE)
    debt = models.DecimalField(max_digits=20, decimal_places=2, default=0,
                               verbose_name='Задолженность перед поставщиком')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата добавления в систему')

    products = models.ManyToManyField(Product, verbose_name='Продукты')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Звено торговой сети"
        verbose_name_plural = "Звенья торговой сети"
