from ..models import Grade
from django import template

register= template.Library()

@register.simple_tag
def get_recent_posts(num=50):
    return Grade.objects.all().order_by('-grade_id')[:num]
