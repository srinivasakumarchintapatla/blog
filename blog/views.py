
# from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponseRedirect, request
# from django.template import context
# from django.urls import reverse
# from django.views.generic import ListView
# from django.views import View

# from .models import Post
# from .forms import CommentForm
# # Create your views here.
# class StartingPageView(ListView):
#     template_name = "blog/index.html"
#     model = Post
#     ordering = ["-date"]
#     context_object_name = "posts"

#     def get_queryset(self):
#         queryset = super().get_queryset()
#         data = queryset[:3]
#         return data


# class AllPostsView(ListView):
#     template_name = "blog/all-posts.html"
#     model = Post
#     ordering = ["-date"]
#     context_object_name = "all_posts"


# class SinglePostView(View):
#     def get(self, request, slug):
#         post = Post.objects.get(slug=slug)
#         context = {
#             "post": post,
#             "post_tags": post.tags.all(),
#             "comment_form": CommentForm(),
#             "comments": post.comments.all().order_by("-id")
#         }
        
        
#         return render(request, "blog/post-detail.html", context)

#     def post(self, request, slug):  
#         comment_form = CommentForm(request.POST)
#         # post = get_object_or_404(Post, slug=slug)
#         post = Post.objects.get(slug=slug)
         
#         if comment_form.is_valid(): 
#             comment = comment_form.save(commit=False)
#             comment.post = post
#             comment.save()
            
#             return HttpResponseRedirect(reverse("post-detail-page", args=[slug])) 
       
#         context = {
#             "post": post,
#             "post_tags": post.tags.all(),
#             "comment_form": comment_form,
#             "comments": post.comments.all().order_by("-id")
#         }
#         return render(request, "blog/post-detail.html", context)
    
# class ReadLaterView(View):
#     def get(self, request):
#         stored_posts = request.session.get("stored_posts")
#         context = {}
        
#         if stored_posts is None or len(stored_posts) == 0:
#             context["posts"] = []
#             context["has_posts"] = False
#         else:
#             posts = Post.objects.filter(id__in=stored_posts)
#             context["posts"] = posts
#             context["has_posts"] = True
            
#         return render(request, "blog/stored-posts.html", context)
    
#     def post(self, request):    
#         stored_posts = request.session.get("stored_posts")
        
#         if stored_posts is None:
#             stored_posts = []
            
#         post_id = int(request.POST["post_id"])
        
#         if post_id not in stored_posts: 
#             stored_posts.append(post_id)
#             request.session["stored_posts"] = stored_posts
            
#         return HttpResponseRedirect("/")








# from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponseRedirect
# from django.urls import reverse
# from django.views.generic import ListView
# from django.views import View

# from .models import Post
# from .forms import CommentForm

# # Create your views here.


# class StartingPageView(ListView):
#     template_name = "blog/index.html"
#     model = Post
#     ordering = ["-date"]
#     context_object_name = "posts"

#     def get_queryset(self):
#         queryset = super().get_queryset()
#         data = queryset[:3]
#         return data


# class AllPostsView(ListView):
#     template_name = "blog/all-posts.html"
#     model = Post
#     ordering = ["-date"]
#     context_object_name = "all_posts"

# class SinglePostView(View):
#     def is_stored_post(self, request, post_id):
#         stored_posts = request.session.get("stored_posts")
#         if stored_posts is not None:
#             is_saved_for_later = post_id in stored_posts
#         else:
#             is_saved_for_later = False
            
            
#             return is_saved_for_later
        
#     def get(self, request, slug):
#         post = Post.objects.get(slug=slug)
        
#         context = {
#             "post": post,
#             "post_tags": post.tags.all(),
#             "comment_form": CommentForm(),
#             "comments": post.comments.all().order_by("-id"),
#             "saved_for_later": self.is_stored_post(request,post.id)
#         }
#         return render(request, "blog/post-detail.html", context)

#     def post(self, request, slug):
#         comment_form = CommentForm(request.POST)
#         post = Post.objects.get(slug=slug)

#         if comment_form.is_valid():
#             comment = comment_form.save(commit=False)
#             comment.post = post
#             comment.save()

