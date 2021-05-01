from django.shortcuts import render
import json
from django.http.response import JsonResponse
from back.models import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view


# Create your views here.

@api_view(['GET', 'POST', 'PUT'])
def tour_list(request):
    permission_classes = [IsAuthenticated]
    # // @ts-ignore
    # pk = Recipes['id']
    if request.method == 'GET':
        post_list = Tour.objects.all()
        serializer = TourSerializer(post_list, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TourSerializer(data=request.data)
        if serializer.is_valid():
            print('success')
            serializer.save(author_id=request.user.id)
            return Response(serializer.data)
        else:
            print(serializer.errors)
        return Response(serializer.errors)
    
    elif request.method == 'PUT':
        try:
            tours = Tour.objects.all()
        except Tour.DoesNotExist as e:
            return Response({'message': str(e)}, status=400)
        serializer = TourSerializer(instance=tours, data=request.data)
        if serializer.is_valid():
            # post = serializer.id
            # if str(post) != str(request.user.id):
            #     print('someone else attempts to change')
            #     return JsonResponse({'error': 'not yours'})
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


@csrf_exempt
def tour_detail(request, company_id):
    try:
        company = Tour.objects.get(id=company_id)
    except Tour.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)

    if request.method == 'GET':
        return JsonResponse(company.to_json())

    elif request.method == 'PUT':
        data = json.loads(request.body)
        company.name = data['name']
        company.save()
        return JsonResponse(company.to_json())

    elif request.method == 'DELETE':
        company.delete()
        return JsonResponse({'message': 'deleted'}, status=204)


@csrf_exempt
def comment_list(request):
    if request.method == 'GET':
        comments = Comment.objects.all()
        comments_json = [comment.to_json() for comment in comments]
        return JsonResponse(comments_json, safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body)
        try:
            vacancy = About.objects.create(name=data['name'])
        except Exception as e:
            return JsonResponse({'message': str(e)})

        return JsonResponse(vacancy.to_json())


@csrf_exempt
def comment_detail(request, vacancy_id):
    try:
        comment = Comment.objects.get(id=vacancy_id)
    except Comment.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)

    if request.method == 'GET':
        return JsonResponse(comment.to_json())

    elif request.method == 'PUT':
        data = json.loads(request.body)
        comment.name = data['name']
        comment.save()
        return JsonResponse(Comment.to_json())

    elif request.method == 'DELETE':
        comment.delete()
        return JsonResponse({'message': 'deleted'}, status=204)

