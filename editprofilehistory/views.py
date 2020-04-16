from django.shortcuts import render

# Create your views here.
def editprofile(request):
    context = {}
    return render(request, 'editprofilehistory/editprofile.html', context)