from django import forms
from .models import Answer

class QuizForm(forms.Form):
    def __init__(self, *args, **kwargs):
        questions = kwargs.pop('questions')
        super(QuizForm, self).__init__(*args, **kwargs)
        
        for question in questions:
            self.fields[f'question_{question.id}'] = forms.ChoiceField(
                choices=[(answer.id, answer.text) for answer in question.answer_set.all()],
                widget=forms.RadioSelect,
                label=question.text
            )
