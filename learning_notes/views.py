from django.shortcuts import render,redirect
from .models import Topic,Entry
from .forms import TopicForm,EntryForm
from django.contrib.auth.decorators import login_required
from django.http import Http404
def check_topic_owner(request,topic):
    if topic.owner != request.user:
        raise Http404
def index(request):
    return render(request,'learning_notes/index.html')

@login_required
def topics(request):
    """显示所有主题"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics':topics}
    return render(request,'learning_notes/topics.html',context)

@login_required
def topic(request,topic_id):
    """显示单个主题以及所有条目"""
    topic = Topic.objects.get(id=topic_id)
    check_topic_owner(request,topic)
    entries=topic.entry_set.order_by('-date_added')
    context = {'topic':topic,'entries':entries}
    return render(request,'learning_notes/topic.html',context)

@login_required
def new_topic(request):
    """增加新主题"""
    if request.method != 'POST':
        #未提交则创建一个新表单
        form = TopicForm()
    else:
        #POST提交的数据，并对数据进行处理
        form=TopicForm(request.POST)
        if form.is_valid():
            new_topic=form.save(commit=False)
            new_topic.owner=request.user
            new_topic.save()
            #form.save()
            return redirect('learning_notes:topics')
    context = {'form':form}
    return render(request,'learning_notes/new_topic.html',context)

@login_required
def new_entry(request,topic_id):
    """特定主题中增加新条目"""
    topic=Topic.objects.get(id=topic_id)
    check_topic_owner(request,topic)
    if request.method != 'POST':
        form = EntryForm()
    else:
        #POST提交的数据，处理数据
        form=EntryForm(data= request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_notes:topic',topic_id=topic_id)
    context = {'form':form,'topic':topic}
    return render(request,'learning_notes/new_entry.html',context)

@login_required
def edit_entry(request,entry_id):
    """编辑已有条目"""
    entry = Entry.objects.get(id=entry_id)
    topic=entry.topic
    check_topic_owner(request,topic)
    if request.method != 'POST':
        #初次请求,:使用当前条目填充表单
        form = EntryForm(instance=entry)
    else:
        #POST提交数据，对数据进行处理
        form=EntryForm(instance=entry,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_notes:topic',topic_id=topic.id)
    context = {'form':form,'topic':topic,'entry':entry}
    return render(request,'learning_notes/edit_entry.html',context)
