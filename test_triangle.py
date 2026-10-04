from app import app


def test_triangle_area_route():
    client = app.test_client()
    response = client.post('/works/area/triangle', data={'base': '10', 'height': '5'})

    assert response.status_code == 200
    assert b'Area of the triangle' in response.data
    assert b'25.0' in response.data


def test_linked_list_route_computes_sum_and_displays_nodes():
    client = app.test_client()
    response = client.post('/works/linked-list', data={'values': '4, 8, 15'})

    assert response.status_code == 200
    assert b'4.0' in response.data
    assert b'8.0' in response.data
    assert b'15.0' in response.data
    assert b'27.0' in response.data


def test_linked_list_route_rejects_invalid_values():
    client = app.test_client()
    response = client.post('/works/linked-list', data={'values': '4, nope'})

    assert response.status_code == 200
    assert b'Enter one or more numbers separated by commas.' in response.data
