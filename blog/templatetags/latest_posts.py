# blog/templatetags/latest_posts.py
from django import template
from blog.models import Post

register = template.Library()

@register.inclusion_tag('blog/latest_posts.html')
def get_latest_posts():
    posts = Post.objects.order_by('-created_at')[:5]
    return {'latest_posts': posts}
