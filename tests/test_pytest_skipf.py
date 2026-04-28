import pytest

system_version = "v1.2.0"

@pytest.mark.skipif("system_version == v1.3.0", reason="skip test")
def test_system_valid():

    ...

@pytest.mark.skipif("system_version == v1.3.0", reason="skip test")
def test_system_invalid():
    ...

@pytest.mark.xfail
def test_with_bug():
    assert 1 == 2

@pytest.mark.xfail
def test_without_bug():
    ...