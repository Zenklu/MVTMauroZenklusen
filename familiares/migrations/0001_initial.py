

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.PositiveIntegerField(verbose_name=99)),
                ('ocupation', models.CharField(max_length=50)),
                ('relationship', models.CharField(max_length=50)),
                ('born', models.DateField(max_length=50)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
