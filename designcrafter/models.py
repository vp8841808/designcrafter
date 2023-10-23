from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class Crafter(AbstractBaseUser):
    crafter_name = models.CharField(max_length=100,null=True)
    crafter_email = models.EmailField(max_length=150,null=True)

    class Meta:
        db_table = "crafter_data"

class designer(AbstractBaseUser):
    designer_name = models.CharField(max_length=100,null=True)
    designer_email = models.EmailField(max_length=150,null=True)
    STATUS_CHOICES = [
        ('finished', 'Finished'),
        ('pending', 'Pending'),
    ]

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='pending',
    )

    class Meta:
        db_table = 'designer_data'

class Newuser(models.Model):
    user_name = models.CharField(max_length=100,null=True)
    user_email = models.EmailField(max_length=150,null=True)
    user_mobile = models.CharField(max_length=15,null=True)
    user_otp = models.CharField(max_length=50,null=True)
    password = models.CharField(max_length=100,null=True)

    STATUS_CHOICES = [
        ('enable','Enable'),
        ('disable','Disable'),
    ]

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='enabled',
   
    )
    
    class Meta:
        db_table = 'dc_user_data'

class dc_category(models.Model):
    category_id = models.AutoField(primary_key=True)
    cat_name = models.CharField(max_length=150,null=True)
    cat_image = models.CharField(max_length=150,null=True)
    
    STATUS_CHOICES = [
        ('enabled', 'Enabled'),
        ('disable', 'Disabled'),
    ]

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='pending',
    )

    class Meta:
        db_table = 'dc_category'

class dc_designs(models.Model):
    design_size_id = models.AutoField(primary_key=True)
    design_size_fk = models.ForeignKey(dc_category, on_delete=models.CASCADE) 
    design_title = models.CharField(max_length=100,null=True)
    design_thumb = models.CharField(max_length=100,null=True)
    STATUS_CHOICES = [
        ('enabled', 'Enabled'),
        ('disable', 'Disabled'),
    ]

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='pending',
    )

    design_discount = models.CharField(max_length=100,null=True)

    class Meta:
        db_table = 'dc_designs'

class dc_design_size(models.Model):
    design_size_id = models.AutoField(primary_key=True)
    design_size_fk = models.ForeignKey(dc_designs, on_delete=models.CASCADE) 
    design_img = models.CharField(max_length=100,null=True)
    design_size = models.CharField(max_length=100,null=True)
    design_price = models.CharField(max_length=100,)    
    STATUS_CHOICES = [
        ('enabled', 'Enabled'),
        ('disable', 'Disabled'),
    ]

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='pending',
    )
    
    class Meta:
        db_table = 'dc_design_size'

class visits(models.Model):
    visit_id = models.AutoField(primary_key=True)
    user_id_fk = models.ForeignKey(Newuser, on_delete=models.CASCADE)
    id = models.IntegerField(null=True)
    STATUS_CHOICES = [
        ('design','Design'),
        ('category','Category'),
    ]

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='empty',
    )

    visit_date = models.DateTimeField(max_length=100,null=True)

    class Meta:
        db_table = 'dc_visits'