from django import forms


class SubmitUrlForm(forms.Form):
    url = forms.URLField(label='Submit URL', widget=forms.widgets.TextInput)

