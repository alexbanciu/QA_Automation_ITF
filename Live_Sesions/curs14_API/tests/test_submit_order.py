from requests_folder.submit_order import submit_order


class TestSubmitOrder:
    def test_submit_order(self):
        r = submit_order(1, "John")
        assert r.status_code == 201, f"Error: Status code is not valid. Expected: 201, actual: {r.status_code}"
        assert r.json()["created"] == True, f"Error: Order creation status is not correct. Expected: True, Actual: {r.json()['created']}"
        assert len(r.json()["orderId"]) > 0, f"Error: Order id is invalid. Expected length must be grater then 0. Actual length: {len(r.json()['orderId'])}"

    def test_submit_order1(self):
            r = submit_order(6, "Ade")
            assert r.status_code == 201, f"Error: Status code is not valid. Expected: 201, actual: {r.status_code}"
            assert r.json()[
                       "created"] == True, f"Error: Order creation status is not correct. Expected: True, Actual: {r.json()['created']}"
            assert len(r.json()[
                           "orderId"]) > 0, f"Error: Order id is invalid. Expected length must be grater then 0. Actual length: {len(r.json()['orderId'])}"

    def test_submit_order_invalid(self):
        r = submit_order(10003, "Maricica")
        assert r.status_code == 400
        assert r.json()["error"] == "Invalid or missing bookId."