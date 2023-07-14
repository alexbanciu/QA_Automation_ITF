import time

from requests_folder.delete_order import delete_order
from requests_folder.submit_order import submit_order


class TestDeleteOrder:
    def test_delete_order(self):
        s = submit_order(6, "Victor Popescu")
        assert s.status_code == 201
        print(s.json())
        order_id = s.json()['orderId']
        print(order_id)
        time.sleep(5)
        r = delete_order(order_id)
        assert r.status_code == 204
        assert r.json() == ""

    def test_delete_invalid_order(self):
        r = delete_order("123abc")
        assert r.status_code == 404
        assert r.json()['error'] == 'No order with id 123abc.', 'error no ok'

