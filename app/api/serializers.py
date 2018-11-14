from rest_framework import serializers
from rest_framework.serializers import (
    HyperlinkedIdentityField,
    HyperlinkedModelSerializer,
    ModelSerializer,
    ListSerializer,
    SerializerMethodField
    )


from accounts.api.serializers import UserDetailSerializer

from app.models import *


# user=UserDetailSerializer()






    

class AddressSerializer(HyperlinkedModelSerializer):
    # user=UserDetailSerializer()
    class Meta:
        model = Address
        fields = (
        'url','id', 'user','doorNo', 'street', 'city','emirate','zipCode'
        )


# post_detail_url = HyperlinkedIdentityField(
#         view_name='address-api:detail',
#         # lookup_field='slug'
#         )
class favoriteThingsSerializer(ModelSerializer):

    class Meta:
        model = favoriteThings
        fields = ('url', 'favoriteThings')



class PetInfoCreateUpdateSerializer(ModelSerializer):
    # favorite=favoriteThingsSerializer(many=True)  

    # favorite = serializers.StringRelatedField(many=True)
    favorite = serializers.JSONField()

   
    class Meta:
        model = PetsInfo
        fields = [
        'url','petId', 'petName','gender','image', 'birthday', 'weight', 'favorite', 'food', 'anythingElse'
        ]

    # def create(self, validated_data):
    #     favorite_data = validated_data.pop('favorite')
    #     petsinfo = PetsInfo.objects.create(**validated_data)
    #     for favorite_data in favorite_data:
    #         favoriteThings.objects.create(petsinfo=petsinfo, **favorite_data)
    #     return petsinfo





# post_detail_url = HyperlinkedIdentityField(
#         view_name='address-api:detail',
#         # lookup_field='slug'
#         )



class PetPersonalInfoCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = PetsPersonalInfo
        fields = [
        'url','petId','age','color','identification'
        ]




# 
class petInfoSerializer(ModelSerializer):
    class Meta:
        model = petInfo
        fields = ('url','petId', 'petPersonalInfo')

# 

class petSerializer(ModelSerializer):

    class Meta:
        model = pet
        fields = ('url', 'name')




class ownerInfoSerializer(ModelSerializer):
    # user=UserDetailSerializer()
    

    class Meta:
        model = ownerInfo
        fields = ('url', 'first_name','last_name', 'gender', 'street_address', 'city', 'pet')






class CertificationSerializer(ModelSerializer):
    class Meta:
        model = Certification
        fields = [
       'url', 'id','name','startDate','endDate','affiliation'
        ]

class LocationSerializer(ModelSerializer):
    class Meta:
        model = Location
        fields = [
        'url','id','location','phone','workingHours'
        ]


class VetInfoCreateUpdateSerializer(ModelSerializer):

    # certification = CertificationSerializer()
    # location = LocationSerializer()


    class Meta:
        model = VetInfo
        fields = ('url','vId','name', 'mobile', 'address', 'phone', 'workingHours','latitude','logitude',)



class jobsListSerializer(ModelSerializer):
    class Meta:
        model = jobsList
        fields = ('url','jId','petId', 'jobName', 'jobCategories')

class jobExperienceSerializer(ModelSerializer):
    class Meta:
        model = jobExperience
        fields = ('url','jeId','jId','noOfYears')



class careTakerInfoSerializer(ModelSerializer):
    # user=UserDetailSerializer()
    class Meta:
        model = careTakerInfo
        fields = ('url', 'first_name','last_name', 'gender', 'street_address', 'city', 'pet')




class petServicesSerializer(ModelSerializer):
    class Meta:
        model = petServices
        fields = ('url','psId','petId', 'serviceName', 'seviceCost','serviceDuration')


# 


class rescueOrganizationsSerializer(ModelSerializer ):
    # location = LocationSerializer()

    class Meta:
        model = rescueOrganizations
        fields = ('url','roId','organizationName','description', 'location', 'webSite', 'facebookLink')



class petFriendlyVenueSerializer(ModelSerializer):
    class Meta:
        model = petFriendlyVenue
        fields = ('url','id', 'place', 'landmark', 'street', 'city', 'emirate', 'zipCode', 'latitude', 'logitude')

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
        fields = ('url', 'faqId', 'question','answers','faqCategory')
       
     

        
class petMeServicesSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = petMeServices
        fields = ('url', 'sId','pets','services', 'created')











