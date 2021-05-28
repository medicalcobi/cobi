
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.

class PostList(ListView):
    model = Post
    ordering = '-pk'

class PostDetail(DetailView):
    model = Post


# def index(request):
#     return render(
#         request,
#         'qna/post_list.html',
#     )
#
# def single_post_page(request, pk):
#     return render(
#         request,
#         'qna/post_detail.html',
#     )


