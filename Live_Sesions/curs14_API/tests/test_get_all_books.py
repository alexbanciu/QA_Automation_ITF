from requests_folder.get_all_books import *


class TestBooks:
    def test_get_all_books_no_filter_no_type_check_status_code(self):
        r = get_all_books("","")
        assert r.status_code == 200, f"Error: status code is not correct. Expected: 200, Actual: {r.status_code}"

    def test_get_all_books_no_filter_no_type_check_nr_rez(self):
        r = get_all_books("", "")
        assert len(r.json()) == 6, f"Expected: 6, actual: {len(r.json())}"

    def test_get_all_books_type_fiction(self):
        r = get_all_books("fiction", "").json()
        assert len(r) == 4, f"Expected: 4, actual: {len(r)}"
        for i in range(len(r)):
            assert r[i]["type"] == "fiction", f"Error: Book {r[i]['name']} has an invalid type."

    def test_get_all_books_type_non_fiction(self):
        r = get_all_books("non-fiction", "").json()
        assert len(r) == 2, f"Expected: 2, actual: {len(r)}"
        for i in range(len(r)):
            assert r[i]["type"] == "non-fiction", f"Error: Book {r[i]['name']} has an invalid type."

    def test_get_all_books_type_invalid(self):
        r = get_all_books("pepelepe", "")
        assert r.status_code == 400
        assert r.json()["error"] == "Invalid value for query parameter 'type'. Must be one of: fiction, non-fiction.", "Error is not correct!"

    def test_get_all_books_limit_invalid(self):
        r = get_all_books("", "21")
        assert r.status_code == 400
        assert r.json()["error"] == "Invalid value for query parameter 'limit'. Cannot be greater than 20.", "Error is not correct!"

    def test_get_all_books_type_fiction_limi_2(self):
        r = get_all_books("fiction", 2)
        assert r.status_code == 200