from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from webpush import send_user_notification
from webpush.utils import send_to_subscription

from .models import BlogPost


@login_required
def BlogPostList(request):
    all_blogposts = BlogPost.objects.all()

    user = get_user_model()
    all_users = user.objects.all()
    payload = {'head': 'Welcome!', 'body': 'Hello World', 'icon': 'https://i.imgur.com/dRDxiCQ.png', 'url': 'www.example.com'}
    for user in all_users:
        send_user_notification(user=user, payload=payload, ttl=1000)
    #Is Not Working
    # user = request.user
    # payload = {"head": "Welcome!", "body": "Hello World"}
    # push_infos = user.webpush_info.select_related("subscription")
    # for push_info in push_infos :
    #     send_to_subscription(push_info.subscription, payload)
    
    # Working Fine
    # payload = {'head': 'Welcome!', 'body': 'Hello World', 'icon': 'https://i.imgur.com/dRDxiCQ.png', 'url': 'www.example.com'}
    # send_user_notification(user=user, payload=payload, ttl=1000)
    # Here in the user parameter, a user object should be passed
    # The user will get notification to all of his subscribed browser. A user can subscribe many browsers.
    context = {
        'all_blogposts': all_blogposts
    }
    return render(request, 'BlogPost/BlogPost.html', context)


@login_required
def BlogPostCreate(request):
    if request.method == 'POST':
        r = request.POST
        code = r.get('code')
        address = r.get('address')
        mobile = r.get('mobile')

        blogpost = BlogPost(code=code, mobile=mobile, address=address)
        blogpost.save()
        return render(request, 'BlogPost/BlogPost.html', context)
    else:
        return render(request, 'BlogPost/BlogPost.html', context)
