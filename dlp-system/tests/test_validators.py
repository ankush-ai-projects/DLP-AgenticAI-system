from app.detection.validators import aadhaar_shape_valid, luhn_valid, pan_valid


def test_luhn_accepts_known_test_number():
    assert luhn_valid("4111111111111111")


def test_luhn_rejects_invalid_number():
    assert not luhn_valid("4111111111111112")


def test_indian_identifier_shapes():
    assert pan_valid("ABCDE1234F")
    assert aadhaar_shape_valid("2345 6789 0123")
