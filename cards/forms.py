from django import forms


class CardCheckForm(forms.Form):
    card_id = forms.IntegerField(required=True)  # Поле для введення ідентифікатора картки
    solved = forms.BooleanField(required=False)  # Прапорець, що вказує на вирішення питання на картці