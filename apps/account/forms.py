# -*- coding: utf-8 -*-
"""
    account.forms

    :copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Limited
    :license: see LICENSE for more details.
"""
from django import forms
from account.models import UserProfile, TrainingProfile, StudentProfile, \
    GovernmentProfile, IndustryProfile

__all__ = [
    'SignupForm', 'TrainingProfileForm', 'TrainingProfileForm',
    'StudentProfileForm', 'IndustryProfileForm', 'GovernmentProfileForm'
]


class SignupForm(forms.Form):
    """
    Signup Form
    """
    role = forms.CharField(
        max_length=5, label='Role',
        widget=forms.Select(choices=UserProfile.ROLE_CHOICES)
    )

    def save(self, user):
        user_profile = UserProfile(role=self.cleaned_data['role'], user=user)
        user_profile.save()


class TrainingProfileForm(forms.ModelForm):
    '''
    Training Profile Form
    '''
    class Meta:
        model = TrainingProfile
        exclude = ('user_profile', 'is_approved')


class StudentProfileForm(forms.ModelForm):
    '''
    Student Profile Form
    '''
    class Meta:
        model = StudentProfile
        exclude = ('user_profile', )


class IndustryProfileForm(forms.ModelForm):
    '''
    Industry Profile Form
    '''
    class Meta:
        model = IndustryProfile
        exclude = ('user_profile', 'is_approved')


class GovernmentProfileForm(forms.ModelForm):
    '''
    Government Profile Form
    '''
    class Meta:
        model = GovernmentProfile
        exclude = ('user_profile', 'is_approved')
