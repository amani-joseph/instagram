from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    posts = [{
        "image": "https://images.pexels.com/photos/11369622/pexels-photo-11369622.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260",
        "likes": "600",
        "comments": ["Dope","Capping","Big up my dawg!!"],
        "pub_date": "Mar 2",
        "caption": "Life on the fast lane",
        "user": "John Doe"
        # comment: ""
    },
        {
            "image": "https://images.pexels.com/photos/9125253/pexels-photo-9125253.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260",
            "likes": "600",
            "comments": ["Dope", "Capping", "Big up my dawg!!"],
            "pub_date": "Mar 2",
            "caption": "Life on the fast lane",
            "user": "John Doe"
            # comment: ""
        },
        {
            "image": "https://images.pexels.com/photos/7614448/pexels-photo-7614448.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260",
            "likes": "600",
            "comments": ["Dope", "Capping", "Big up my dawg!!"],
            "pub_date": "Mar 2",
            "caption": "Life on the fast lane",
            "user": "John Doe"
            # comment: ""
        },
        {
            "image": "https://images.pexels.com/photos/7478690/pexels-photo-7478690.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260",
            "likes": "600",
            "comments": ["Dope", "Capping", "Big up my dawg!!"],
            "pub_date": "Mar 2",
            "caption": "Life on the fast lane",
            "user": "John Doe"
            # comment: ""
        },
    ]
    context = {
        'posts': posts
    }
    return render(request, 'insta/index.html', context)

