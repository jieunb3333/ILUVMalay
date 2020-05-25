from django.db import models

# Create your models here.
# 모델명 첫글자 대문자
class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    #char는 max를 꼭 설정해주어야함. Text는 글자수 제한이 없음.

    def __str__(self):
        return self.title

    
    def summary(self):
        return self.body[:50]

class Practice(models.Model):
    name = models.CharField(max_length=3)
    age = models.IntegerField()
    
