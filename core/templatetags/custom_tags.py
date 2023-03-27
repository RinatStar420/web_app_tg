from django import template

from core.models import Channel

register = template.Library()


@register.simple_tag()
def filter_channels(value, *args, **kwargs):
    channels = Channel.objects.filter(category_id=value)
    return channels
