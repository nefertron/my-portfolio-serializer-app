from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views


profile_router = DefaultRouter()
profile_router.register(r'Profile', ProfileViewSet)  # Provide a valid basename

introduction_router = DefaultRouter()
introduction_router.register(r'Introduction', IntroductionViewSet)  # Provide a valid basename

projects_router = DefaultRouter()
projects_router.register(r'Projects', ProjectsViewSet)  # Provide a valid basename

experiences_router = DefaultRouter()
experiences_router.register(r'Experiences', ExperiencesViewSet)  # Provide a valid basename

languages_router = DefaultRouter()
languages_router.register(r'Languages', LanguagesViewSet)  # Provide a valid basename

about_router = DefaultRouter()
about_router.register(r'About', AboutViewSet)  # Provide a valid basename

contact_router = DefaultRouter()
contact_router.register(r'Contact', ContactViewSet)  # Provide a valid basename

message_router = DefaultRouter()
message_router.register(r'Message', MessageViewSet)  # Provide a valid basename


urlpatterns = [
    path('profile/', include(profile_router.urls)),
    path('introduction/', include(introduction_router.urls)),
    path('projects/', include(projects_router.urls)),
    path('experiences/', include(experiences_router.urls)),
    path('languages/', include(languages_router.urls)),
    path('about/', include(about_router.urls)),
    path('contact/', include(contact_router.urls)),
    path('message/', include(message_router.urls)),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
