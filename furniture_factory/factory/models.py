from django.db import models


class Base(models.Model):
    description = models.TextField(blank=True, verbose_name="Описание")

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class Workshop(Base):
    name = models.CharField(max_length=100, verbose_name="Название цеха")
    manager = models.OneToOneField(
        'Worker',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='managed_workshop',
        verbose_name="Начальник цеха"
    )

    @property
    def worker_count(self):
        return self.workers.count()

    def __str__(self):
        return f"{self.name} ({self.worker_count} рабочих)"


class Worker(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    position = models.CharField(max_length=100, verbose_name="Должность")
    workshop = models.ForeignKey(
        Workshop,
        on_delete=models.CASCADE,
        related_name='workers',
        verbose_name="Цех"
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Order(Base):
    STATUS_CHOICES = [
        ('P', 'В процессе'),
        ('C', 'Завершён'),
        ('H', 'Приостановлен'),
    ]

    title = models.CharField(max_length=100, verbose_name="Название заказа")
    workshops = models.ManyToManyField(
        Workshop,
        related_name='orders',
        verbose_name="Задействованные цеха"
    )
    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        default='P',
        verbose_name="Статус"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    def __str__(self):
        return self.title
