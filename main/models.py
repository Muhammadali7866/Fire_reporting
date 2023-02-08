from django.db import models


# Create your models here.


class add_team(models.Model):
    team_name=models.CharField(max_length=50)
    team_lead=models.CharField(max_length=45)
    lead_number=models.CharField(max_length=50)
    team_member=models.CharField(max_length=50)
    postingDate = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.team_lead

class fire_report(models.Model):
    name=models.CharField(max_length=50)
    mobile=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    message=models.CharField(max_length=50)
    AssignTo=models.ForeignKey(add_team,on_delete=models.CASCADE,null=True)
    status=models.CharField(max_length=70,null=True)
    Postingdate = models.DateTimeField(auto_now_add=True)
    AssignedTime = models.CharField(max_length=150, null=True)
    UpdationDate = models.DateTimeField(null=True)
  


    def __str__(self):
        return self.name

class fire_history(models.Model):
    firereport=models.ForeignKey(fire_report,on_delete=models.CASCADE,null=True)
    status=models.CharField(max_length=75,null=True)
    remark=models.CharField(max_length=75,null=True)
    PostingDate = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.firereport)