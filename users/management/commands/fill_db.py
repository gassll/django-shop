import random

from django.core.management import BaseCommand
from django.db import transaction
from faker.proxy import Faker

from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Скрипт для создания тестовых данных"

    def handle(self, *args, **options):
        faker = Faker(["ru_RU"])

        with transaction.atomic():
            # Вариант 1: Используем только bulk_create
            category_list = []

            for _ in range(5):
                category = Category(
                    name=faker.word(),
                    slug=faker.slug(),
                    description=faker.text(),
                    is_active=True,
                )
                category_list.append(category)

            # Создаем все категории одним запросом
            Category.objects.bulk_create(category_list)

            product_list = []

            for _ in range(100):
                product = Product(
                    name=faker.word(),
                    description=faker.text(),
                    category=random.choice(category_list),
                )
                product_list.append(product)

            # Создаем все продукты одним запросом
            Product.objects.bulk_create(product_list)

        self.stdout.write(
            self.style.SUCCESS(
                f'Создано {len(category_list)} категорий и {len(product_list)} продуктов'
            )
        )
