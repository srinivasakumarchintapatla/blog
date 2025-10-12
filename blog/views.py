# # from nt import lstat
# # from django.db.models import QuerySet
# # from django.http import HttpResponse
# # from django.shortcuts import render, get_object_or_404
# # from .models import Post
# # from .forms import CommentForm
# from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponseRedirect
# from django.urls import reverse
# from django.views.generic import ListView
# from django.views import View
# from django.views.generic import DetailView, ListView , DateDetailView
# from .models import Post
# from .forms import CommentForm


# # Create your views here.

# class StartingPageView(ListView):
#     template_name = "blog/index.html"
#     model = Post
#     ordering = ["-date"]
#     context_object_name = "posts"
    
#     def get_queryset(self):
#         querySet = super().get_queryset()
#         data = querySet[:3]
#         return data


# class AllPostsView(ListView):
#     template_name = "blog/all-posts.html" 
#     model = Post
#     ordering = ["-date"]
#     context_object_name = "all_posts"
    
# class SinglePostView(DetailView):
#     template_name = "blog/post-detail.html"
#     model = Post
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["post_tags"] = self.object.tags.all()
#         context["Comment_form"] = CommentForm()
#         return context
            























from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.template import context
from django.views.generic import ListView, detail
from django.views import View

from .models import Comment, Post
from .forms import CommentForm

# Create your views here.

class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data


class AllPostsView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "all_posts"


class SinglePostView(View):
    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm()
        }
        return render(request, "blog/post-detail.html", context)

    def post(self, request, slug):  
        comment_form = CommentForm(request.POST)
        # post = get_object_or_404(Post, slug=slug)
        post = Post.objects.get(slug=slug)
         
        if comment_form.is_valid(): 
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            
            return HttpResponseRedirect(reverse("post-detail-page", args=[slug])) 
       
        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": comment_form
        }
        return render(request, "blog/post-detail.html", context)
# pyright: ignore[reportUndefinedVariable]


    # def get_context_data(self, **kwargs):
    #     context =  super().get_context_data(**kwargs)
    #     context["post_tags"] = self.object.tags.all()
    #     context["comment_form"] = CommentForm()
    #     return context
