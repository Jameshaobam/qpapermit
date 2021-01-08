from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Year(models.Model):
    year = models.CharField(max_length = 10)
    value = models.CharField(max_length = 10)

    def __str__(self):
        return self.year

class Question(models.Model):
    trade = models.CharField(max_length = 10)
    semester = models.CharField(max_length = 10)
    subject = models.CharField(max_length = 20)
    exam = models.CharField(max_length = 10)
    year_of_exm = models.CharField(max_length = 10)
    file = CloudinaryField(resource_type ='image',folder = 'questions_Qpaper')
    owner = models.ForeignKey(User, on_delete = models.CASCADE)
    date_published = models.DateTimeField()
    def __str__(self):
        return self.trade +"|"+self.semester+"|"+self.exam+"|"+self.year_of_exm+'|' + self.subject + "|" + "by " + self.owner.username

class Answer(models.Model):
    post = models.ForeignKey(Question, on_delete = models.CASCADE,related_name = 'answers')
    owner = models.ForeignKey(User, on_delete = models.CASCADE)
    context = models.CharField(max_length = 30,blank = False)
    image = CloudinaryField(resource_type ='image',folder = 'answers_Qpaper')
    date_published = models.DateTimeField()

    def __str__(self):
        return f"{self.post.trade}|{self.post.semester}Sem|{self.post.subject}|{self.post.year_of_exm}|{self.post.exam} by {self.owner}"