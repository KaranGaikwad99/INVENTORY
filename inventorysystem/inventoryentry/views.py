from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Entries
from .forms import EntriesForm
from django.http import JsonResponse
from django.template.loader import render_to_string
from .resources import EntriesResource
from django.http import HttpResponse
from django.db.models import Q
from django.utils import timezone
from .filters import EntriesFilter


def entries_list(request):
	entriess = Entries.objects.all().order_by('-id')
	
	query = request.GET.get("q")
	if query:
		entriess = entriess.filter(
			Q(machine_type__icontains=query) |
			Q(machine_make__icontains=query) 
		).distinct()
	paginator = Paginator(entriess, 10) # Show 5 Entries per page	
	page = request.GET.get('page')
	try:
		entriess = paginator.page(page)
	except PageNotAnInteger:
		entriess = paginator.page(1)
	except EmptyPage:
		entriess = paginator.page(paginator.num_pages)
	
	context = {
	'entriess': entriess
	}
	return render(request, 'inventorysystem/entries_list.html',context)

def save_all(request,form,template_name):
	data = dict()
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			data['form_is_valid'] = True
			entriess = Entries.objects.all()
			data['entries_list'] = render_to_string('inventorysystem/entries_list_2.html',{'entriess':entriess})
		else:
			data['form_is_valid'] = False
	context = {
	'form':form
	}
	data['html_form'] = render_to_string(template_name,context,request=request)
	return JsonResponse(data)

def entries_create(request):
	if request.method == 'POST':
		form = EntriesForm(request.POST)
	else:
		form = EntriesForm()
	return save_all(request,form,'inventorysystem/entries_create.html')

def entries_update(request,id):
	entries = get_object_or_404(Entries,id=id)
	if request.method == 'POST':
		form = EntriesForm(request.POST,instance=entries)
	else:
		form = EntriesForm(instance=entries)
	return save_all(request,form,'inventorysystem/entries_update.html')

def entries_delete(request,id):
	data = dict()
	entries = get_object_or_404(Entries,id=id)
	if request.method == "POST":
		entries.delete()
		data['form_is_valid'] = True
		entriess = Entries.objects.all()
		data['entries_list'] = render_to_string('inventorysystem/entries_list_2.html',{'entriess':entriess})
	else:
		context = {'entries':entries}
		data['html_form'] = render_to_string('inventorysystem/entries_delete.html',context,request=request)

	return JsonResponse(data)

def export_csv(request):
    entries_resource = EntriesResource()
    dataset = entries_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="entries.csv"'
    return response

def export_excel(request):
    entries_resource = EntriesResource()
    dataset = entries_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="entries.xls"'
    return response

