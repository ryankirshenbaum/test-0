from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import MemberForm as member_form
from .models import Member
from django.views import generic
from rest_framework import viewsets
from .serializers import MemberSerializer
from rest_framework.decorators import action
from .models import Member


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


def TestView(request):
    set = Member.objects.all()
    return render(request, 'test_app/test.html', {"member_list" : set})


