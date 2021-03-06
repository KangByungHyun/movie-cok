# Generated by Django 3.2.4 on 2021-07-12 13:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='아이디')),
                ('title', models.TextField(verbose_name='제목')),
                ('genre', models.TextField(verbose_name='장르')),
                ('nation', models.TextField(verbose_name='국가')),
                ('playtime', models.IntegerField(verbose_name='상영시간')),
                ('directors', models.TextField(verbose_name='감독')),
                ('actors', models.TextField(verbose_name='배우')),
                ('age', models.IntegerField(verbose_name='연령등급')),
                ('date', models.DateField(verbose_name='개봉일')),
                ('summary', models.TextField(blank=True, null=True, verbose_name='줄거리')),
                ('image', models.URLField(verbose_name='이미지')),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score_npro', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='네티즌평점')),
                ('score_pro', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='전문가평점')),
                ('score_m', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='남자평점')),
                ('score_w', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='여자평점')),
                ('score_10', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='10대평점')),
                ('score_20', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='20대평점')),
                ('score_30', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='30대평점')),
                ('score_40', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='40대평점')),
                ('score_50', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='50대평점')),
                ('production', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='연출')),
                ('acting', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='연기')),
                ('story', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='스토리')),
                ('visual', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='영상미')),
                ('ost', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='ost')),
                ('movie', models.OneToOneField(db_column='movie', on_delete=django.db.models.deletion.CASCADE, related_name='score', to='movie.movie', verbose_name='영화')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score_user', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='회원평점')),
                ('point', models.TextField(verbose_name='포인트')),
                ('content', models.TextField(verbose_name='내용')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='작성일')),
                ('modify_date', models.DateTimeField(blank=True, null=True, verbose_name='수정일')),
                ('author', models.ForeignKey(db_column='author', on_delete=django.db.models.deletion.CASCADE, related_name='comment', to=settings.AUTH_USER_MODEL, verbose_name='작성자')),
                ('movie', models.ForeignKey(db_column='movie', on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='movie.movie', verbose_name='영화')),
            ],
        ),
    ]
