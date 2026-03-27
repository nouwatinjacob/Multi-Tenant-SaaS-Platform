from django.db import models
from django.conf import settings

# Create your models here.
class Role(models.TextChoices):
        OWNER = "owner", "Owner"
        ADMIN = "admin", "Admin"
        MANAGER = "manager", "Manager"
        MEMBER = "member", "Member"

class Membership(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="memberships")
    organization = models.ForeignKey("organizations.Organization", on_delete=models.CASCADE, related_name="memberships")
    role = models.CharField(max_length=50, choices=Role.choices, default=Role.MEMBER)
    is_active = models.BooleanField(default=True)
    joined_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
       constraints = [
           models.UniqueConstraint(fields=["user", "organization"], name="unique_membership")
       ]

    def __str__(self):
        return f"{self.user.email} - {self.organization.name} ({self.role})"