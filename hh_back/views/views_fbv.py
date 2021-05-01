from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from back.models import Tour, About, Comment
from back.serializers import TourSerializer, AboutSerializer, CommentSerializer


@api_view(['GET', 'POST'])
def tour_list(request):
    if request.method == 'GET':
        tours = Tour.objects.filter(name__contains='5').order_by('-id')
        serializer = TourSerializer(tours, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TourSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def tour_detail(request, tour_id):
    try:
        tour = Tour.objects.get(id=tour_id)
    except Tour.DoesNotExist as e:
        return Response({'message': str(e)}, status=400)

    if request.method == 'GET':
        serializer = TourSerializer(tour)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TourSerializer(instance=tour, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'DELETE':
        tour.delete()
        return Response({'message': 'deleted'}, status=204)


@api_view(['GET', 'POST'])
def about_list(request):
    if request.method == 'GET':
        abouts = About.objects.filter(name__contains='5').order_by('-id')
        serializer = AboutSerializer(abouts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AboutSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def about_detail(request, about_id):
    try:
        about = About.objects.get(id=about_id)
    except About.DoesNotExist as e:
        return Response({'message': str(e)}, status=400)

    if request.method == 'GET':
        serializer = AboutSerializer(about)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = AboutSerializer(instance=about, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'DELETE':
        about.delete()
        return Response({'message': 'deleted'}, status=204)


@api_view(['GET', 'POST'])
def comment_list(request):
    if request.method == 'GET':
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)
