from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import News
from django.views.generic import View

class GetList(View):
    template_name = 'main.html'
    data = [
        {'name': 'fox', 'title': 'test1', 'is_published': True },
        {'name': 'wolf', 'title': 'test 2', 'is_published': False},
        {'name': 'cat', 'title': 'life of cat', 'is_published': True},
    ]
    def get(self, request, *argc, **kwargs):
        context = {
            'data': self.data,
        }
        return render(request, self.template_name, context)

    def post(self, request, *argc, **kwargs):
        result = request.POST
        context = {
            'data' : self.data,
            'result' : result,
        }
        return render(request, self.template_name, context)

"""
def lastlist(request):
    lastlist = News.objects.last()
    lastperiod = lastlist.period
    recentlist = News.objects.filter(period=lastperiod)
    print(searchperiod(request))
    return render(request, 'siteapp/index.html', {"recentlist":recentlist, "lastperiod": lastperiod})

def recentlist(request):
    lastlist = News.objects.last()
    lastperiod = lastlist.period
    recentlist = News.objects.filter(period=lastperiod)
    return render(request, 'siteapp/index.html', {"list":recentlist})

def alllist(request):
    alllist = News.objects.all()
    return render(request, 'siteapp/index.html', {"list": alllist})

def searchperiod(request):
    if request.method == "POST":
        s_period = request.GET['weeklyDatePicker']
        if s_period is not None:
            print("선택한 기간", s_period)
    #       alllist = News.objects.all()
    #       searchlist = alllist.filter(title__icontains=keyword)
    #     return render(request, 'siteapp/search.html', {'searchlist' : searchlist,})
    # else:
    #     pass
    #
    # start = period[:9]
    # start = start.replace("-", "")
    # end = period[13:]
    # end = end.replace("-", "")
    # periodlist = News.objects.filter(period>=start, period<=end)

    return None

def search(request):
    if request.method == "GET":
        keyword = request.GET['keyword']

        if keyword is not None:
            alllist = News.objects.all()
            searchlist = alllist.filter(title__icontains=keyword)
        return render(request, 'siteapp/search.html', {'searchlist' : searchlist,})
    else:
        pass


"""