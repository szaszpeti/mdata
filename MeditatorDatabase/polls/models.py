from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    slug = models.CharField(max_length=10, unique=True,
                            default="question")

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Meditator(models.Model):
    name = models.CharField(max_length=264)
    country = models.CharField(max_length=120)
    born = models.CharField(max_length=20)
    gender = models.CharField(max_length=10, null=True)
    email = models.EmailField(max_length=60, unique=True)
    phone = models.CharField(max_length=60)
    profession = models.CharField(max_length=60)
    course = models.CharField(max_length=60)
    course_date = models.DateField()
    teacher = models.CharField(max_length=60)
    remarks = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return self.name

