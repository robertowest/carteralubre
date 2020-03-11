from django import template
from django.db.models.query import QuerySet

register = template.Library()


@register.filter
def verbose_name(obj):
    if isinstance(obj, QuerySet):
        return obj.model._meta.verbose_name
    else:
        return obj._meta.verbose_name


@register.filter
def verbose_name_plural(obj):
    # return obj._meta.verbose_name_plural
    # return obj.__class__.__name__
    if isinstance(obj, QuerySet):
        return obj.model._meta.verbose_name_plural
    else:
        return obj._meta.verbose_name_plural


@register.filter
def filtro_active(modelo, valor):
    return modelo.filter(active=valor)


@register.filter
def query(qs, **kwargs):
    """ template tag which allows queryset filtering. Usage:
          {% query books author=author as mybooks %}
          {% for book in mybooks %}
            ...
          {% endfor %}
    """
    return qs.filter(**kwargs)


@register.filter
def url_action(obj, action):
    if isinstance(obj, QuerySet):
        model_name = obj.model._meta.verbose_name
    else:
        model_name = obj._meta.verbose_name
    return '{obj}:{act}'.format(obj=model_name.lower(), act=action.lower())


@register.filter
def url_action_pk(url, pk):
    return '{url} {id}'.format(url=url, id=pk)
