# Generated by Django 2.0 on 2019-12-31 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PGFinder', '0002_auto_20191230_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='findpg',
            name='location',
            field=models.CharField(choices=[('uk', 'United Kingdom'), ('australia', 'Australia'), ('canada', 'Canada'), ('germany', 'Germany')], default='australia', max_length=100),
        ),
        migrations.AlterField(
            model_name='findpg',
            name='mealchoice',
            field=models.CharField(choices=[('onetime', 'Breakfast only'), ('twotimes', 'Breakfast & Dinner'), ('threetimes', 'Breakfast, Lunch & Dinner')], default='threetimes', max_length=100),
        ),
        migrations.AlterField(
            model_name='findpg',
            name='rentchoice',
            field=models.CharField(choices=[('daily', 'Daily'), ('monthly', 'Monthly'), ('quarterly', 'Quarterly'), ('Yearly', 'Yearly')], default='monthly', max_length=100),
        ),
        migrations.AlterField(
            model_name='findpg',
            name='roomchoice',
            field=models.CharField(choices=[('singleroom', 'Singleroom'), ('twosharedroom', 'Twosharedroom'), ('threesharedroom', 'Threesharedroom'), ('foursharedroom', 'Foursharedroom')], default='singleroom', max_length=100),
        ),
    ]