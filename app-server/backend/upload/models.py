from django.db import models

# Creating package class for the sake of documentation and future abilities
class Packagey(models.Model):
    pack_name = models.CharField(max_length=64)# 64 is standard max repo name character limit
    pack_ID = models.IntegerField # Each package should have an ID number in the github API
    version_field = models.CharField(max_length=9) # allows for XX.XX.XX format (content should be found on 1st level of json)
    stars = models.IntegerField()  # Stargazer count
    downloads = models.IntegerField() # Download count overall (if releases are relevant)
    metrics_score = models.FloatField(max_length=4) # metric score should at most contain 2 beyond the decimal

    def __str__(self):
        return self.pack_name