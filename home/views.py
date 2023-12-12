from functools import partial
from rest_framework.authtoken.models import Token
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from home.models import Student
from .serializers import *
from rest_framework.views import APIView





# Create your views here.

# @api_view(['GET'])
# def home(request):
#     studentObj = Student.objects.all()
#     serializer = StudentSerializer(studentObj, many=True)
#     return Response({'status': 200, "payload": serializer.data})

# @api_view(['POST'])
# def post_student(request):
#     data = request.data
#     serializer = StudentSerializer(data=request.data)
#     if not serializer.is_valid():
#         return Response({"status":403, "msg":"Something went wrong", "errors":serializer.errors})
#     serializer.save()
#     return Response({"status":200,'payload': serializer.data})

# @api_view(['PUT'])
# def update_student(request, id):
#     try:
#         studentobj = Student.objects.get(id=id)
    
#         data = request.data
#         serializer = StudentSerializer(studentobj, data=request.data)
#         if not serializer.is_valid():
#             return Response({"status":403, "msg":"Something went wrong", "errors":serializer.errors})
#         serializer.save()
#         return Response({"status":200,'payload': serializer.data})
#     except Exception as e:
#         return  Response({'status':403, 'msg':e})
    
# @api_view(['PATCH'])
# def modify_student(request, id):
#     try:
#         studentobj = Student.objects.get(id=id)
    
#         data = request.data
#         serializer = StudentSerializer(studentobj, data=request.data, partial=True)
#         if not serializer.is_valid():
#             return Response({"status":403, "msg":"Something went wrong", "errors":serializer.errors})
#         serializer.save()
#         return Response({"status":200,'payload': serializer.data})
#     except Exception as e:
#         return  Response({'status':403, 'msg':e}) # dont send exception in response, rather print
    
# @api_view(['DELETE'])
# def delete_student(request, id):
#     try:
#         studentobj = Student.objects.get(id=id)
#         studentobj.delete()
#         return Response({'status':200, "message":"deleted"})
#     except Exception as e:
#         return  Response({'status':403, 'msg':e})

# @api_view(['GET'])
# def get_book(request):
#     book_objs = Books.objects.all()
#     serializer = BookSerializer(book_objs, many=True)
#     return Response({'statud': 200, 'payload': serializer.data})

#------------------------------------------------------------------------------

from rest_framework.authentication import TokenAuthentication # Token auth
from rest_framework.permissions import IsAuthenticated # Token auth

from rest_framework_simplejwt.authentication import JWTAuthentication

class StudentAPI(APIView):

    # authentication_classes = [TokenAuthentication] # Token auth
    # permission_classes = [IsAuthenticated]          # Token auth

    authentication_classes = [JWTAuthentication] # Token auth
    permission_classes = [IsAuthenticated]          # Token auth

    def get(self, request):
        
        student_obj = Student.objects.all()
        serializer = StudentSerializer(student_obj, many=True)

        print(request.user)

        return Response({'status': 200, 'payload': serializer.data})
        def post(self, request):
            pass
        def patch(self, request):
            pass
        def put(self, request):
            pass
        def delete(self, request):
            pass

#--------------------------------------------------------------------------------------------------------
#JWT AUTHENTICATION
#--------------------------------------------------------------------------------------------------------
from rest_framework_simplejwt.tokens import RefreshToken

class Registeruser(APIView):
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'status':403, 'errors':serializer.errors, 'message':'something went wrong'})
        serializer.save()
        user = User.objects.get(username=serializer.data['username'])
        # token_obj, _ = Token.objects.get_or_create(user=user)
        refresh = RefreshToken.for_user(user)
        return Response({'status':200,'payload':serializer.data,'access_token':str(refresh.access_token), 'refresh_token':str(refresh), 'message':"success"})

