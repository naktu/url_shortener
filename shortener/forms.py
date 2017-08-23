from django import forms


class SubmitUrlForm(forms.Form):
    url = forms.URLField(label='',
                         widget=forms.widgets.TextInput(attrs= {
                             "placeholder": "Long URL",
                             "class": "form-control"
                         }),
                         )

