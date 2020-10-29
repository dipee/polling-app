from django.db import models

# Create your models here.
class Poll(models.Model):
    question = models.TextField(max_length=255)
    option_one = models.CharField(max_length=30)
    option_two  = models.CharField(max_length=30)
    option_three = models.CharField(max_length=30)
    option_one_count = models.IntegerField(default=0)
    option_two_count  = models.IntegerField(default=0)
    option_three_count  = models.IntegerField(default=0)

    def total(self):
        return self.option_one_count + self.option_two_count+self.option_three_count

    def percent_one(self):
        if(self.option_one_count>0):
            return self.option_one_count/int(self.total())*100
        else:
            return 0;
    
    def percent_two(self):
        if(self.option_three_count>0):
            return self.option_two_count/int(self.total())*100
        else:
            return 0;
    
    def percent_three(self):
        if(self.option_three_count>0):
            return self.option_three_count/int(self.total())*100
        else:
            return 0;