import random
from django.contrib.auth.models import User
from django.db import models

class OTP(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    otp_code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def generate_otp(self):
        return str(random.randint(100000, 999999))


class UploadedVideo(models.Model):
    video_file = models.FileField(upload_to='videos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Video {self.pk}"
from django.db import models

class Video(models.Model):
    file = models.FileField(upload_to='videos1/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name
class ImageUpload(models.Model):
    image_file = models.ImageField(upload_to="uploads/", blank=True, null=True)
    image_folder = models.FileField(upload_to="uploads/", blank=True, null=True)

    def __str__(self):
        return self.image_file.name
from django.db import models
from django.contrib.auth.models import User

class DetectionHistory(models.Model):
    DETECTION_TYPES = (
        ('video', 'Video Detection'),
        ('image', 'Image Detection'),
        ('video_meta', 'Video Metadata'),
        ('image_meta', 'Image Metadata'),
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    detection_type = models.CharField(max_length=20, choices=DETECTION_TYPES)
    filename = models.CharField(max_length=255)
    result = models.CharField(max_length=100)
    confidence = models.FloatField(null=True, blank=True)
    metadata = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return f"{self.get_detection_type_display()} - {self.filename}"