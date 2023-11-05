import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert 'LYRIC FINDR' in response.data.decode('utf-8')

def test_search_by_artist(client):
    response = client.post('/', data={'search_artist': 'The Beatles'})
    assert response.status_code == 200
    assert response.data
    assert 'songs' in response.data

def test_search_by_song_title(client):
    response = client.post('/', data={'search_lyrics': 'Yesterday'})
    assert response.status_code == 200
    assert 'song' in response.data
    assert 'lyrics' in response.data

def test_error_message_for_empty_search(client):
    response = client.post('/', data={'search_artist': '', 'search_lyrics': ''})
    assert response.status_code == 200
    assert 'error_message' in response.data
