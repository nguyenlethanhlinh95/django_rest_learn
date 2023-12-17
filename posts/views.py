from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Post
from .serializers import PostSerializer
from django.shortcuts import get_object_or_404
from rest_framework import generics
# Create your views here.

@api_view(["GET", "POST"])
def list_create(request:Request):
    if request.method == "POST":
        data = request.data
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "message": "Post created",
                "data": serializer.data
            }
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    posts = Post.objects.all()
    serializer = PostSerializer(instance=posts, many=True)
    response = {
                "message": "Get list successful",
                "data": serializer.data
            }
    return Response(data=response, status=status.HTTP_200_OK)


@api_view(["GET", "PUT", "DELETE"])
def retrieve_update_delete(request:Request, id:int):
    post = get_object_or_404(Post, id=id)
    if request.method == "PUT":
        data = request.data
        serializer = PostSerializer(instance=post, data=data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "message": "Post updated",
                "data": serializer.data
            }
            return Response(data=data, status=status.HTTP_200_OK)
        response = {
            "message": "Post updated failed",
            "data": serializer.errors
        }
        return Response(data=response, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        post.delete()
        response = {
            "message": "Post deleted"
        }
        return Response(data={"message": "Post deleted", }, status=status.HTTP_204_NO_CONTENT)


    serializer = PostSerializer(instance=post)
    response = {
        "message": "Get detail successful",
        "data": serializer.data
    }
    return Response(data=response, status=status.HTTP_200_OK)


# @api_view(["GET", "POST"])
# def home(request:Request):
#     if request.method == "POST":
#         data = request.data
#         return Response({"message":"Hello World", "data": data}, status=status.HTTP_201_CREATED)
#     response = {
#         "message":"Hello World"
#     }
#     return Response(response, status=status.HTTP_200_OK)


# @api_view(["GET", "POST"])
# def index(request:Request):
#     if request.method == "POST":
#         data = request.data
#         serializer = PostSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             response = {
#                 "message": "Post created",
#                 "data": serializer.data
#             }
#             return Response({"data": response, "status":status.HTTP_201_CREATED})
#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     posts = Post.objects.all()
#     serializer = PostSerializer(instance=posts, many=True)
#     return Response({"data": serializer.data, "status":status.HTTP_200_OK})


# @api_view(["GET", "PUT", "DELETE"])
# def detail(request:Request, id:int):
#     # post = Post.objects.get(id=id)
#     post = get_object_or_404(Post, id=id)
#     serializer = PostSerializer(instance=post)
#     return Response({"data": serializer.data, "status": status.HTTP_200_OK})


# @api_view(["PUT"])
# def update(request:Request, id:int):
#     # post = Post.objects.get(id=id)
#     post = get_object_or_404(Post, id=id)
#     data = request.data
#     serializer = PostSerializer(instance=post, data=data)
#     if serializer.is_valid():
#         serializer.save()
#         response = {
#             "message": "Post updated",
#             "data": serializer.data
#         }
#         return Response(data=data, status=status.HTTP_200_OK)
#     return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(["DELETE"])
# def delete(request:Request, id:int):
#     # post = Post.objects.get(id=id)
#     post = get_object_or_404(Post, id=id)
#     serializer = PostSerializer(instance=post, many=False)
#     return Response({"data": serializer.data, "status": status.HTTP_200_OK})



# class PostListCreateView(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# class PostRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer