from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

from fastapi.testclient import TestClient


API_PATH = Path(__file__).resolve().parents[1] / "app" / "api.py"


def load_api_app():
    spec = spec_from_file_location("segmenai_api", API_PATH)

    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to load app/api.py")

    module = module_from_spec(spec)
    spec.loader.exec_module(module)

    return module.app


def test_health_endpoint():
    app = load_api_app()
    client = TestClient(app)

    response = client.get("/api/v1/health")

    assert response.status_code == 200

    body = response.json()

    assert body["status"] == "ok"
    assert body["service"] == "segmenai-api"