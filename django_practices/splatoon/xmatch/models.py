from django.db import models

class Result(models.Model):
    # Fieldクラス: https://github.com/django/django/blob/stable/6.0.x/django/db/models/fields/__init__.py#L119
    # 第一引数は`verbose_name`というラベル名を指す
    content = models.CharField("内容", max_length=200)
    battle_at = models.DateTimeField("対戦日時")

class Player(models.Model):
    result = models.ForeignKey(Result, on_delete=models.CASCADE)
    wepon_type = models.CharField("武器種別")