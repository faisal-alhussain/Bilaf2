# Generated by Django 4.2.2 on 2023-06-17 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0009_alter_store_instagram_link_alter_store_snapchat_link_and_more'),
        ('main_app', '0003_remove_product_product_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('logo', models.ImageField(default='images/placeholder.png', upload_to='images/')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users_app.store')),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
