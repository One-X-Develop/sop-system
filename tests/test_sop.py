from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_and_list_sop():
    data = {
        "sop_code": "TEST-001",
        "title": "单元测试",
        "description": "pytest 生成",
        "steps": {"step1": "done"}
    }
    r = client.post("/api/sops", json=data)
    assert r.status_code == 201
    sop_id = r.json()["sop_id"]

    r = client.get("/api/sops")
    assert r.status_code == 200
    ids = [item["sop_id"] for item in r.json()]
    assert sop_id in ids
