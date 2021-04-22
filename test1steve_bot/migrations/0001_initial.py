# Generated by Django 3.1.3 on 2021-03-15 06:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TelegramChat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram_id', models.CharField(max_length=128, unique=True)),
                ('type', models.CharField(choices=[('private', 'private'), ('group', 'group'), ('supergroup', 'supergroup'), ('channel', 'channel')], max_length=128)),
                ('title', models.CharField(blank=True, max_length=512, null=True)),
                ('username', models.CharField(blank=True, max_length=128, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TelegramUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram_id', models.CharField(max_length=128, unique=True)),
                ('is_bot', models.BooleanField(default=False)),
                ('first_name', models.CharField(max_length=128)),
                ('last_name', models.CharField(blank=True, max_length=128, null=True)),
                ('username', models.CharField(blank=True, max_length=128, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TelegramState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('memory', models.TextField(blank=True, null=True, verbose_name='Memory in JSON format')),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('telegram_chat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='telegram_states', to='test1steve_bot.telegramchat')),
                ('telegram_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='telegram_states', to='test1steve_bot.telegramuser')),
            ],
            options={
                'unique_together': {('telegram_user', 'telegram_chat')},
            },
        ),
    ]
