from tablegpt_kernel.__about__ import __version__


def test_version_is_not_none():
    assert __version__ is not None
