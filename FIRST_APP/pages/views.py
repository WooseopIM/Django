from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request,'index.html')

def home(request):
    # return HttpResponse('<!DOCTYPE><html>....홈페이지')
    name = 'Kahn'
    data = ['강동주', '김지수', '정의진']
    empty_data = ['엄복동', '클레멘타인', '성냥팔이소녀의 재림']
    matrix = [[1,2,3],[4,5,6]]
    context = {
        'name': name,
        'data': data,
        'empty_data': empty_data,
        'matrix': matrix,
        'number': 10,
    }
    return render(request, 'home.html', context)

def lotto(request):
    import random
    mylotto = sorted(random.sample(range(1,46),6))
    context = {
        'lotto':mylotto,
        'number': 10,
    }
    return render(request, 'lotto.html', context)

def cube(request, num):
    result = num ** 3
    context = {
        'result': result,
    }
    return render(request, 'cube.html', context)

def match(request):
    import random
    goonghap = random.randint(50,100)
    me = request.POST.get('me')
    you = request.POST.get('you')
    test = request.path_info
    context = {
        'goonghap': goonghap,
        'me': me,
        'you': you,
        'test': test,
    }
    return render(request, 'match.html', context)