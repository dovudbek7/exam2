from django.urls import path
from .views import *
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="My API",
        default_version='v1',
        description="Test description of my API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@myapi.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('about/', AboutListView.as_view(), name='about-list'),
    path('news/', NewsListView.as_view(), name='news-list'),
    path('news/<slug:slug>/', NewsDetailView.as_view(), name='news-detail'),
    path('team-members/', TeamMemberListView.as_view(), name='team-member-list'),
    path('team-members/<slug:slug>/', TeamMemberDetailView.as_view(), name='team-member-detail'),
    path('publications/', PublicationListView.as_view(), name='publication-list'),
    path('publications/<slug:slug>/', PublicationDetailView.as_view(), name='publication-detail'),
    path('reviews/', ReviewListView.as_view(), name='review-list'),
    path('services/', ServiceListView.as_view(), name='service-list'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
