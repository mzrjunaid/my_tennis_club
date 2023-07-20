from django.http import HttpResponse
from django.template import loader
from .models import Member
from django.db.models import Q


def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))


def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))


def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())


def testing(request):
    mydata = Member.objects.filter(
        Q(firstname__contains='bia') | Q(firstname='Emil')
    ).values()
    mymembers = Member.objects.all().order_by('id', 'firstname').values()
    template = loader.get_template('template.html')
    context = {
        'mymembers': mymembers,
        'data': mydata
    }
    return HttpResponse(template.render(context, request))
