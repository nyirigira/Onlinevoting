from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from voting import views  # Import the 'views' module from the 'voting' app

urlpatterns = [
    # Admin interface URL
    path('admin/', admin.site.urls),
    
    # Root URL set to login page with custom template and redirect to home
    path('', auth_views.LoginView.as_view(template_name='voting/login.html', next_page='/home/'), name='login'),

    # Registration page URL
    path('register/', views.voter_register, name='voter_register'),

    # Voter home page URL
    path('home/', views.voter_home, name='voter_home'),

    # Voting page URL
    path('vote/<int:candidate_id>/', views.vote, name='vote'),

    # Include URLs from the 'voting' app
    path('voting/', include('voting.urls')),
]
