from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
class Sensor(models.Model):
    name = models.CharField('Название', max_length=50)
    description = models.TextField('Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сенсор'
        verbose_name_plural = 'Сенсоры'

class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.FloatField('Температура')
    date = models.DateTimeField('Дата/Время', auto_now_add=True)
    picture = models.ImageField(null=True)

    class Meta:
        verbose_name = 'Измерение'
        verbose_name_plural = 'Измерения'