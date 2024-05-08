from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/', views.voter_register, name='voter_register'),  # Registration page
    path('home/', views.voter_home, name='voter_home'),  # Voter home page (list of candidates)
    path('vote/<int:candidate_id>/', views.vote, name='vote'),  # Voting page
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
