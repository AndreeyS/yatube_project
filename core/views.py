from django.shortcuts import render


def page_not_found(request, exception):
    context = {
        'path': request.path
    }
    return render(request, 'core/404.html', context, status=404)


def crsf_failure(request, reason=''):
    return render(request, 'core/403crsf.html')


def server_error(request):
    return render(request, 'core/500.html')


def permission_denied(request, exception):
    return render(request, 'core/403.html')
