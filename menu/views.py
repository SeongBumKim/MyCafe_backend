from django.contrib.auth.models import User
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


@api_view(['GET'])
def menu_category_list(request, ca):
    menus = Menu.objects.filter(category=ca)
    serializer = MenuSerializer(menus, many=True)
    return Response(serializer.data)

# @api_view(['POST'])
# def login_check(request):
#     data = UserSerializer(request.data) #body에 작성
#     print(data.data) #역 직렬화 데이터 출력
#     try: 
#         login = User.objects.filter(data.email, data.password)
#         serializer = UserSerializer(login)
#         print(serializer.data)
#         return Response(serializer.data)
#     except(Exception): #로그인 실패하면~~
#         print('login fail')
#         return Response({'message': 'login fail'})

