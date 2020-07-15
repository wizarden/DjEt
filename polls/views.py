from django.shortcuts import  render


from .models import Question


def index1(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def index(request):
    question = Question.objects.all()

    return render(request, 'polls/index.html', {'question': question} )