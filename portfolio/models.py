from django.db import models

# Create your models here.
class Portfolio(models.Model):
    image = models.ImageField(upload_to="portfolio/%Y/%m/%d")
    description = models.CharField(max_length=500)

    # model에서는 필드의 추가 / 수정 / 삭제가 이루어 지고 난 후 makemigration과 migrate가 이루어져야한다