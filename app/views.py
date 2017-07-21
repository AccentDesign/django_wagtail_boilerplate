from django.http import HttpResponse
from django.template import Context, loader


def error404(request, exception):
    template = loader.get_template('404.html')
    context = {'request': request}
    return HttpResponse(content=template.render(context), content_type='text/html; charset=utf-8', status=404)


def error500(request):
    template = loader.get_template('500.html')
    context = {'request': request}
    return HttpResponse(content=template.render(context), content_type='text/html; charset=utf-8', status=500)


def robots(request):
    template = loader.get_template('robots.txt')
    return HttpResponse(content=template.render(), content_type="text/plain")
