from django import template

register = template.Library()


@register.filter
def verbose_name(obj):
    return obj.model._meta.verbose_name


@register.filter
def verbose_name_plural(obj):
    # return obj._meta.verbose_name_plural
    # return obj.__class__.__name__
    return obj.model._meta.verbose_name_plural


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
