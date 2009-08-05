from danielworth.discography.models import *
from django.contrib import admin

class PROAdmin(admin.ModelAdmin):
    list_display = ('name', 'city')

class ArtistPerformanceAdmin(admin.ModelAdmin):
    list_display = ('artist', 'performance')

admin.site.register(Group)
admin.site.register(License)
admin.site.register(Song)
admin.site.register(Artist)
admin.site.register(Performance)
admin.site.register(ArtistPerformance, ArtistPerformanceAdmin)
admin.site.register(Album)
admin.site.register(Studio)
admin.site.register(Publisher)
admin.site.register(PRO, PROAdmin)
admin.site.register(GroupMembership)
admin.site.register(Distributor)
admin.site.register(Role)
