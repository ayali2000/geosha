from django.shortcuts import render,redirect
from django.db.models import Q, query
from geomatics.models import Quest,Ans
from geomatics.forms import AnsForm, QuesForm
from django.contrib import messages


# Create your views here.
def geohome(request):
    ques = Quest.objects.all()
    query = request.GET.get('q','')
    if query:
        queryset=(Q(question__icontains=query))
        results=Quest.objects.filter(queryset).distinct()
    else:
        results=[]
    frm = QuesForm()
    if request.method == "POST":
        frm = QuesForm(request.POST)
        if frm.is_valid():
            instance = frm.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(request,("Posted"))
            return redirect("geohome")
        else:
            frm = QuesForm()
    context = {
        "query":query,
        "results":results,
        'ques':ques,
        "frm":frm
    }
    return render(request,'geo/geopage.html',context)

def detail_quest(request,pk):
    d_quest = Quest.objects.get(pk=pk)
    ans = Ans.objects.filter(quest=d_quest)
    ansform = AnsForm()
    if request.method == "POST":
        ansform = AnsForm(request.POST)
        if ansform.is_valid():
            instance = ansform.save(commit=False)
            instance.user = request.user
            instance.quest = d_quest
            instance.save()
            return redirect("detail_quest", pk=d_quest.id)
        else:
            ansform = AnsForm()   
    context={
        "d_quest":d_quest,
        "ans":ans,
        "ansform":ansform
    }
    return render(request,"geo/detail_quest.html",context)
