from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers

from accounts.api.views import *
from .views import petMeServicesView


from .views import *



router = routers.DefaultRouter()

router.register('address', addressView)
router.register('favorite-thing', favoriteThingsView)

router.register('pets-create', petCreateAPIView)
router.register('pp-info', PetsPersonalInfoCreateAPIView)

router.register('vet', VetInfoCreateAPIView)
router.register('location', LocationCreateAPIView)

router.register('certification', CertificationCreateAPIView)
router.register('job-list', jobListCreateAPIView)
router.register('job-experience', jobExperienceCreateAPIView)
router.register('care-taker-info', careTakerInfoAPIView)

 

router.register('pet-services', petServicesCreateAPIView)


router.register('pet-info', petInfoCreateAPIView)


router.register('owner-info', ownerInfoCreateAPIView)


router.register('rescue-info', rescueOrganizationsCreateAPIView)


router.register('friendly-venue', petFriendlyVenueCreateAPIView)


router.register('lostandfound', lostAndFoundCreateAPIView)


router.register('pet-was', petWasCreateAPIView)


router.register('petlost', petLostFoundInfoCreateAPIView)


router.register(r'faq', faqViewSet)


router.register('pet-me-services', petMeServicesView)

urlpatterns = [
  url('', include(router.urls)), 

]















# from .views import (
#     PostCreateAPIView,
#     PostDeleteAPIView,
#     PostDetailAPIView,
#     PostListAPIView,
#     PostUpdateAPIView,
#     AddressCreateAPIView,
#     petCreateAPIView,
#     PetsPersonalInfoCreateAPIView
#     )

# urlpatterns = [
#     # url(r'^$', PostListAPIView.as_view(), name='list'),
#     url(r'^', include(router.urls)),    # url(r'^address/$', AddressCreateAPIView .as_view(), name='address-create'),
#     # url(r'^pet/$', petCreateAPIView.as_view(), name='pet-info'),

    # url(r'^pp-info/$', PetsPersonalInfoCreateAPIView.as_view(), name='pet-personal-info'),
    # url(r'^vet/$', VetInfoCreateAPIView.as_view(), name='vets-info'),
    # url(r'^location/$', LocationCreateAPIView.as_view(), name='location'),
    # url(r'^certification/$', CertificationCreateAPIView.as_view(), name='certification'),

    # url(r'^job-list/$', jobListCreateAPIView.as_view(), name='job-list'),
   #  url(r'^job-experience/$', jobExperienceCreateAPIView.as_view(), name='job-experience'),
   #  url(r'^pet-services/$', petServicesCreateAPIView.as_view(), name='pet-services'),
   #  url(r'^pet-info/$', petInfoCreateAPIView.as_view(), name='pet-info'),


   #  url(r'^owner-info/$', ownerInfoCreateAPIView.as_view(), name='owner-info'),

   # url(r'^rescue-info/$', rescueOrganizationsCreateAPIView.as_view(), name='rescue-info'),
   # url(r'^friendly-venue/$', petFriendlyVenueCreateAPIView.as_view(), name='friendly-venue'),

   # url(r'^lostandfound/$', lostAndFoundCreateAPIView.as_view(), name='friendly-venue'),
   # url(r'^pet-was/$', petWasCreateAPIView.as_view(), name='friendly-venue'),

   # url(r'^petlost/$', petLostFoundInfoCreateAPIView.as_view(), name='friendly-venue'),
   # url(r'^faq/$', faqCreateAPIView.as_view(), name='petlost'),

   # url(r'^pet-me-services/$', petMeServicesAPIView.as_view(), name='pet-services'),
  # url(r'^api/$', faqAPIListCreateView.as_view()),







    # url(r'^create/$', PostCreateAPIView.as_view(), name='create'),
  # url(r'^(?P<pk>[\w-]+)/$', faqAPIListCreateView.as_view(), name='detail'),
    # url(r'^(?P<slug>[\w-]+)/edit/$', PostUpdateAPIView.as_view(), name='update'),
    # url(r'^(?P<slug>[\w-]+)/delete/$', PostDeleteAPIView.as_view(), name='delete'),



