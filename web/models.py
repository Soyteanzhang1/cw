from django.db import models

# Create your models here.

class Blog(models.Model):
    # name = models.CharField('博客名称',max_length=64,unique=True)
    user = models.CharField('用户名',max_length=64,unique=True)
    title = models.CharField('文章标题',max_length=128,unique=True)
    content = models.TextField('文章内容')

class User(models.Model):
    user = models.CharField('用户名',max_length=64,unique=True)
    pwd = models.CharField('密码',max_length=64)

