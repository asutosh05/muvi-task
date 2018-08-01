from django.urls import reverse
from django.contrib.auth.models import User
from content.views import ContentListView
from mixer.backend.django import mixer
import pytest
from django.test import RequestFactory
from accounts.models import Profile

@pytest.mark.django_db
class TestViews:

    def test_content_list_authenticated(self):
        mixer.blend('content.Content')
        path=reverse('all-muvi')
        request=RequestFactory().get(path)
        request.user=mixer.blend(User)


        responce=ContentListView(request)
        assert responce.status_code==200