from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status


class signuptest(APITestCase):
    def test_ssignup(self):
        url = reverse("user_view")
        user_data ={
            "username":"test",
            "fullname":"테스트",
            "email":"skunn123@naver.com",
            "password":"asd",
        }
        response =self.client.post(url,user_data)
        print(response.data)
        self.assertEqual(response.data,{'message': '가입 완료!!'})