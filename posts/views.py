from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Post
# Create your views here.

# posts = [
#     {
#         "id": 1,
#         "title": "Post 1",
#         "content": "This is the first post",
#         "date": "2021-09-10",
#         "author": "John Doe"
#     },
#     {
#         "id": 2,
#         "title": "Post 2",
#         "content": "This is the second post",
#         "date": "2021-09-10",
#         "author": "John Doe"
#     },
#     {
#         "id": 3,
#         "title": "Post 3",
#         "content": "This is the third post",
#         "date": "2021-09-10",
#         "author": "John Doe"
#     }
#     ]

@api_view(["GET", "POST"])
def home(request:Request):
    if request.method == "POST":
        data = request.data
        return Response({"message":"Hello World", "data": data}, status=status.HTTP_201_CREATED)
    response = {
        "message":"Hello World"
    }
    return Response(response, status=status.HTTP_200_OK)


@api_view(["GET"])
def index(request:Request):
    posts = Post.objects.all()
    return Response({"data": posts, "status":status.HTTP_200_OK})


@api_view(["GET"])
def detail(request:Request, id:int):
    post = Post.objects.get(id=id)
    if post:
        return Response({"data": post, "status": status.HTTP_200_OK})
    return Response({data: "Post not found", "status":status.HTTP_404_NOT_FOUND})