import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_create_dataset(client):
    response = client.post('/datasets', json={
        "name": "Test Dataset",
        "owner": "test_owner",
        "description": "This is a test dataset.",
        "tags": ["test", "pytest"]
    })
    assert response.status_code == 201
    json_data = response.get_json()
    assert json_data["name"] == "Test Dataset"
    assert "created_at" in json_data

def test_get_datasets_by_owner(client):
    # First, create a dataset
    client.post('/datasets', json={
        "name": "Owner Filter Test",
        "owner": "filter_owner",
        "description": "Filter test",
        "tags": ["filter"]
    })

    # Now, test GET with filter
    response = client.get('/datasets?owner=filter_owner')
    assert response.status_code == 200
    datasets = response.get_json()
    assert isinstance(datasets, list)
    assert any(ds["owner"] == "filter_owner" for ds in datasets)
