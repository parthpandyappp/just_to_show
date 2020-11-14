from django.shortcuts import render, redirect
from .models import Profile
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.generic.edit import CreateView

def index(request):
    if request.method == "POST":
        pr = Profile()
        pr.name = request.POST.get('name')
        pr.std = request.POST.get('std')
        pr.save()
        return redirect('st')
    return render(request, "exa/input.html")

class ProfileList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'exa/profile_list.html'

    def get(self, request):
        queryset = Profile.objects.all()
        return Response({'profiles': queryset})