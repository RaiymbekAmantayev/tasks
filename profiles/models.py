from django.db import models
from .generate import generate_invite_code
from django.contrib.auth.models import User
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, unique=True, null=True)
    invite_code = models.CharField(max_length=6, unique=True, blank=True)
    referred_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='ref_by')


    def __str__(self) -> str:
        return f"{self.user.username}-{self.invite_code}"
    
    def get_reffered_profiles(self):
        qs = Profile.objects.all()

        my_recs = []
        for profile in qs:
            if profile.referred_by == self.user:
                my_recs.append(profile)
                # numbers.append(profile.phone)
        return my_recs

    def save(self, *args, **kwargs):
        if self.invite_code == "":
            code = generate_invite_code()
            self.invite_code = code
        super().save(*args, **kwargs)