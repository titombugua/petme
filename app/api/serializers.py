from rest_framework import serializers
from rest_framework.serializers import (
    HyperlinkedIdentityField,
    HyperlinkedModelSerializer,
    ModelSerializer,
    SerializerMethodField
    )


from accounts.api.serializers import UserDetailSerializer

from app.models import *


# user=UserDetailSerializer()

class AddressSerializer(ModelSerializer):
    # user=UserDetailSerializer()
    class Meta:
        model = Address
        fields = (
        'id', 'user','doorNo', 'street', 'city','emirate','zipCode'
        )


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
        fields = ('petId', 'petPersonalInfo')

# 
class ownerInfoSerializer(ModelSerializer):
    # user=UserDetailSerializer()

    class Meta:
        model = ownerInfo
        fields = ('oId', 'user', 'petInfo')




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
        'id','location','phone','workingHours'
        ]


class VetInfoCreateUpdateSerializer(ModelSerializer):

    # certification = CertificationSerializer()
    # location = LocationSerializer()


    class Meta:
        model = VetInfo
        fields = ('vId','user', 'location', 'certification')



class jobsListSerializer(ModelSerializer):
    class Meta:
        model = jobsList
        fields = ('jId','petId', 'jobName', 'jobCategories')

class jobExperienceSerializer(ModelSerializer):
    class Meta:
        model = jobExperience
        fields = ('jeId','jId','noOfYears')



class careTakerInfoSerializer(ModelSerializer):
    # user=UserDetailSerializer()
    class Meta:
        model = careTakerInfo
        fields = ('ctId', 'user', 'jobExperience')




class petServicesSerializer(ModelSerializer):
    class Meta:
        model = petServices
        fields = ('psId','petId', 'serviceName', 'seviceCost','serviceDuration')


# 


class rescueOrganizationsSerializer(ModelSerializer ):
    location = LocationSerializer()

    class Meta:
        model = rescueOrganizations
        fields = ('roId','organizationName', 'location', 'webSite', 'facebookLink')



class petFriendlyVenueSerializer(ModelSerializer):
    class Meta:
        model = petFriendlyVenue
        fields = ('id', 'place', 'landmark', 'street', 'city', 'emirate', 'zipCode', 'latitude', 'logitude')

class lostAndFoundSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = lostAndFound
        fields = ('url', 'lfId','oId', 'reportingActivity', 'date', 'emirate','petInfo')


class petWasSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = petWas
        fields = ('url', 'id','specifically')


class petLostFoundInfoSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = petLostFoundInfo
        fields = ('url', 'typeOfPet', 'breed','gender', 'color', 'age', 'petWas', 'image')




    # def create(self, validated_data):
    #     tracks_data = validated_data.pop('petWas')
    #     Plaf = petLostFoundInfo.objects.create(**validated_data)
    #     for track_data in tracks_data:
    #         petWas.objects.create(Plaf=Plaf, **track_data)
    #     return Plaf


class petServicesSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = petServices
        fields = ('url','psId','petId','serviceName', 'seviceCost','serviceDuration')


class faqSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = faq
        fields = ('url', 'faqId', 'question','answers','category')
       
     

        
class petMeServicesSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = petMeServices
        fields = ('url', 'sId','pets','services', 'created')











