from app import app


def test_triangle_area_route():
    client = app.test_client()
    response = client.post('/works/area/triangle', data={'base': '10', 'height': '5'})

    assert response.status_code == 200
    assert b'Area of the triangle' in response.data
    assert b'25.0' in response.data
