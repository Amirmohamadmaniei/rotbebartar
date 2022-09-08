from django.db.models import Count
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic

from blog import models
from blog.models import Like, Blog


class BlogListView(generic.View):
    def get(self, request):
        last_blogs = models.Blog.objects.filter(status=True).order_by('-created')[:2]
        popular_blogs = models.Blog.objects.filter(status=True).annotate(
            count=Count('likes')).order_by('-count', '-created')[:2]
        views_blogs = models.Blog.objects.filter(status=True).annotate(count=Count('ipaddress')).order_by('-count',
                                                                                                          '-created')[
                      :2]
        print(popular_blogs)

        return render(request, 'blog/Blog_list.html',
                      {'last_blogs': last_blogs, 'popular_blogs': popular_blogs, 'views_blogs': views_blogs})


class BlogDetail(generic.View):
    def get(self, request, slug):
        blog = models.Blog.objects.get(slug=slug)
        related_blogs = models.Blog.objects.filter(status=True, author_id=blog.author_id).order_by('?')[:3]

        if request.user.is_authenticated:
            liked = Like.objects.filter(blog=blog, user=request.user).exists()
        else:
            liked = ''

        if request.user.ip_address not in blog.ipaddress.all():
            blog.ipaddress.add(request.user.ip_address)

        return render(request, 'blog/Blog_detail.html',
                      {'object': blog, 'related_blogs': related_blogs, 'liked': liked})


class LikeView(generic.View):
    def get(self, request, slug):
        blog = Blog.objects.get(slug=slug)
        Like.objects.create(blog=blog, user=self.request.user)

        return redirect(reverse('blog:blog_detail', kwargs={'slug': slug}))


def unlike(request, slug):
    blog = Blog.objects.get(slug=slug)
    Like.objects.filter(blog=blog, user=request.user).delete()
    return redirect(reverse('blog:blog_detail', kwargs={'slug': slug}))
