from django import template
from django.core.urlresolvers import NoReverseMatch, reverse
from django.utils.html import escape, format_html
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def df_login(request):
    """
    Include a login snippet if REST framework's login view is in the URLconf.
    """
    try:
        login_url = reverse('admin:login')
    except NoReverseMatch:
        return ''

    snippet = """
              {href}?next={next}
              """
    snippet = format_html(snippet, href=login_url, next=escape(request.path))

    return mark_safe(snippet)


@register.simple_tag
def df_logout(request, user):
    try:
        logout_url = reverse('admin:logout')
    except NoReverseMatch:
        return None
    snippet = """
                {href}?next={next}
              """
    snippet = format_html(snippet, user=escape(user), href=logout_url, next=escape(request.path))

    return mark_safe(snippet)


