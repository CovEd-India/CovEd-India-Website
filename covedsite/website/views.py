from django.shortcuts import render
from .models import CoreMember

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
