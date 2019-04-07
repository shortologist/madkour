from django.http import JsonResponse


def names(request):
    return JsonResponse({'names': ['Islam', 'Atef', 'Salem', 'Ahmed']})
