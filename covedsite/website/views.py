from django.shortcuts import render
from .models import CoreMember

def home(request) :
	return render(request, 'index.html')

def aboutUs(request) :
	m = CoreMember.objects.all()
	members1 = []
	members2 = []
	members3 = []
	for mem in m :
		c = mem.categories.split(',')
		if '1' in c :
			members1.append(mem)
		if '2' in c :
			members2.append(mem)
		if '3' in c :
			members3.append(mem)
	return render(request, 'aboutUs.html', {'members1' : members1, 'members2' : members2, 'members3' : members3})

def mentor(request) :
	return render(request, 'mentorSignUp.html')

def student(request) :
	return render(request, 'studentSignUp.html')

def resources(request) :
	return render(request, 'resources.html')

