# loja/context_processors.py
from django.conf import settings

def site_info(request):
    return {
        'site_name': getattr(settings, 'SITE_NAME', 'Mayconcell'),
        'site_description': getattr(settings, 'SITE_DESCRIPTION', ''),
    }

def colors(request):
    return {
        'primary_color': getattr(settings, 'PRIMARY_COLOR', '#000000'),
        'secondary_color': getattr(settings, 'SECONDARY_COLOR', '#00AA13'),
    }