from django.shortcuts import render

# Create your views here.

def artii(request):
    import requests
    font_url = 'http://artii.herokuapp.com/fonts_list'
    response = requests.get(font_url).text
    font_list = response.split()
    context = {
        'font_list': font_list,
    }
    return render(request, 'artii/artii.html', context)

def artii_result(request):
    import requests

    # 1. 단어를 받아온다. request.Get.get('string')
    string = request.GET.get('string')
    font = request.GET.get('font')
    
    # 2. artii api를 통해 ascii art 결과물을 요청하고.
    url = f'http://artii.herokuapp.com/make?text={string}&font={font}'
    result = requests.get(url).text
    
    # 3. 결과를 받아와 보여준다.font_url = f'http://artii.herokuapp.com/make?text={string}'
    context = {
        'string': string,
        'artii_result': result,
    }
    return render(request, 'artii/artii_result.html', context)
