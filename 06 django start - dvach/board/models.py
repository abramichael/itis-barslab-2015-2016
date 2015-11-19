from django.db import models

class Post(models.Model):
    text = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    def __unicode__(self):
        return "%s:%s" % (self.text, self.pub_date)

class Comment(models.Model):
    post = models.ForeignKey(Post)
    text = models.CharField(max_length=200)
    pub_date = models.DateTimeField()        
    def __unicode__(self):
        return "%s : %s : %s" % (self.post.text , self.text, self.pub_date)