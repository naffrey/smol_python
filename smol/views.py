from .serializer import ItemSerializer
from rest_framework import generics
from .models import Item
# Create your views here.


def item_list(request):
    item = Item.objects.all().values('name', 'author', 'photo_url')
    item_list = list(item)
    return JsonResponse(item_list, safe=False)
