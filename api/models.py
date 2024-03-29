from django.db import models


class Users(models.Model):
    id = models.AutoField(primary_key=True)
    nickname = models.CharField(max_length=255)
    hash_password = models.CharField(max_length=255)

    def __str__(self):
        return self.nickname

    class Meta:
        verbose_name_plural = "Users"
        verbose_name = "User"
        # managed = True
        # db_table = 'myapp_users'
        # app_label = 'myapp'


class News(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    news_date = models.DateField()
    address = models.TextField()
    url = models.TextField()
    img = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "News"
        verbose_name = "News"
        # managed = True
        # db_table = 'News'
        # app_label = 'myapp'


class Feedback(models.Model):
    id = models.AutoField(primary_key=True)
    news_id = models.ForeignKey(News, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    comment = models.TextField()
    feedback_date = models.DateField()

    def __str__(self):
        return self.comment

    class Meta:
        verbose_name_plural = "Feedback"
        verbose_name = "Feedback"
        # managed = True
        # db_table = 'Feedback'
        # app_label = 'myapp'
