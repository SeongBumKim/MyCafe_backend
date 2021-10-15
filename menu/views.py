from django.db.models.query import QuerySet
from rest_framework.response import Response
from rest_framework.decorators import api_view

from menu.models import Menu, Order
from menu.serializer import MenuSerializer, OrderSerializer


@api_view(['GET'])
def menu_list(request):
    menus = Menu.objects.all()
    serializer = MenuSerializer(menus, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def menu_detail(request, pk):
    print(pk)
    menu = Menu.objects.get(id=pk)
    serializer = MenuSerializer(menu, many=False)
   
    return Response(serializer.data)

# @api_view(['GET'])
# def menu_search(request, keyword):
#     pass


@api_view(['GET'])
def order_list(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)


# @api_view(['POST'])
# def book_create(request):
#     serializer = BookSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)


# @api_view(['PUT'])
# def book_update(request, pk):
#     book = Book.objects.get(id=pk)
#     serializer = BookSerializer(instance=book, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)


# @api_view(['DELETE'])
# def book_delete(request, pk):
#     book = Book.objects.get(id=pk)
#     book.delete()
#     return Response('Deleted')

@api_view(['GET'])
def menu_category_list(request, ca):
    menus = Menu.objects.filter(category=ca)
    serializer = MenuSerializer(menus, many=True)
    return Response(serializer.data)

