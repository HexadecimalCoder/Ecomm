from django.db import models


class User(models.Model):
    fname = models.CharField(max_length=50, null=True, blank=True)
    lname = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    email=models.EmailField()
    password=models.CharField(max_length=500)
    profileImg = models.ImageField(upload_to='profile_images/', blank=True, null=True)

    def register(self):
        self.save()

    @staticmethod
     
    def get_customer_by_email(email):
        try:
            return User.objects.get(email=email)
        except:
            return False
        
    def isExists(self):
        if User.objects.filter(email=self.email):
            return True
        