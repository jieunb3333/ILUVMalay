from django.db import models

# Create your models here.
class Portfolio(models.Model):
    image = models.ImageField(upload_to="portfolio/%Y/%m/%d")
    # pakage_num = models.IntegerField(help_text='4자리로 입력해주세요.')
    # pakage_name = models.CharField(max_length=50)
    # max_person=models.IntegerField()
    # pre_person=models.IntegerField()
    # during_date = models.CharField(max_length=50,default="입력값없음.")
    description = models.CharField(max_length=500)

    # model에서는 필드의 추가 / 수정 / 삭제가 이루어 지고 난 후 makemigration과 migrate가 이루어져야한다