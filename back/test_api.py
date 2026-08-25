"""
Backend integration tests for the devops-demo FastAPI application.

conftest.py stubs config.database with an in-memory SQLite engine so no
real Postgres connection is required.
"""

# conftest.py runs first and patches config.database — safe to import app now
from fastapi.testclient import TestClient

from conftest import override_get_db, test_engine
from config.database import get_db, ORMBase
from start import app

# Ensure all ORM tables exist in the in-memory DB
import models  # noqa: F401 — registers all models against ORMBase

ORMBase.metadata.create_all(bind=test_engine)

# Override the DB dependency
app.dependency_overrides[get_db] = override_get_db

client = TestClient(app, raise_server_exceptions=False)


# ── Health check ─────────────────────────────────────────────────────────────

def test_health_check_returns_200():
    """GET /api/health should return 200 when the DB is reachable."""
    response = client.get('/api/health')
    assert response.status_code == 200


# ── Auth: signup ─────────────────────────────────────────────────────────────

def test_signup_creates_user_and_returns_tokens():
    """POST /api/v0/auth/signup with valid data returns 200 with tokens."""
    response = client.post(
        '/api/v0/auth/signup',
        json={
            'username': 'testuser',
            'password': 'StrongPassword1!',
            'readableName': 'Test User',
            'areas': [],
        },
    )
    assert response.status_code == 200
    body = response.json()
    assert 'accessToken' in body
    assert 'refreshToken' in body


def test_signup_duplicate_username_returns_400():
    """Signing up twice with the same username returns 400."""
    payload = {
        'username': 'duplicateuser',
        'password': 'StrongPassword1!',
        'areas': [],
    }
    client.post('/api/v0/auth/signup', json=payload)
    response = client.post('/api/v0/auth/signup', json=payload)
    assert response.status_code == 400


# ── Auth: login ──────────────────────────────────────────────────────────────

def test_login_valid_credentials_returns_tokens():
    """POST /api/v0/auth/login with correct credentials returns tokens."""
    client.post(
        '/api/v0/auth/signup',
        json={'username': 'loginuser', 'password': 'ValidPass1!', 'areas': []},
    )
    response = client.post(
        '/api/v0/auth/login',
        json={'username': 'loginuser', 'password': 'ValidPass1!'},
    )
    assert response.status_code == 200
    body = response.json()
    assert 'accessToken' in body
    assert 'refreshToken' in body


def test_login_wrong_password_returns_401():
    """POST /api/v0/auth/login with wrong password returns 401."""
    client.post(
        '/api/v0/auth/signup',
        json={'username': 'wrongpwduser', 'password': 'CorrectPass1!', 'areas': []},
    )
    response = client.post(
        '/api/v0/auth/login',
        json={'username': 'wrongpwduser', 'password': 'WrongPass!'},
    )
    assert response.status_code == 401


def test_login_unknown_user_returns_400():
    """POST /api/v0/auth/login for a non-existent user returns 400."""
    response = client.post(
        '/api/v0/auth/login',
        json={'username': 'nobody_here', 'password': 'anything'},
    )
    assert response.status_code == 400
