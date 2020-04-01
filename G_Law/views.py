from django.http import HttpResponse, HttpResponseNotFound, Http404,  HttpResponseRedirect
 
def test_redirect1(request):
    return HttpResponseRedirect("client/")

def test_redirect2(request):
    return HttpResponseRedirect("client/")