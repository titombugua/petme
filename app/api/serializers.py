from rest_framework import serializers
from rest_framework.serializers import (
    HyperlinkedIdentityField,
    HyperlinkedModelSerializer,
    ModelSerializer,
    SerializerMethodField
    )


from accounts.api.serializers import UserDetailSerializer

from app.models import *


user=UserDetailSerializer()

class AddressSerializer(HyperlinkedModelSerializer):
    # user=UserDetailSerializer()
    class Meta:
        model = Address
        fields = [
        'id', 'url', 'doorNo', 'street', 'city','emirate','zipCode'
        ]


# post_detail_url = HyperlinkedIdentityField(
#         view_name='address-api:detail',
#         # lookup_field='slug'
#         )



class PetInfoCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = PetsInfo
        fields = [
        'petId', 'petName','image', 'birthday', 'weight', 'favoriteThings', 'food', 'anythingElse'
        ]


# post_detail_url = HyperlinkedIdentityField(
#         view_name='address-api:detail',
#         # lookup_field='slug'
#         )



class PetPersonalInfoCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = PetsPersonalInfo
        fields = [
        'petId','age','color','identification'
        ]




# 
class petInfoSerializer(ModelSerializer):
    class Meta:
        model = petInfo
        fields = ('petId','url', 'petPersonalInfo')

# 
class ownerInfoSerializer(ModelSerializer):
    user=UserDetailSerializer()

    class Meta:
        model = ownerInfo
        fields = ('oId','url', 'user', 'petInfo')




class CertificationSerializer(ModelSerializer):
    class Meta:
        model = Certification
        fields = [
        'id','name','startDate','endDate','affiliation'
        ]

class LocationSerializer(ModelSerializer):
    class Meta:
        model = Location
        fields = [
        'id','url','location','phone','workingHours'
        ]


class VetInfoCreateUpdateSerializer(ModelSerializer):

    certification = CertificationSerializer()
    location = LocationSerializer()


    class Meta:
        model = VetInfo
        fields = ('vId','user','url', 'location', 'certification')



class jobsListSerializer(ModelSerializer):
    class Meta:
        model = jobsList
        fields = ('jId','petId', 'url', 'jobName', 'jobCategories')

class jobExperienceSerializer(ModelSerializer):
    class Meta:
        model = jobExperience
        fields = ('jeId','jId','url', 'noOfYears')



class careTakerInfoSerializer(ModelSerializer):
    user=UserDetailSerializer()
    class Meta:
        model = careTakerInfo
        fields = ('ctId','url', 'user', 'jobExperience')




class petServicesSerializer(ModelSerializer):
    class Meta:
        model = petServices
        fields = ('psId','petId', 'url', 'serviceName', 'seviceCost','serviceDuration')


# 


class rescueOrganizationsSerializer(ModelSerializer ):
    location = LocationSerializer()

    class Meta:
        model = rescueOrganizations
        fields = ('roId','url', 'organizationName', 'location', 'webSite', 'facebookLink')



class petFriendlyVenueSerializer(ModelSerializer):
    class Meta:
        model = petFriendlyVenue
        fields = ('id','url', 'place', 'landmark', 'street', 'city', 'emirate', 'zipCode', 'latitude', 'logitude')

class lostAndFoundSerializer(ModelSerializer):
    class Meta:
        model = lostAndFound
        fields = ('lfId','url', 'oId', 'reportingActivity', 'date', 'emirate','petInfo')


class petWasSerializer(ModelSerializer):
    class Meta:
        model = petWas
        fields = ('id','specifically')


class petLostFoundInfoSerializer(ModelSerializer):
    class Meta:
        model = petLostFoundInfo
        fields = ('id', 'typeOfPet', 'breed','gender', 'color', 'age', 'petWas', 'image')




    # def create(self, validated_data):
    #     tracks_data = validated_data.pop('petWas')
    #     Plaf = petLostFoundInfo.objects.create(**validated_data)
    #     for track_data in tracks_data:
    #         petWas.objects.create(Plaf=Plaf, **track_data)
    #     return Plaf


class petServicesSerializer(ModelSerializer):
    class Meta:
        model = petServices
        fields = ('psId','petId', 'url', 'serviceName', 'seviceCost','serviceDuration')


class faqSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = faq
        fields = ('faqId', 'question','answers')

        
class petMeServicesSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = petMeServices
        fields = ('sId','pets','services', 'created')




















""""

from posts.models import Post
from posts.api.serializers import PostDetailSerializer


data = {
    "title": "Yeahh buddy",
    "content": "New content",
    "publish": "2016-2-12",
    "slug": "yeah-buddy",
    
}

obj = Post.objects.get(id=2)
new_item = PostDetailSerializer(obj, data=data)
if new_item.is_valid():
    new_item.save()
else:
    print(new_item.errors)


"""