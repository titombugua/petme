from django.contrib import admin

# Register your models here.
from app.models import *

class PetsInfoModelAdmin(admin.ModelAdmin):
	# list_display = ["title", "updated", "timestamp"]
	# list_display_links = ["updated"]
	# list_editable = ["title"]
	# list_filter = ["updated", "timestamp"]

	# search_fields = ["title", "content"]
	class Meta:
		model = PetsInfo


admin.site.register(Address)

admin.site.register(ownerInfo)

	
admin.site.register(careTakerInfo)
admin.site.register(PetsInfo)
admin.site.register(VetInfo)
admin.site.register(jobsList)
admin.site.register(jobExperience)
admin.site.register(petServices)
admin.site.register(rescueOrganizations)
admin.site.register(PetsPersonalInfo)
admin.site.register(petInfo)
admin.site.register(Location)

admin.site.register(Certification)
admin.site.register(petFriendlyVenue)
admin.site.register(lostAndFound)
admin.site.register(petWas)
# admin.site.register(files)
admin.site.register(petLostFoundInfo)
admin.site.register(faq)
admin.site.register(petMeServices)

