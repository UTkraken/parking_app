from django.core.management import BaseCommand

from ...models import Parking, Floor, Spot


class Command(BaseCommand):
    help = 'Adds data to the database'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Start adding data ...'))

        park_info = [
            {'name': 'Bonlieu', 'code': 'BON'},
            {'name': 'Courrier', 'code': 'COU'},
            {'name': 'Hôtel de ville', 'code': 'HDV'}
        ]

        for info in park_info:
            parking = Parking.objects.create(**info)

            for num_floor in [0, -1, -2]:
                floor = Floor.objects.create(
                    number=num_floor,
                    parking=parking,
                )

                for num_spot in range(1,7):
                    spot = Spot.objects.create(
                        number=num_spot,
                        floor=floor,
                    )
            self.stdout.write(self.style.SUCCESS(f'{parking.name} successfully added'))