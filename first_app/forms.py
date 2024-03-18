from django import forms
from django.core import validators


class contactForm(forms.Form):
    name = forms.CharField(label="Full Name: ", initial="Rahim",
                           help_text="total length must be within 70 characters", disabled=True)
    # file = forms.FileField()
    # email = forms.EmailField()
    # age = forms.IntegerField()
    # weight = forms.FloatField()
    # balance = forms.FloatField()
    # check = forms.BooleanField()
    # Birthdate = forms.DateField()
    # appoinment = forms.DateTimeField()
    # Choices = [('S', 'Small'), ('M', 'Medium'), ('L', 'Large')]
    # size = forms.ChoiceField(choices=Choices)


# class StudentData(forms.Form):
#     name = forms.CharField()
#     email = forms.EmailField()

    # def clean_name(self):
    #     valname = self.cleaned_data['name']
    #     if len(valname) < 10:
    #         raise forms.ValidationError(
    #             "Enter a name with at least 10 characters")
    #     return valname

    # def clean_email(self):
    #     valemail = self.cleaned_data['email']
    #     if '.com' not in valemail:
    #         raise forms.ValidationError("Your email must contain .com")
    #     return valemail

    # def clean(self):
    #     cleaned_data = super().clean()
    #     valname = self.cleaned_data['name']
    #     valemail = self.cleaned_data['email']
    #     if len(valname) < 10:
    #         raise forms.ValidationError("Enter a name with at least 10 characters")
    #     if '.com' not in valemail:
    #         raise forms.ValidationError("Your email must contain .com")

class StudentData(forms.Form):
    name = forms.CharField(validators=[validators.MinLengthValidator(
        10, message='Enter a name with at least 10 characters')])
    email = forms.EmailField(validators=[validators.EmailValidator()])
    age = forms.IntegerField(validators=[validators.MaxValueValidator(
        34, message="age must be maximum 34"), validators.MinValueValidator(20, message="age at least 20")])

    file = forms.FileField(validators=[validators.FileExtensionValidator(
        allowed_extensions=['pdf'], message="file extention must be ended with .pdf")])


class PasswordValidationProject(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        val_pass = self.cleaned_data['password']
        val_conpass = self.cleaned_data['confirm_password']
        val_name = self.cleaned_data['name']
        if val_conpass != val_pass:
            raise forms.ValidationError("passsword doesn't match")
        if len(val_name) < 15:
            raise forms.ValidationError("Name must be at least 15 characters")
