from django.urls import path
from . import views

urlpatterns = [
    path('item/', views.BookList.as_view(), name="item_list"),
    path('item/<int:pk>', views.BookDetail.as_view(), name="book_detail")
]
