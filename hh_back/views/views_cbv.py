from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView

from back.models import *

from back.serializers import TourSerializer, AboutSerializer, UserSerializer, CommentSerializer
from rest_framework.response import Response
from django.shortcuts import Http404


class UserListAPIView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get_object(self, pk):
        try:
            return User.objects.get(id=pk)
        except User.DoesNotExist as e:
            raise Http404

    def get(self, request, pk=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk=None):
        user = self.get_object(pk)
        serializer = UserSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk=None):
        user = self.get_object(pk)
        user.delete()
        return Response({'message': 'deleted'}, status=204)


class TourListAPIView(APIView):
    def get(self, request):
        tours = Tour.objects.all()
        serializer = TourSerializer(tours, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TourSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class TourDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Tour.objects.get(id=pk)
        except Tour.DoesNotExist as e:
            raise Http404

    def get(self, request, pk=None):
        tour = request.get_object(pk)
        serializer = TourSerializer(tour)
        return Response(serializer.data)

    def put(self, request, pk=None):
        tour = request.get_object(pk)
        serializer = TourSerializer(instance=tour, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class CommentAPIView(APIView):
    def get_object(self, pk):
        try:
            comments = Comment.objects.get(id=pk)
            return comments
        except Comment.DoesNotExist as e:
            raise Http404

    def get(self, request, pk=None):
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def put(self, request, pk=None):
        comment = self.get_object(pk)
        user = User.objects.get(username=request.user.username)
        request.data.update({'user_id': user.id})
        serializer = CommentSerializer(instance=comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        print(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk=None):
        comment = self.get_object(pk)
        comment.delete()
        return Response({'message': 'deleted'}, status=200)
