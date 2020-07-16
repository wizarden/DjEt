from django.shortcuts import  render


from .models import Question


def index(request):
    question = Question.objects.all()

    return render(request, 'polls/index.html', {'question': question} )