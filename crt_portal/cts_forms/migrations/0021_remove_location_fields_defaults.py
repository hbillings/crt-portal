# Generated by Django 2.2.4 on 2019-11-25 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cts_forms', '0020_add_location_fields_to_cts_form'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='location_city_town',
            field=models.CharField(max_length=700),
        ),
        migrations.AlterField(
            model_name='report',
            name='location_name',
            field=models.CharField(max_length=225),
        ),
        migrations.AlterField(
            model_name='report',
            name='location_state',
            field=models.CharField(choices=[('AL', 'Alabama '), ('AK', 'Alaska '), ('AZ', 'Arizona '), ('AR', 'Arkansas '), ('CA', 'California '), ('CO', 'Colorado '), ('CT', 'Connecticut '), ('DE', 'Delaware '), ('DC', 'District of Columbia '), ('FL', 'Florida '), ('GA', 'Georgia '), ('HI', 'Hawaii '), ('ID', 'Idaho '), ('IL', 'Illinois '), ('IN', 'Indiana '), ('IA', 'Iowa '), ('KS', 'Kansas '), ('KY', 'Kentucky '), ('LA', 'Louisiana '), ('ME', 'Maine '), ('MD', 'Maryland '), ('MA', 'Massachusetts '), ('MI', 'Michigan '), ('MN', 'Minnesota '), ('MS', 'Mississippi '), ('MO', 'Missouri '), ('MT', 'Montana '), ('NE', 'Nebraska '), ('NV', 'Nevada '), ('NH', 'New Hampshire '), ('NJ', 'New Jersey '), ('NM', 'New Mexico '), ('NY', 'New York '), ('NC', 'North Carolina '), ('ND', 'North Dakota '), ('OH', 'Ohio '), ('OK', 'Oklahoma '), ('OR', 'Oregon '), ('PA', 'Pennsylvania '), ('RI', 'Rhode Island '), ('SC', 'South Carolina '), ('SD', 'South Dakota '), ('TN', 'Tennessee '), ('TX', 'Texas '), ('UT', 'Utah '), ('VT', 'Vermont '), ('VA', 'Virginia '), ('WA', 'Washington '), ('WV', 'West Virginia '), ('WI', 'Wisconsin '), ('WY', 'Wyoming '), ('AS', 'American Samoa '), ('GU', 'Guam '), ('MP', 'Northern Mariana Islands '), ('PR', 'Puerto Rico '), ('VI', 'Virgin Islands '), ('AE', 'Armed Forces Africa '), ('AA', 'Armed Forces Americas '), ('AE', 'Armed Forces Canada '), ('AE', 'Armed Forces Europe '), ('AE', 'Armed Forces Middle East '), ('AP', 'Armed Forces Pacific ')], max_length=100),
        ),
    ]
