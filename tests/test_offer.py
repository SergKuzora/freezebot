from fastapi.testclient import TestClient

from evrone_freezebot.main import app
from evrone_freezebot.settings import settings


def test_offer():
    client = TestClient(app)
    result = client.get(settings.main_url)
    assert result.status_code == 200
    assert result.json() == {'status': 'ok'}
