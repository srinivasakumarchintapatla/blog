from django.http import HttpResponse
from django.shortcuts import render
from datetime import date

all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Maximilian",
        "date": date(2021, 7, 21),
        "title": "Mountain Hiking",
        "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for the waht happened whilst I was enjoying the view!",
        "content": """ 
           Lorem, ipsum dolor sit amet consectetur adipisicing elit. Deleniti dolorem dignissimos, 
           ad quidem labore molestiae nihil esse excepturi error hic ipsum repellat cupiditate! Deserunt
           suscipit ab perferendis nihil officia culpa.

           Lorem, ipsum dolor sit amet consectetur adipisicing elit. Deleniti dolorem dignissimos, 
           ad quidem labore molestiae nihil esse excepturi error hic ipsum repellat cupiditate! Deserunt
           suscipit ab perferendis nihil officia culpa.

           Lorem, ipsum dolor sit amet consectetur adipisicing elit. Deleniti dolorem dignissimos, 
           ad quidem labore molestiae nihil esse excepturi error hic ipsum repellat cupiditate! Deserunt
           suscipit ab perferendis nihil officia culpa.

        """             
                         

    },
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Maximilian",
        "date": date(2022, 3, 10),
        "title": "Programming is fun!",
        "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for the waht happened whilst I was enjoying the view!",
        "content": """ 
           Lorem, ipsum dolor sit amet consectetur adipisicing elit. Deleniti dolorem dignissimos, 
           ad quidem labore molestiae nihil esse excepturi error hic ipsum repellat cupiditate! Deserunt
           suscipit ab perferendis nihil officia culpa.

           Lorem, ipsum dolor sit amet consectetur adipisicing elit. Deleniti dolorem dignissimos, 
           ad quidem labore molestiae nihil esse excepturi error hic ipsum repellat cupiditate! Deserunt
           suscipit ab perferendis nihil officia culpa.

           Lorem, ipsum dolor sit amet consectetur adipisicing elit. Deleniti dolorem dignissimos, 
           ad quidem labore molestiae nihil esse excepturi error hic ipsum repellat cupiditate! Deserunt
           suscipit ab perferendis nihil officia culpa.

        """             
                         

    },
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Maximilian",
        "date": date(2020, 8, 5),
        "title": "nature at its best",
        "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for the waht happened whilst I was enjoying the view!",
        "content": """ 
           Lorem, ipsum dolor sit amet consectetur adipisicing elit. Deleniti dolorem dignissimos, 
           ad quidem labore molestiae nihil esse excepturi error hic ipsum repellat cupiditate! Deserunt
           suscipit ab perferendis nihil officia culpa.

           Lorem, ipsum dolor sit amet consectetur adipisicing elit. Deleniti dolorem dignissimos, 
           ad quidem labore molestiae nihil esse excepturi error hic ipsum repellat cupiditate! Deserunt
           suscipit ab perferendis nihil officia culpa.

           Lorem, ipsum dolor sit amet consectetur adipisicing elit. Deleniti dolorem dignissimos, 
           ad quidem labore molestiae nihil esse excepturi error hic ipsum repellat cupiditate! Deserunt
           suscipit ab perferendis nihil officia culpa.

        """             
                         

    }
]

def get_date(post):
    return post['date']

# Create your views here.


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render( request,"blog/index.html", {
     "posts": latest_posts
    })

def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts      
    })

def post_detail(request, slug):
    identified_post = next(posts for posts in all_posts if posts["slug"] == slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post 
    })


