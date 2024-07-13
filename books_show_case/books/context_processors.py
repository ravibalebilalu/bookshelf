# books/context_processors.py
from django.conf import settings

def custom_processor(request):
    # Example context processor
    return {
        'DEBUG': settings.DEBUG,
        'INTERNAL_IPS': settings.INTERNAL_IPS,
        'request_path': request.path,  # Example of accessing request attributes
        # Add more context variables as needed
    }