from django.shortcuts import render, redirect
from .models import Topic, Entry
from .forms import TopicForm, EntryForm


# Create your views here.

def index(request):
    """学习笔记的主页。"""
    return render(request, 'learning_logs/index.html')


def topics(request):
    """显示所有的主题"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}

    return render(request, 'learning_logs/topics.html', context)


def topic(request, topic_id):
    """显示单个主题及所有的条目"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {
        'topic': topic,
        'entries': entries
    }
    return render(request, 'learning_logs/topic.html', context)


def new_topic(request):
    """添加新主题"""
    if request.method != 'POST':
        # 未提交数据：创建一个新表单
        form = TopicForm()
    else:
        # post 提交的数据：对数据进行处理
        print(request.POST)
        # <QueryDict: {'csrfmiddlewaretoken': ['b3IdOQATx4YpqyXrpvmsB3NbUXrLBr0SH4B5qoZ2eZEquck0OKl9yf19Fp5YXa9s'],
        # 'text': ['dsfdsf'], 'submit': ['']}>

        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')
    # 显示空表单或指出表单数据无效
    context = {
        'form': form
    }
    return render(request, 'learning_logs/new_topic.html', context)


def new_entry(request, topic_id):
    """在特定主题中添加新条目"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != "POST":
        # 未提交数据：创建一个空表单
        form = EntryForm()
    else:
        # post 提交的数据：对数据进行处理
        form = EntryForm(data=request.POST)
        if form.is_valid():
            # 让Django创建一个新的条目对象，并将其赋值给new_entry,但不保存到数据库中。
            new_entry = form.save(commit=False)
            # 将其与正确的主题相关联
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)
    # 显示空表单或指出表单数据无效。
    context = {'topic': topic,
               'form': form}

    return render(request, 'learning_logs/new_entry.html', context)


def edit_entry(request, entry_id):
    """编辑既有条目。"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        # 初次请求：使用当前条目填充表单
        form = EntryForm(instance=entry)
    else:
        # POST 提交的数据：对数据进行处理
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)

    context = {
        'entry': entry,
        'topic': topic,
        'form': form
    }

    return render(request, 'learning_logs/edit_entry.html', context)
