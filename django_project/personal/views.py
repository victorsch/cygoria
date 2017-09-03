from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'personal/home.html')

def contact(request):
	return render(request, 'personal/basic.html', {'content':['Contact: victor.schiavo52@yahoo.com']})

def news(request):
	return render(request, 'personal/news.html')

def analysis(request):
	return render(request, 'personal/analysis.html')
