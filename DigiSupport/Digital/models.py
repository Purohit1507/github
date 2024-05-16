from django.db import models

# Create your models here.
class Post(models.Model):
    department =models.CharField(max_length=150)
    Problem =models.TextField(max_length=150)
    
class NetAuthorizationRequest(models.Model):
    applicant_ps_number = models.CharField(max_length=100)
    applicant_name = models.CharField(max_length=100)
    applicant_email_id = models.EmailField()
    request_date = models.DateField()
    location = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=15)
    initiator_hod_ps_no = models.CharField(max_length=100)
    initiator_hod_name = models.CharField(max_length=100)
    initiator_hod_email_id = models.EmailField()
    net_request_type = models.CharField(max_length=100)
    copy_to_id = models.CharField(max_length=100)
    copy_from_id = models.CharField(max_length=100)
    application_name = models.CharField(max_length=100)
    justification = models.TextField()

    def __str__(self):
        return self.applicant_name

    
    
    