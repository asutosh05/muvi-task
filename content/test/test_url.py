from django.urls import reverse,resolve

class TestUrls:

    def test_list_url(self):
        path=reverse("all-muvi")
        assert resolve(path).view_name=="all-muvi"

    def test_details_url(self):
        path=reverse("muvi-details",kwargs={'slug':'morning-video'})
        assert resolve(path).view_name=="muvi-details"

    def test_create_url(self):
        path=reverse("create-muvi")
        assert resolve(path).view_name=="create-muvi"

    def test_delete_url(self):
        path=reverse("delete",kwargs={'slug':'mar-ing'})
        assert resolve(path).view_name=="delete"