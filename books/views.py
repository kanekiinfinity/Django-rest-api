from rest_framework import generics


from .serializers import BooksSerializer

from .models import Book


# Create your views here.


class BookListApiView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer


class BookDetailApiView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer



class BookDeleteApiView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer



class BookUpdateApiView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer


class BookCreateApiView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer


