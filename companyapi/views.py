from django.http import HttpResponse,JsonResponse

def home_page(request):
    print("Home page requested")
    list=[
        'Bhvaesh',
        'Ayush',
        'Vivek'
    ]
    return JsonResponse(list,safe=False)
    pass