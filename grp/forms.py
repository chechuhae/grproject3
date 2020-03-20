from grp.models import Profile
from django import forms
from .widgets import BootstrapDateTimePickerInput

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    username = forms.CharField(label=u"Имя пользователя")
    email = forms.EmailField(label=u"Email", required=False)
    password = forms.CharField(label=u"Пароль", widget=forms.PasswordInput)
    password_confirm = forms.CharField(label=u"Подтвердите пароль", widget=forms.PasswordInput)

    def is_valid(self):
        valid = super(RegisterForm, self).is_valid()
        if self.cleaned_data['password'] != self.cleaned_data['password_confirm']:
            self.add_error("password_confirm", u"Пароли не совпадают")
            return False
        return valid

# Тут происходит маппинг твоей модели профайла из базы данных с html-формой. Этот класс генерирует нужный html для всей формы
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
    # Эта функция повзволяет сделать специальный маппинг для полей (колонок) из твоей базы к полям html формы
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['birth_date'] = forms.DateTimeField( # Тут ты поле\колонку birth_date приязываешь к твоему кастомному виджету выбора даты
            input_formats=['%d/%m/%Y'],
            widget=BootstrapDateTimePickerInput() # Виджет будет применен конкретно к birth_date
        )