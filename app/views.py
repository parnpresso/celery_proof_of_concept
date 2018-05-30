from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.shortcuts import redirect, render

from .forms import GenerateTypedWord
from .tasks import create_typed_word, random_string
from .models import TypedWord


class testTemplate(TemplateView):
    template_name = 'base.html'

    def submit(self):
        print('hello world')
        random_string.delay()

# class GenerateTypedWordView(FormView):
#     template_name = 'base.html'
#     form_class = GenerateTypedWord
#     model = TypedWord

#     def form_valid(self, form):
#         typed_word = form.cleaned_data.get('typed_word')
#         create_typed_word.delay(typed_word)
#         return redirect('proof')
