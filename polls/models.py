from django.db import models
from django.utils import timezone
from datetime import timedelta
class Questions(models.Model):
    question_text = models.CharField(max_length=50)
    public_date = models.DateField(default=timezone.now, null=True)
    end_date = models.DateField(default= timezone.now() + timedelta(days=1), null=True)

    def __str__(self):
        return self.question_text
    
class choice(models.Model):
    questions = models.ForeignKey(Questions, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=25)
    
    def __str__(self) -> str:
        return self.choice_text