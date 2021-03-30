from django.test import TestCase

# Create your tests here.
def test_register():
    try:
        (1 == 1)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    test_register()
    print("All tests passed")