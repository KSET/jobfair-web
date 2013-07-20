from django.http import HttpResponse

def index(request):
    return HttpResponse("CV INDEX PAGE")

def new(request):
    return HttpResponse("NEW CV")

def edit_profile(request, access_code="-1"):
    return HttpResponse("Editing CV with access code {}".format(access_code))

def edit_page(request):
    return HttpResponse("Enter your login info for profile editing")

