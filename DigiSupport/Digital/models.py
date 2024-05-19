from django.db import models
from django.contrib.auth.models import User

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
    
class Folder(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class File(models.Model):
    folder = models.ForeignKey(Folder, related_name='files', on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.file.name
    
class ChatLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ChatLog({self.user}, {self.timestamp})"


    
    
    