from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from django import forms
from .models import Event, Exponents


class SignUpForm(UserCreationForm):
    username = forms.CharField(label="", max_length=25, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}))
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))



    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'




class AddRecordForm(forms.ModelForm):
    name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class":"form-control"}), label="")
    data_begin = forms.DateField(required=True, widget=forms.widgets.DateInput)
    data_end = forms.DateField(required=True, widget=forms.widgets.DateInput)
    image_of_event = forms.ImageField()
    description = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class":"form-control"}), label="")
    exp = forms.ModelMultipleChoiceField(queryset=Exponents.objects.all(),widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Event
        exclude = ("user",)
        fields = ('image_of_event',)

class AddExpForm(forms.ModelForm):
    name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class":"form-control"}), label="")
    name_of_company = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class":"form-control"}), label="")
    price = forms.IntegerField(required=True, widget=forms.widgets.NumberInput)
    desription = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class":"form-control"}), label="")
    image_of_exp1 = forms.ImageField(required=None)
    class Meta:
        model = Exponents
        exclude = ("user",)
        fields = ('image_of_exp1',)
