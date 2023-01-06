from django.shortcuts import render


# Create your views here.

def home(request):
	return render(request, 'expensify/home.html')

def about(request):
	return render(request, 'expensify/about.html')

def aboutContent(request):
	return render(request, 'expensify/aboutContent.html')

def education(request):
	return render(request, 'expensify/education.html')

def workExp(request):
	return render(request, 'expensify/workExp.html')

def skills(request):
	return render(request, 'expensify/skills.html')

def achievements(request):
	return render(request, 'expensify/achievements.html')

