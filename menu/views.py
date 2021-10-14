from rest_framework.response import Response
from rest_framework.decorators import api_view

from menu.models import Menu
from menu.serializer import MenuSerializer


@api_view(['GET'])
def menu_list(request):
    menus = Menu.objects.all()
    serializer = MenuSerializer(menus, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def menu_detail(request, pk):
    menu = Menu.objects.get(id=pk)
    serializer = MenuSerializer(book, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def menu_search(request, keyword):
    pass


@api_view(['POST'])
def book_create(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
def book_update(request, pk):
    book = Book.objects.get(id=pk)
    serializer = BookSerializer(instance=book, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def book_delete(request, pk):
    book = Book.objects.get(id=pk)
    book.delete()
    return Response('Deleted')

@api_view(['GET'])
def menu_catagory_list(request, catagory):
    menus = Menu.objects()
    serializer = MenuSerializer(menus, many=True)
    return Response(serializer.data)