#             return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))

#         context = {
#             "post": post,
#             "post_tags": post.tags.all(),
#             "comment_form": comment_form,
#             "comments": post.comments.all().order_by("-id"),
#             "saved_for_later": self.is_stored_post(request,post.id)
#         }
#         return render(request, "blog/post-detail.html", context)


# class ReadLaterView(View):
#     def get(self, request):
#         stored_posts = request.session.get("stored_posts")

#         context = {}

#         if stored_posts is None or len(stored_posts) == 0:
#             context["posts"] = []
#             context["has_posts"] = False
#         else:
#           posts = Post.objects.filter(id__in=stored_posts)
#           context["posts"] = posts
#           context["has_posts"] = True

#         return render(request, "blog/stored-posts.html", context)


#     def post(self, request):
#         stored_posts = request.session.get("stored_posts")

#         if stored_posts is None:
#           stored_posts = []

#         post_id = int(request.POST["post_id"])

#         if post_id not in stored_posts:
#           stored_posts.append(post_id) 
#         else:
#             stored_posts.remove(post_id)
            
#             request.session["stored_posts"] = stored_posts
        
#         return HttpResponseRedirect("/")









# from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponseRedirect
# from django.urls import reverse
# from django.views.generic import ListView
# from django.views import View

# from .models import Post
# from .forms import CommentForm
# from .forms import ContactForm # ContactForm is imported here!

# # Create your views here.


# class StartingPageView(ListView):
#     template_name = "blog/index.html"
#     model = Post
#     ordering = ["-date"]
#     context_object_name = "posts"

#     def get_queryset(self):
#         queryset = super().get_queryset()
#         data = queryset[:3]
#         return data


# class AllPostsView(ListView):
#     template_name = "blog/all-posts.html"
#     model = Post
#     ordering = ["-date"]
#     context_object_name = "all_posts"


# class SinglePostView(View):
#     def is_stored_post(self, request, post_id):
#         stored_posts = request.session.get("stored_posts")
#         if stored_posts is not None:
#             is_saved_for_later = post_id in stored_posts
#         else:
#             is_saved_for_later = False

#         return is_saved_for_later

#     def get(self, request, slug):
#         # Using get_object_or_404 for robustness is better practice
#         post = get_object_or_404(Post, slug=slug) 
        
#         context = {
#             "post": post,
#             "post_tags": post.tags.all(),
#             "comment_form": CommentForm(),
#             "comments": post.comments.all().order_by("-id"),
#             "saved_for_later": self.is_stored_post(request, post.id)
#         }
#         return render(request, "blog/post-detail.html", context)

#     def post(self, request, slug):
#         comment_form = CommentForm(request.POST)
#         # Using get_object_or_404 for robustness is better practice
#         post = get_object_or_404(Post, slug=slug) 

#         if comment_form.is_valid():
#             comment = comment_form.save(commit=False)
#             comment.post = post
#             comment.save()

#             # Post-Redirect-Get Pattern: redirect to prevent resubmission
#             return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))

#         # Re-render with form errors if invalid
#         context = {
#             "post": post,
#             "post_tags": post.tags.all(),
#             "comment_form": comment_form,
#             "comments": post.comments.all().order_by("-id"),
#             "saved_for_later": self.is_stored_post(request, post.id)
#         }
#         return render(request, "blog/post-detail.html", context)


# class ReadLaterView(View):
#     def get(self, request):
#         stored_posts = request.session.get("stored_posts")

#         context = {}

#         if stored_posts is None or len(stored_posts) == 0:
#             context["posts"] = []
#             context["has_posts"] = False
#         else:
#           posts = Post.objects.filter(id__in=stored_posts)
#           context["posts"] = posts
#           context["has_posts"] = True

#         return render(request, "blog/stored-posts.html", context)


#     def post(self, request):
#         stored_posts = request.session.get("stored_posts")

#         if stored_posts is None:
#           stored_posts = []

#         post_id = int(request.POST["post_id"])

