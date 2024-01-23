from django import forms
from .models import *

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

class SignUpForm(forms.ModelForm):
	class Meta:
		model=SignUp
		fields='__all__'

	full_name = forms.CharField(
		required=False,
		widget=forms.TextInput(
			attrs={
			'type':'text',
			'class':'rounded border-0 input-login w-100 text-main',
			'placeholder': "Họ và tên"
			}
			)
		)

	email = forms.EmailField(
		required=False,
		widget=forms.TextInput(
			attrs={
			'type':'email',
			'class':'rounded border-0 input-login w-100 text-main',
			'placeholder': "Email",
			'autocomplete': 'off'
			}
			)
		)

	email_login = forms.EmailField(
		required=False,
		widget=forms.TextInput(
			attrs={
			'type':'email',
			'class':'rounded border-0 input-login w-100 text-main',
			'placeholder': "Email",
			'autocomplete': 'off'
			}
			)
		)

	password = forms.CharField(
		required=False,
		widget=forms.PasswordInput(
			attrs={
			'type':'password',
			'class':'rounded border-0 input-login w-100 text-main',
			'placeholder': "Mật khẩu",
			'autocomplete': 'off'
			}
			)
		)

	password_login = forms.CharField(
		required=False,
		widget=forms.PasswordInput(
			attrs={
			'type':'password',
			'class':'rounded border-0 input-login w-100 text-main',
			'placeholder': "Mật khẩu",
			'autocomplete': 'off'
			}
			)
		)

	password_aign = forms.CharField(
		required=False,
		widget=forms.PasswordInput(
			attrs={
			'type':'password',
			'class':'rounded border-0 input-login w-100 text-main',
			'placeholder': "Nhập lại mật khẩu"
			}
			)
		)

	phone = forms.CharField(
		required=False,
		widget=forms.TextInput(
			attrs={
			'type':'phone',
			'class':'rounded border-0 input-login w-100 text-main',
			'placeholder': "Số điện thoại"
			}
			)
		)