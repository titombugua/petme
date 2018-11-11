from __future__ import unicode_literals

from django.conf import settings
from django.contrib.contenttypes.models import ContentType
# from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.utils import timezone
from django.utils.safestring import mark_safe
from django.utils.text import slugify


from markdown_deux import markdown

from .utils import get_read_time
# Create your models here.
# MVC MODEL VIEW CONTROLLER


#Post.objects.all()
#Post.objects.create(user=user, title="Some time")


class Address(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    doorNo = models.CharField(max_length=50 , null=True )
    street=models.CharField(max_length=50 , null=True)
    AUH = 'Abu Dhabi'
    AJM = 'Ajman'
    SHJ = 'Sharjah'
    DXB = 'Dubai'
    FUJ = 'Fujairah'
    RAK = 'Ras Al Khaimah'  
    UAQ = 'Umm Al Quwain'


    cityChoices = (
        (AUH, 'Abu Dhabi'),
        (AJM, 'Ajman'),
        (SHJ, 'Sharjah'),
        (DXB, 'Dubai'),
        (FUJ, 'Fujairah'),
        (RAK, 'Ras Al Khaimah'),
        (UAQ, 'Umm al Quwain'),

        )   


    city = models.CharField(max_length=30, choices=cityChoices)
    emirate=models.CharField(max_length=30, choices=cityChoices)
    zipCode=models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.street





class PetsInfo(models.Model):    
    petId = models.AutoField(primary_key=True)
    petName  = models.CharField(max_length=30)
    petBreed = models.CharField(max_length=30)
    image = models.ImageField(upload_to="/uploads", null=True)

    # files = models.ForeignKey(files, on_delete=models.CASCADE)

# GENDER CHOICES
    MALE = 'M'
    FEMALE = 'F'
    genderChoices = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),

        )

# FAVORITE THINGS CHOICES
  

    gender = models.CharField(max_length=30, choices=genderChoices)
    birthday=models.DateField()
    w1 = 'w1'
    w2 = 'w2'
    w3 = 'w3'
    w4 = 'w4'
    weightChoices = (
        (w1, '0-25 lbs'),
        (w2, '25-50 lbs'),
        (w3, '50-100 lbs'),
        (w4, '100+ lbs'),
        )
    weight = models.CharField(max_length=30, choices=weightChoices)
    
    favoriteThings = models.CharField(max_length=30)
    food = models.CharField(max_length=500)
    anythingElse = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.petName



class PetsPersonalInfo(models.Model): 
    petId = models.ForeignKey(PetsInfo, on_delete=models.CASCADE)
    age = models.IntegerField()
    color = models.CharField(max_length=20)
    identification = models.CharField(max_length=100)


    def __str__(self):
        return self.identification
# 
class petInfo(models.Model):    
    petId = models.ForeignKey(PetsInfo, on_delete=models.CASCADE)
    petPersonalInfo=models.ForeignKey(PetsPersonalInfo, on_delete=models.CASCADE)
    def __str__(self):
        return self.petPersonalInfo.identification
# 


class ownerInfo(models.Model):
    oId = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    petInfo = models.ForeignKey(petInfo, on_delete=models.CASCADE)



# 

class Certification(models.Model):
    name = models.CharField(max_length=200)
    startDate=models.DateField()
    endDate = models.DateField()
    affiliation=models.CharField(max_length=200)


class Location(models.Model):
    location = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
    workingHours= models.CharField(max_length=50)



class VetInfo(models.Model):
    vId = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    certification = models.ForeignKey(Certification, on_delete=models.CASCADE)



class jobsList(models.Model):
    jId = models.AutoField(primary_key=True)
    petId = models.ForeignKey(PetsInfo, on_delete=models.CASCADE)
    jobName = models.CharField(max_length=30)
    jobCategories = models.CharField(max_length=30)


class jobExperience(models.Model):
    jeId = models.AutoField(primary_key=True)
    jId = models.ForeignKey(jobsList, on_delete=models.CASCADE)
    noOfYears = models.IntegerField()

