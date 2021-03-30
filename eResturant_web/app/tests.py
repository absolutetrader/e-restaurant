from django.test import TestCase

# Create your tests here.
def test_register():
    try:
        assert(1 == 2), "Registration Failed"
    except ValueError as e:
        print(e)

def test_login():
    try:
        assert(1 == 2), "Login failed"
    except ValueError as e:
        print(e)

def test_logout():
    try:
        assert(1 == 2), "Logout faield"
    except ValueError as e:
        print(e)

def test_tableBook():
    try:
        assert(1 == 2), "Table booking failed"
    except ValueError as e:
        print(e)

def test_tableEdit():
    try:
        assert(1 == 2), "Table booking edit failed"
    except ValueError as e:
        print(e)

def test_tableCancel():
    try:
        assert(1 == 2), "Table cancelling failed"
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    test_register()
    print("All tests passed")