from django.shortcuts import render, redirect
from django.urls import reverse
from django import forms
import markdown
from . import util
import random as rd


class CreateForm(forms.Form):
    title = forms.CharField(widget = forms.TextInput(attrs={"name": "title", "placeholder": "Title"}))
    body = forms.CharField(widget = forms.Textarea(attrs={"name":"body"}))
    edit = forms.CharField(widget = forms.HiddenInput(attrs={"name":"edit"}))
    
    def __init__(self, *args, **kwargs):
        edit = kwargs.pop("edit",None)
        title = kwargs.pop("title",None)
        body = kwargs.pop("body",None)
        super().__init__(*args,**kwargs)
        
        if edit:
            self.fields["edit"].widget.attrs["value"] = edit
            # self.fields["title"].widget.attrs["value"] = title
            # self.fields["body"].widget.attrs["value"] = body
            

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request, title):
    content = util.get_entry(title.capitalize())
    if content is None:
        content = f"The page {title} was not found"
    content = markdown.markdown(content)
    return render(request, "encyclopedia/content.html", {
            "title": title.upper(),
            "content": content
        })

def search(request):
    q = request.GET.get("q")
    if q.capitalize() in util.list_entries():
        return redirect(f"/wiki/{q}")
        
    entries = []
    for x in util.list_entries():
        if q.lower() in x.lower():
            entries.append(x)
        else:
            continue
            
    if entries:
        return render(request, "encyclopedia/search.html", {
            "title": "Search",
            "entries": entries 
        })
    else:
        return render(request, "encyclopedia/error.html", {"message":
            "No Results Found"})
    
def create(request):
    return render(request, "encyclopedia/create.html", {
        "form": CreateForm(edit="False"),
        "title": "Create New Wiki"
    })
    
def add(request):
    if request.method == "POST":
        form = CreateForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            body = form.cleaned_data["body"]
            
            if form.cleaned_data["edit"] == "False":
                if title.lower() in util.list_entries():
                    return render(request, "encyclopedia/error.html", {
                        "message": "wiki title already exists"
                    })  
                
            with open(f"entries/{title}.md","w") as f:
                f.write(body)
            
            return redirect("index")
        else:
            return render(request, "encyclopedia/create.html", {
                "form": form,
                "title": "Create New Wiki"
            })
    else:
        return redirect("index")
    
    
def edit(request, title):
    title = title.capitalize()
    with open(f"entries/{title}.md", "r") as f:
        body = f.read()
    print(body)
    
    return render(request, "encyclopedia/create.html", {
        "form": CreateForm(edit="True", initial={"title" : title, "body":body} ),
        "title": "Edit Wiki"
    })
    
def random(request):
    lucky_page = rd.choice(util.list_entries())
    return redirect(reverse("title", kwargs = {"title":lucky_page}))