class careTakerInfo(models.Model):
    ctId = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    jobExperience = models.ForeignKey(jobExperience, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_name


class petServices(models.Model):
    psId = models.AutoField(primary_key=True)
    petId = models.ForeignKey(PetsInfo, on_delete=models.CASCADE)
    serviceName = models.CharField(max_length=30)
    seviceCost = models.IntegerField()
    serviceDuration = models.CharField(max_length=30)




class rescueOrganizations(models.Model):
    roId = models.AutoField(primary_key=True)
    organizationName = models.CharField(max_length=30)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    webSite = models.CharField(max_length=30)
    facebookLink = models.CharField(max_length=30)
    

class petFriendlyVenue(models.Model):
    place = models.CharField(max_length=30)
    landmark = models.CharField(max_length=30)
    street = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    emirate = models.CharField(max_length=30)
    zipCode = models.IntegerField()
    latitude = models.IntegerField()
    logitude = models.IntegerField()

    
class lostAndFound(models.Model):
    lfId = models.AutoField(primary_key=True)
    oId = models.ForeignKey(ownerInfo, on_delete=models.CASCADE)
    reportingActivity = models.CharField(max_length=30)
    date = models.DateField()
    emirate = models.CharField(max_length=30)
    petInfo = models.ForeignKey(petInfo, on_delete=models.CASCADE)



class petWas(models.Model):
    specifically = models.CharField(max_length=300)
    def __str__(self):
        return self.specifically


class petLostFoundInfo(models.Model):
# typeOfPet = models.ForeignKey(typeOfPet, on_delete=models.CASCADE)
# typeOfPet = models.ManyToManyField(typeOfPet)
    typeOfPet = models.CharField(max_length=30)
    breed = models.CharField(max_length=30)

    MALE = 'M'
    FEMALE = 'F'
    genderChoices = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),

        )

    gender = models.CharField(max_length=30, choices=genderChoices)
    color = models.CharField(max_length=30)
    age=models.IntegerField()
    # size=models.ManyToManyField(weight)
    w1 = 'w1'
    w2 = 'w2'
    w3 = 'w3'
    w4 = 'w4'
    weightChoices = (
        (w1, '0-25 lbs'),
        (w2, '25-50 lbs'),
        (w3, '50-100 lbs'),
        (w4, '100+ lbs'),
        )
    weight = models.CharField(max_length=30, choices=weightChoices)
    

    # petWas = models.ManyToManyField(petWas) 
    petWas = models.ForeignKey(petWas, on_delete=models.CASCADE)



    image = models.ImageField(upload_to='images/', null=True)  

    shelter=models.CharField(max_length=30)
    additionalInfo=models.CharField(max_length=30, null=True)
    additionalData=models.CharField(max_length=30, null=True)



    





class faq(models.Model):
    faqId = models.AutoField(primary_key=True)
    question = models.CharField(max_length=200)
    answers = models.TextField()

    Pet_Me_Question = 'Pet-Me-Question'
    General_Question = 'General-Question'
    faqCategories = (
        (Pet_Me_Question, 'Pet-Me-Questions'),
        (General_Question, 'General-Question'),

        )

    category = models.CharField(max_length=50, choices=faqCategories)
    def __str__(self):
        return self.category




class petMeServices(models.Model):
    sId = models.AutoField(primary_key=True)
    # petId = models.ForeignKey(PetsInfo, on_delete=models.CASCADE)
    pets = models.CharField(max_length=30)
    services = models.CharField(max_length=30)
    created = models.DateField()










# class PostManager(models.Manager):
#     def active(self, *args, **kwargs):
#         # Post.objects.all() = super(PostManager, self).all()
#         return super(PostManager, self).filter(draft=False).filter(publish__lte=timezone.now())


# def upload_location(instance, filename):
#     #filebase, extension = filename.split(".")
#     #return "%s/%s.%s" %(instance.id, instance.id, extension)
#     PostModel = instance.__class__
#     new_id = PostModel.objects.order_by("id").last().id + 1
#     """
#     instance.__class__ gets the model Post. We must use this method because the model is defined below.
#     Then create a queryset ordered by the "id"s of each object, 
#     Then we get the last object in the queryset with `.last()`
#     Which will give us the most recently created Model instance
#     We add 1 to it, so we get what should be the same id as the the post we are creating.
#     """
#     return "%s/%s" %(new_id, filename)

# class Post(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
#     title = models.CharField(max_length=120)
#     slug = models.SlugField(unique=True)
#     image = models.ImageField(upload_to=upload_location, 
#             null=True, 
#             blank=True, 
#             width_field="width_field", 
#             height_field="height_field")
#     height_field = models.IntegerField(default=0)
#     width_field = models.IntegerField(default=0)
#     content = models.TextField()
#     draft = models.BooleanField(default=False)
#     publish = models.DateField(auto_now=False, auto_now_add=False)
#     read_time =  models.IntegerField(default=0) # models.TimeField(null=True, blank=True) #assume minutes
#     updated = models.DateTimeField(auto_now=True, auto_now_add=False)
#     timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

#     objects = PostManager()

#     def __unicode__(self):
#         return self.title

#     def __str__(self):
#         return self.title

#     def get_absolute_url(self):
#         return reverse("posts:detail", kwargs={"slug": self.slug})

#     def get_api_url(self):
#         return reverse("posts-api:detail", kwargs={"slug": self.slug})
    
#     class Meta:
#         ordering = ["-timestamp", "-updated"]

#     def get_markdown(self):
#         content = self.content
#         markdown_text = markdown(content)
#         return mark_safe(markdown_text)

#     @property
#     def comments(self):
#         instance = self
#         qs = Comment.objects.filter_by_instance(instance)
#         return qs

#     @property
#     def get_content_type(self):
#         instance = self
#         content_type = ContentType.objects.get_for_model(instance.__class__)
#         return content_type


# def create_slug(instance, new_slug=None):
#     slug = slugify(instance.title)
#     if new_slug is not None:
#         slug = new_slug
#     qs = Post.objects.filter(slug=slug).order_by("-id")
#     exists = qs.exists()
#     if exists:
#         new_slug = "%s-%s" %(slug, qs.first().id)
#         return create_slug(instance, new_slug=new_slug)
#     return slug


# def pre_save_post_receiver(sender, instance, *args, **kwargs):
#     if not instance.slug:
#         instance.slug = create_slug(instance)

#     if instance.content:
#         html_string = instance.get_markdown()
#         read_time_var = get_read_time(html_string)
#         instance.read_time = read_time_var


# pre_save.connect(pre_save_post_receiver, sender=Post)










