from django.contrib import admin

# Register your models here.
from .models import Candidate

admin.site.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'vote_count' , 'created_at')
    fields = ('name', 'description', 'picture', 'vote_count','created_at')
    readonly_fields = ('created_at', 'vote_count')
    
