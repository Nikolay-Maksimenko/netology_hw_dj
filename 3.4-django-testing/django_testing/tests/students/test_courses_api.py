import pytest
from django.urls import reverse
import random
from students.models import Course
from tests.conftest import course_factory, student_factory

@pytest.mark.django_db
def test_course_retrieve(client, course_factory):
    courses = course_factory(_quantity=10)
    course_id = random.randint(0, len(courses)-1)
    url = reverse('courses-detail', args=(courses[course_id].id,))
    response = client.get(url)
    response_json = response.json()
    print(response_json)
    assert response.status_code == 200
    assert response_json['id'] == courses[course_id].id
    assert response_json['name'] == courses[course_id].name

@pytest.mark.django_db
def test_course_list(client, course_factory):
    course_factory(_quantity=20)
    url = reverse('courses-list')
    response = client.get(url)
    response_json = response.json()
    assert response.status_code == 200
    assert len(response_json) == 20

@pytest.mark.django_db
def test_course_filter_id(client, course_factory):
    courses = course_factory(_quantity=10)
    course_id = random.randint(0, len(courses) - 1)
    url = reverse("courses-list") + f'?id={courses[course_id].id}'
    response = client.get(url)
    response_json = response.json()
    assert response.status_code == 200
    assert response_json[0].get('id') == courses[course_id].id

@pytest.mark.django_db
def test_course_filter_name(client, course_factory):
    courses = course_factory(_quantity=10)
    course_id = random.randint(0, len(courses) - 1)
    url = reverse("courses-list") + f'?name={courses[course_id].name}'
    response = client.get(url)
    assert response.status_code == 200
    assert response.data[0].get('name') == courses[course_id].name

@pytest.mark.django_db
def test_course_create(client, student_factory):
    url = reverse("courses-list")
    students = student_factory(_quantity=5)
    data = {'name': 'python',
            'stundents': students}
    response = client.post(url, data)
    assert response.status_code == 201

@pytest.mark.django_db
def test_course_update(client, course_factory):
    courses = course_factory(_quantity=5)
    course_id = random.randint(0, len(courses) - 1)
    url = reverse("courses-detail", args=(courses[course_id].id,))
    update_data = {'name': 'ruby'}
    response = client.patch(url, update_data)
    assert response.status_code == 200

@pytest.mark.django_db
def test_course_delete(client, course_factory):
    courses = course_factory(_quantity=5)
    course_id = random.randint(0, len(courses) - 1)
    url = reverse("courses-detail", args=(courses[course_id].id,))
    data_del = {'name': 'ruby'}
    response = client.delete(url, data_del)
    assert response.status_code == 204