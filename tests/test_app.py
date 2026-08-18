from app import search_students

def test_search_student_found():
    result = search_students("Nguyen")
    assert len(result) == 1
    assert result[0]["name"] == "Nguyen Van A"

def test_search_student_not_found():
    result = search_students("Unknown")
    assert len(result) == 0

def test_search_student_case_insensitive():
    result = search_students("nguyen")
    assert len(result) == 1
