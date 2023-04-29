from django.db import models

# Creating package class for the sake of documentation and future abilities
class Package(models.Model):
    pack_ID = models.IntegerField # 64 is standard max repo name character limit
    version_field = models.CharField(max_length=9) # allows for XX.XX.XX format
    popularity_score = models.IntegerField()  # popularity score will scale
    metrics_score = models.FloatField(max_length=4) # metric score should at most contain 2 beyond the decimal