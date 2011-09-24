from django.db import models
from django.contrib.auth.models import User

class TimeshitClient(models.Model):
    name = models.CharField(max_length=64)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return "User: %s, Client: %s" % (self.user.email, self.name)


class TimeshitProject(models.Model):
    client = models.ForeignKey(TimeshitClient)
    name = models.CharField(max_length=64)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return "User: %s, Project: %s" % (self.user.email, self.name)


class TimeshitTask(models.Model):
    project = models.ForeignKey(TimeshitProject)
    name = models.CharField(max_length=64)
    user = models.ForeignKey(User)
 
    def __unicode__(self):
        return "User: %s, Task: %s" % (self.user.email, self.name)


class TimeshitRecord(models.Model):
    task = models.ForeignKey(TimeshitTask)
    user = models.ForeignKey(User)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __unicode__(self):
        return 'UserRecord: %d' % self.id

