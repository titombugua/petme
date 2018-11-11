from django.db.models import Q
from rest_framework import viewsets


from rest_framework.filters import (
        SearchFilter,
        OrderingFilter,
    )
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView, 
    UpdateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView
    )



from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,

    )

from app.models import *
# from posts.models import Post, Address, PetsInfo, PetsPersonalInfo

from .pagination import PostLimitOffsetPagination, PostPageNumberPagination
from .permissions import IsOwnerOrReadOnly
from .serializers import *

# from .serializers import (
#     PostCreateUpdateSerializer, 
#     PostDetailSerializer, 
#     PostListSerializer,
#     AddressCreateUpdateSerializer,
#     PetInfoCreateUpdateSerializer,
#     PetPersonalInfoCreateUpdateSerializer,
#     )

class addressView(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

# class AddressCreateAPIView(viewsets.ModelViewSet):
#     queryset = Address.objects.all()
#     serializer_class = AddressCreateUpdateSerializer
#     # permission_classes = [IsAuthenticated]
#     permission_classes = [AllowAny]


#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)

class petCreateAPIView(viewsets.ModelViewSet):
    queryset = PetsInfo.objects.all()
    serializer_class = PetInfoCreateUpdateSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]


    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)



class PetsPersonalInfoCreateAPIView(viewsets.ModelViewSet):
    queryset = PetsPersonalInfo.objects.all()
    serializer_class = PetPersonalInfoCreateUpdateSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]


    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)




# 
class petInfoCreateAPIView(viewsets.ModelViewSet):
    queryset = petInfo.objects.all()
    serializer_class = petInfoSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]


    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

class ownerInfoCreateAPIView(viewsets.ModelViewSet):
    queryset = ownerInfo.objects.all()
    serializer_class = ownerInfoSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]


    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)










class CertificationCreateAPIView(viewsets.ModelViewSet):
    queryset = Certification.objects.all()
    serializer_class = CertificationSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]


    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)


class LocationCreateAPIView(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]


    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)



class VetInfoCreateAPIView(viewsets.ModelViewSet):
    queryset = VetInfo.objects.all()
    serializer_class = VetInfoCreateUpdateSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]


    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)



class jobListCreateAPIView(viewsets.ModelViewSet):
    queryset = jobsList.objects.all()
    serializer_class = jobsListSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]


    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)


class jobExperienceCreateAPIView(viewsets.ModelViewSet):
    queryset = jobExperience.objects.all()
    serializer_class = jobExperienceSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]


    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

class careTakerInfoAPIView(viewsets.ModelViewSet):
    queryset = careTakerInfo.objects.all()
    serializer_class = careTakerInfoSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]


    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

class petServicesCreateAPIView(viewsets.ModelViewSet):
    queryset = petServices.objects.all()
    serializer_class = petServicesSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]
    

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

# 

class rescueOrganizationsCreateAPIView(viewsets.ModelViewSet):
    queryset = rescueOrganizations.objects.all()
    serializer_class = rescueOrganizationsSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]


    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)


class petFriendlyVenueCreateAPIView(viewsets.ModelViewSet):
    queryset = petFriendlyVenue.objects.all()
    serializer_class = petFriendlyVenueSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]


    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

class lostAndFoundCreateAPIView(viewsets.ModelViewSet):
    queryset = lostAndFound.objects.all()
    serializer_class = lostAndFoundSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]


    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

class petWasCreateAPIView(viewsets.ModelViewSet):
    queryset = petWas.objects.all()
    serializer_class = petWasSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]




class petLostFoundInfoCreateAPIView(viewsets.ModelViewSet):
    queryset = petLostFoundInfo.objects.all()
    serializer_class = petLostFoundInfoSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]



class faqViewSet(viewsets.ModelViewSet):
    queryset = faq.objects.all()
    serializer_class = faqSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

    






class petMeServicesAPIView(viewsets.ModelViewSet):
    queryset = petMeServices.objects.all()
    serializer_class = petMeServicesSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

















