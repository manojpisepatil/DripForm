from django import forms

# class ContactForm(forms.Form):
#     name = forms.CharField(max_length=100, required=True)
#     email = forms.EmailField(required=True)
#     message = forms.CharField(widget=forms.Textarea, required=True)


# class ContactForm(forms.Form):
#     name = forms.CharField(label='Full Name', max_length=100)
#     email = forms.EmailField(label='Email')
#     domain = forms.ChoiceField(
#         label='Domain',
#         choices=[
#             ('digital_marketing', 'Digital Marketing'),
#             ('web_development', 'Web Development'),
#             ('data_analysis', 'Data Analysis'),
#         ],
#     )


from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    domain = forms.ChoiceField(choices=[
        ('digital_marketing', 'Digital Marketing'),
        ('web_development', 'Web Development'),
        ('data_analysis', 'Data Analysis'),
    ])
    duration = forms.ChoiceField(choices=[
        ('1', '1 month'),
        ('2', '2 months'),
        ('3', '3 months'),
        ('4', '4 months'),
        ('5', '5 months'),
        ('6', '6 months'),
    ])
