# from django.conf import settings
from pyexpat import model
from django.contrib.auth.models import AbstractUser

from django.db import models
# from django.utils import timezone


MALE = "male"
FEMALE = "female"

GENDER_CHOICE = (
    (MALE, "male"),
    (FEMALE, "female")
)


class User(AbstractUser):
    INVALID_CODE = "######"
    full_name = models.CharField(("full name"), max_length=256)
    email = models.EmailField(
        ("email"),
        unique=True,
        error_messages={
            "error": ("Bunday email mavjud."),
        },
        null=True
    )

    bio = models.CharField(max_length=256, null=True, blank=True)
    awatar = models.ImageField(upload_to='awatar/', null=True, blank=True)
    bg_image = models.ImageField(upload_to='bg_image/', null=True, blank=True)
    birth_day = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICE)

    phone = models.CharField(max_length=32, null=True, blank=True)
    website = models.CharField(max_length=256, null=True, blank=True)
    location = models.CharField(max_length=512, null=True, blank=True)

    facebook = models.CharField(max_length=256, null=True, blank=True)
    instagram = models.CharField(max_length=256, null=True, blank=True)
    twitter = models.CharField(max_length=256, null=True, blank=True)
    linkedln = models.CharField(max_length=256, null=True, blank=True)

    flowwing = models.ManyToManyField(
        "self", related_name="user_following", null=True, blank=True)
    followers = models.ManyToManyField(
        "self", related_name="user_follower", null=True, blank=True)
    blocked_users = models.ManyToManyField(
        "self", related_name="blocked_users", null=True, blank=True)

    flowwing_count = models.PositiveIntegerField(null=True, blank=True)
    followers_count = models.PositiveIntegerField(null=True, blank=True)
    blocked_users_count = models.PositiveIntegerField(null=True, blank=True)

    # view or @property in models
    is_online = models.BooleanField(default=False)

    created_at = models.DateTimeField(
        ("date created"), auto_now_add=True, null=True)
    updated_at = models.DateTimeField(("date updated"), auto_now=True)

    # SETTINGS
    USERNAME_FIELD = "email"
    first_name = None
    last_name = None
    REQUIRED_FIELDS = ["username", "full_name"]

    def __str__(self):
        return f"{self.email}"

    class Meta:
        db_table = "user"
        swappable = "AUTH_USER_MODEL"
        verbose_name = ("user")
        verbose_name_plural = ("users")
