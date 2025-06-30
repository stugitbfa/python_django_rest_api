from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from apps.blogs.serializers import *
from apps.blogs.models import *

# https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status
# class BlogListAPI:
#     # LISTAPI
#     # POST - create record
#     # GET - get all records
#     @api_view(['GET', 'POST'])
#     def BlogListAPIFuncView(self, request):
#         if request.method == 'GET':
#             querySet = Blog.objects.all()
#             serializer = BlogSerializer(querySet, many=True)
#             context = {
#                 'data': serializer.data
#             }
#             return Response(context, status=status.HTTP_200_OK)

#         if request.method == 'POST':
#             serializer = BlogSerializer(data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 context = {
#                     'data':serializer.data,
#                     'message':"Record inserted successfully"
#                 }
#                 return Response(context, status=status.HTTP_201_CREATED)
#             else:
#                 context = {
#                     'ERROR': serializer.errors,
#                     'Message': 'Oops, Something went wrong'
#                 }
#                 return Response(context, status=status.HTTP_400_BAD_REQUEST)

#     # DETAILAPI
#     # ID - required
#     # GET - get specific record
#     # PUT - update all fileds specific record
#     # PATCH - update fields partially specific record
#     # DELETE - delete specific record
#     @api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
#     def BlogDetailAPIFuncView(self, request, blog_id):
#         if request.method == 'GET':
#             pass

#         if request.method == 'PUT':
#             pass

#         if request.method == 'PATCH':
#             pass

#         if request.method == 'DELETE':
#             pass


# api_object = BlogListAPI()

@api_view(['GET', 'POST'])
def BlogListAPIFuncView(request):
    if request.method == 'GET':
        querySet = Blog.objects.all()
        serializer = BlogSerializer(querySet, many=True)
        context = {
            'data': serializer.data
        }
        return Response(context, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            context = {
                'data':serializer.data,
                'message':"Record inserted successfully"
            }
            return Response(context, status=status.HTTP_201_CREATED)
        else:
            context = {
                'ERROR': serializer.errors,
                'Message': 'Oops, Something went wrong'
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def BlogDetailAPIFuncView(request, blog_id):
    try:
        querySet = Blog.objects.get(id=blog_id)
        print(querySet)
    except Blog.DoesNotExist:
        return Response({'Message':"Blog not found"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = BlogSerializer(querySet)
        context = {
            'data': serializer.data
        }
        return Response(context, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        serializer = BlogSerializer(querySet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            context = {
                'data':serializer.data,
                'message':"Record updated successfully"
            }
            return Response(context, status=status.HTTP_200_OK)
        else:
            context = {
                'ERROR': serializer.errors,
                'Message': 'Oops, Something went wrong'
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PATCH':
        serializer = BlogSerializer(querySet, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            context = {
                'data':serializer.data,
                'message':"Record updated successfully"
            }
            return Response(context, status=status.HTTP_200_OK)
        else:
            context = {
                'ERROR': serializer.errors,
                'Message': 'Oops, Something went wrong'
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)


    if request.method == 'DELETE':
        querySet.delete()
        return Response({'Message': "data deleted successfully"}, status=status.HTTP_204_NO_CONTENT)