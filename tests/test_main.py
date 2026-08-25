from app.main import get_app_info


def test_get_app_info():
    info = get_app_info()

    assert info["name"] == "DevSecOps Lab"
    assert info["version"] == "0.1.0"
    assert info["status"] == "running"