#         if post_id not in stored_posts:
#           stored_posts.append(post_id)
#         else:
#           stored_posts.remove(post_id)

#         # Ensure session is saved after modification
#         request.session["stored_posts"] = stored_posts
        
#         # Check for 'next' URL to redirect back to the post detail page (UX improvement)
#         next_url = request.POST.get("next", "/")
#         return HttpResponseRedirect(next_url)


# ## 🚀 NEW CONTACT VIEW ##

# class ContactSuccessView(View):
#     """Renders a page confirming the contact message was successfully sent."""
    
#     def get(self, request):
#         return render(request, "blog/contact-success.html")

# class ContactView(View):
#     """Handles displaying and processing the contact form."""
#     template_name = "blog/contact.html"  # Assuming you have this template

#     def get(self, request):
#         """Displays the empty contact form."""
#         form = ContactForm()
#         return render(request, self.template_name, {
#             "contact_form": form
#         })

#     def post(self, request):
#         """Processes the submitted contact form."""
#         form = ContactForm(request.POST)

#         if form.is_valid():
#             # **TO-DO: Implement actual contact logic here, such as:**
#             # 1. Sending an email using Django's send_mail function.
#             # 2. Saving the contact message to a database model.
            
#             # Placeholder for successful submission:
#             # The user is usually redirected to a 'success' page or the homepage.
#             return HttpResponseRedirect(reverse("contact-success")) 

#         # If the form is invalid, re-render the template with the populated form and errors
#         return render(request, self.template_name, {
#             "contact_form": form
#         })




from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView
from django.views import View

from .models import Post
from .forms import CommentForm
from .forms import ContactForm 

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
    def is_stored_post(self, request, post_id):
        stored_posts = request.session.get("stored_posts")
        if stored_posts is not None:
            is_saved_for_later = post_id in stored_posts
        else:
            is_saved_for_later = False

        return is_saved_for_later

    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug) 
        
        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm(),
            "comments": post.comments.all().order_by("-id"),
            "saved_for_later": self.is_stored_post(request, post.id)
        }
        return render(request, "blog/post-detail.html", context)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = get_object_or_404(Post, slug=slug) 

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()

            return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))

        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": comment_form,
            "comments": post.comments.all().order_by("-id"),
            "saved_for_later": self.is_stored_post(request, post.id)
        }
        return render(request, "blog/post-detail.html", context)


class ReadLaterView(View):
    def get(self, request):
        stored_posts = request.session.get("stored_posts")

        context = {}

        if stored_posts is None or len(stored_posts) == 0:
            context["posts"] = []
            context["has_posts"] = False
        else:
          posts = Post.objects.filter(id__in=stored_posts)
          context["posts"] = posts
          context["has_posts"] = True

        return render(request, "blog/stored-posts.html", context)


    def post(self, request):
        stored_posts = request.session.get("stored_posts")

        if stored_posts is None:
          stored_posts = []

        post_id = int(request.POST["post_id"])

        if post_id not in stored_posts:
          stored_posts.append(post_id)
        else:
          stored_posts.remove(post_id)

        request.session["stored_posts"] = stored_posts
        
        next_url = request.POST.get("next", "/")
        return HttpResponseRedirect(next_url)


## 🚀 CONTACT VIEWS ##

class ContactSuccessView(View):
    """Renders a page confirming the contact message was successfully sent."""
    
    def get(self, request):
        return render(request, "blog/contact-success.html")

class ContactView(View):
    """Handles displaying and processing the contact form."""
    template_name = "blog/contact.html" 

    def get(self, request):
        """Displays the empty contact form."""
        form = ContactForm()
        return render(request, self.template_name, {
            "contact_form": form
        })

    def post(self, request):
        """Processes the submitted contact form."""
        form = ContactForm(request.POST)

        if form.is_valid():
            # **ENHANCED: Saving the data to the Contact model**
            form.save() 
            
            # Redirect to the success page
            return HttpResponseRedirect(reverse("contact-success")) 

        # If the form is invalid, re-render the template with the populated form and errors
        return render(request, self.template_name, {
            "contact_form": form
        })