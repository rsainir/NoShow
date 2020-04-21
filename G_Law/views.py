from django.http import HttpResponse, HttpResponseNotFound, Http404,  HttpResponseRedirect

def test_redirect1(request):
    return HttpResponseRedirect("client/signin")

def test_redirect2(request):
    return HttpResponseRedirect("client/signin")

def test_redirect3(request):
    return HttpResponseRedirect("admin/")

def test_redirect4(request):
    return HttpResponseRedirect("client/signin")
