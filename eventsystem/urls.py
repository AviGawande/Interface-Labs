from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from events import views as event_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('events.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='event-list'), name='logout'),
    path('register/', event_views.register, name='register'),
]