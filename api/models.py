from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from multiselectfield import MultiSelectField

# Create your models here.

selection_values = (
    ('none','None'),
    ('daily','Daily'),
    ('weekly','Weekly'),

)
shift_values = (
    ('morning shift','Morning Shift'),
   
)

days= (
    ('1','Monday'),
    ('2' ,'Tuesday'),
    ('3' ,'Wednesday'),
    ('4' ,'Thursday'),
    ('5' ,'Friday'),
    ('6' ,'Saturday'), 
    ('0' ,'Sunday'),
)
class UserManager(BaseUserManager):

	def create_user(self,email,password,**extra_fields):
		if not email:
			raise ValueError('Users must have an email address')


		user = self.model(email = self.normalize_email(email))
		user = self.model(email=email, **extra_fields)
		user.set_password(password)
		user.save(using = self._db)
		return user


	def create_superuser(self,email,password):

		if password is None:
			raise TypeError('superuser must have a password')

		user = self.create_user(email,password)
		user.is_superuser = True
		user.is_staff = True
		user.save()

		return user


class User(AbstractBaseUser, PermissionsMixin):
	id = models.AutoField(primary_key=True)
	first_name = models.CharField(_('first name'), max_length=30, blank=True, null=True)
	last_name = models.CharField(_('last name'), max_length=150, blank=True, null=True)	
	email = models.CharField(unique=True,max_length=50)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default = False)
	is_superuser = models.BooleanField(default = False)
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []
	objects =UserManager()

	def __str__(self):
		return self.email

	class Meta:
		db_table = "login"

class Shift(models.Model):
    title = models.CharField(max_length=100)
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False)
    start_time = models.TimeField(auto_now=False, auto_now_add=False)
    end_time = models.TimeField(auto_now=False, auto_now_add=False)
    repeat  = models.CharField(max_length=255, choices=selection_values)
    shift = models.CharField(max_length=255, choices=shift_values)
    weekdays =MultiSelectField( choices=days,max_choices=7,max_length=15)
    client = models.ForeignKey(User,on_delete=models.CASCADE)