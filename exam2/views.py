from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from .models import About, News, TeamMember, Publication, Review, Service, Contact
from .serializers import AboutSerializer, NewsSerializer, TeamMemberSerializer, PublicationSerializer, ReviewSerializer, \
    ServiceSerializer, ContactSerializer
from rest_framework.response import Response
from rest_framework import generics


class ReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [AllowAny]


class AboutListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        abouts = About.objects.all()
        serializer = AboutSerializer(abouts, many=True)
        return Response(serializer.data)


class NewsListView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [AllowAny]


class NewsDetailView(generics.RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [AllowAny]
    lookup_field = 'slug'


class TeamMemberListView(generics.ListAPIView):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer
    permission_classes = [AllowAny]


class TeamMemberDetailView(generics.RetrieveAPIView):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer
    permission_classes = [AllowAny]
    lookup_field = 'slug'


class PublicationListView(generics.ListAPIView):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer
    permission_classes = [AllowAny]


class PublicationDetailView(generics.RetrieveAPIView):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer
    permission_classes = [AllowAny]
    lookup_field = 'slug'


class ReviewListView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [AllowAny]


class ServiceListView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [AllowAny]


class ContactView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [AllowAny]

    # Allow only GET and POST methods
    http_method_names = ['get', 'post']
