from django.forms import forms


class ProfileForm(forms.ModelForm):
       the_choices = forms.ModelMultipleChoiceField(queryset=Choices.objects.all(), required=False, widget=forms.CheckboxSelectMultiple)

       class Meta:
           model = Profile
           exclude = ['user']