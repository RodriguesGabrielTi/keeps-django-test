from uuid import uuid4

from django.test import TestCase
from model_mommy import mommy
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

from course.models import Course


class CourseTestCase(TestCase):
    def setUp(self):
        self.course = mommy.make(Course)
        self.client = APIClient()

        self.headers = {}
        self.url = reverse('courses-list')

    def test_course_list(self):
        response = self.client.get(self.url, format='json').json()
        self.assertEqual(len(response), 1)

    def test_course_detail(self):
        response = self.client.get(
            reverse('courses-detail', args=[str(self.course.id)]),
            format='json'
        )
        self.assertEqual(response.json().get('id'), str(self.course.id))
        self.assertEqual(response.status_code, 200)

    def test_course_detail_not_found(self):
        response = self.client.get(
            reverse('courses-detail', args=[str(uuid4())]),
            format='json'
        )
        self.assertEqual(response.status_code, 404)

    def test_course_post(self):
        course_data = {
            'name': 'New Course',
            'duration': 10
        }
        response = self.client.post(
            self.url,
            data=course_data,
            format='json'
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json().get('name'), course_data.get('name'))

    def test_course_patch(self):
        course_data = {
            'name': 'New Course Updated',
        }
        response = self.client.patch(
            reverse('courses-detail', args=[str(self.course.id)]),
            data=course_data,
            format='json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get('name'), course_data.get('name'))
