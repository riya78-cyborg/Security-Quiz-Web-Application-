from django.shortcuts import render
from .models import Quiz
from .forms import QuizForm

def quiz_view(request, quiz_id):
    quiz = Quiz.objects.get(pk=quiz_id)
    questions = quiz.question_set.all()

    if request.method == 'POST':
        form = QuizForm(request.POST, questions=questions)

        if form.is_valid():
            # Process form submission (calculate score, etc.)
            # This part will depend on your specific requirements
            pass
    else:
        form = QuizForm(questions=questions)

    return render(request, 'quiz/quiz.html', {'quiz': quiz, 'form': form})
