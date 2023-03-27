from django.views.generic import TemplateView
from rest_framework import generics, viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Category, Favorites, Channel, Users
from .serializers import CategoryModelSerializer, FavoriteModelSerializer, UsersModelSerializer


# channel_qs2 = Channel.objects.all()

class HomeView(TemplateView):
    template_name = 'usable_templates/index-2.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context



class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer

class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersModelSerializer

    def create(self, request, *args, **kwargs):
        user_id = request.data.get('user_id', None)
        channel_id = request.data.get('channel_id', None)
        print(user_id, channel_id)
        if user_id and channel_id:
            obj, created = Favorites.objects.get_or_create(user_id=user_id, channel_id=channel_id,
                                                           defaults={'user_id': user_id, 'channel_id': channel_id})
            print(created, obj)
            if not created:
                raise ValidationError('Объект уже имеется в базе.')
            serializer = FavoriteModelSerializer(obj, many=False)
            return Response(serializer.data)

        else:
            raise ValidationError('Выданы неправильные данные.')

    def list(self, request, *args, **kwargs):




def add_to_favorite(request, channel_id):
    request.GET
    if request.method == 'POST':
        channel = Channel.objects.get(pk=channel_id)

        user = request.POST.get('user_id', None)
        obj = Users.objects.get_or_create(user=user, defaults={'user': user})
        Favorites.objects.create(user=obj, channel=channel)

















