from django.contrib import admin
from django import forms
from nexteria.nextis.models import Level

from .models import *
# Register your models here.
admin.site.register(Skolne)


class PlatbaAdmin(admin.ModelAdmin):
    list_display = ['get_meno','suma','cas','vlastnik']
    list_filter = ['cas']

admin.site.register(Platba,PlatbaAdmin)

class VydavokAdmin(admin.ModelAdmin):
    list_display = ['get_meno','suma','ucel','splatnost','uhradene','vlastnik']
    list_filter = ['splatnost']
admin.site.register(Vydavok, VydavokAdmin)



class ParsedEmailAdmin(admin.ModelAdmin):
    list_display = ['nazov','datum', 'priradene']
    list_filter = ['datum']

admin.site.register(ParsedEmail, ParsedEmailAdmin)


class SkolneForm(forms.Form):
    ucel = forms.CharField()
    level = forms.ModelChoiceField(queryset=Level.objects.all(), empty_label=None)
    suma = forms.FloatField()
    splatnost = forms.DateField()

from django.shortcuts import render, HttpResponseRedirect
from django.core.urlresolvers import reverse
def level_skolne_view(req, *args, **kwargs):
    if req.method == "POST":
        form = SkolneForm(req.POST)
        if form.is_valid():
            level = form.cleaned_data['level']

            stud = Student.objects.filter(level=level)
            for s in stud:

                skolne = s.skolne
                vydavok = Vydavok.objects.create(ucel = form.cleaned_data['ucel'], suma= form.cleaned_data['suma'], splatnost = form.cleaned_data['splatnost'], uhradene = 0, vlastnik=skolne)
                vydavok.save()

            return HttpResponseRedirect(reverse('admin:index'))


    form = SkolneForm()
    return render(req, 'admin_skolne.html', context={'form':form})

admin.site.register_view('level_skolne', 'Pridat levelu skolne', view=level_skolne_view)