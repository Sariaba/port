from django.urls import path
from app import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', admin.site.urls),
    path("", views.home, name="home"),
    path("home", views.home, name="home"),
    path("about", views.about, name="about"),
    path("education", views.education, name="education"),
    path("skills", views.skills, name="skills"),
    path("contact", views.contact, name="contact"),
]