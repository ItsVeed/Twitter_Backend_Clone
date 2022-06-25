# Generated by Django 4.0.5 on 2022-06-25 14:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tweet', '0002_tweet_likes_tweet_users_liked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='users_liked',
            field=models.ManyToManyField(related_name='tweet_user_liked', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=250)),
                ('datetimeuploaded', models.DateTimeField(auto_now_add=True)),
                ('likes', models.PositiveIntegerField(default=0)),
                ('tweet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tweet.tweet')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('users_liked', models.ManyToManyField(related_name='comment_user_liked', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
