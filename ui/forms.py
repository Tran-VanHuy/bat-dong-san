from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm

class ContactForm(forms.ModelForm):

	class Meta:
		model = Contact
		fields = '__all__'

	full_name = forms.CharField(
		required=True,
		widget=forms.TextInput(
			attrs={
			'type':'text',
			'class':'input-contact rounded px-4 border-0 mb-3',
			'placeholder': 'Họ và tên *' 
			}
			)
		)

	phone = forms.CharField(
		required=True,
		widget=forms.TextInput(
			attrs={
			'type':'text',
			'class':'input-contact rounded px-4 border-0 mb-3',
			'placeholder': 'Số điện thoại *' 
			}
			)
		)

	email = forms.CharField(
		required=False,
		widget=forms.TextInput(
			attrs={
			'type':'text',
			'class':'input-contact rounded px-4 border-0 mb-3',
			'placeholder': 'Email' 
			}
			)
		)

	note = forms.CharField(
		required=True,
		widget=forms.Textarea(
			attrs={
			'type':'text',
			'class':'w-100 h-100 note-contact rounded p-3 border-0',
			'placeholder': 'Ghi chú *' 
			}
			)
		)

class RegisterForm(UserCreationForm):
	class Meta:
		model=User
		fields = ('last_name', 'first_name',  'phone', 'email', 'username')

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field in self.fields.values():
			field.widget.attrs['class'] = 'rounded border-0 input-login w-100 text-main'
			field.widget.attrs['required'] = ""

			if field.label == "Last name":
				field.widget.attrs['autofocus'] = ""
				field.widget.attrs['placeholder'] = "Họ"

			if field.label == "First name":
				field.widget.attrs['autofocus'] = ""
				field.widget.attrs['placeholder'] = "Tên"

			if field.label == "Email address":
				field.widget.attrs['autofocus'] = ""
				field.widget.attrs['placeholder'] = "Email"

			if field.label == "Username":
				field.widget.attrs['autofocus'] = ""
				field.widget.attrs['placeholder'] = "Tài khoản"

			if field.label == "Password":
				field.widget.attrs['autofocus'] = ""
				field.widget.attrs['placeholder'] = "Mật khẩu"

			if field.label == "Password confirmation":
				field.widget.attrs['autofocus'] = ""
				field.widget.attrs['placeholder'] = "Xác nhận mật khẩu"

			if field.label == "Phone":
				field.widget.attrs['autofocus'] = ""
				field.widget.attrs['placeholder'] = "Số điện thoại"

class LoginForm(AuthenticationForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field in self.fields.values():
			field.widget.attrs['class'] = 'rounded border-0 input-login w-100 text-main'
			field.widget.attrs['required'] = ""

			if field.label == "Username":
				field.widget.attrs['placeholder'] = "Tài khoản"

			if field.label == "Password":
				field.widget.attrs['placeholder'] = "Mật khẩu"
	