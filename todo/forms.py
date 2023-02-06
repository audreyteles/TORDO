from django import forms


class ToDoForms(forms.Form):
    task = forms.CharField(max_length=40,
                           widget=forms.TextInput(attrs={'class': 'task', 'placeholder': "Enter your task here"}),
                           label="")


class Login(forms.Form):
    email = forms.CharField(max_length=40,
                            widget=forms.EmailInput(attrs={'placeholder': "E-mail"}),
                            label="")
    password = forms.CharField(max_length=40,
                               widget=forms.PasswordInput(attrs={'placeholder': "Password"}),
                               label="")


class Register(forms.Form):
    username = forms.CharField(max_length=20,
                               widget=forms.TextInput(attrs={'placeholder': "Username"}),
                               label="")
    email = forms.CharField(max_length=40,
                            widget=forms.EmailInput(attrs={'placeholder': "E-mail"}),
                            label="")
    password = forms.CharField(max_length=40,
                               widget=forms.PasswordInput(attrs={'placeholder': "Password"}),
                               label="")


"""<div class="textfield">
                <label for="user">E-mail:</label>
                <input type="text" name="user" placeholder="e-mail">
            </div>
            <div class="textfield">
                <label for="password">Password:</label>
                <input type="password" name="user" placeholder="password">
            </div>
            <button class="btn-login">Login</button>"""
