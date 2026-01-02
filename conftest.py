import pytest

def pytest_configure(config):
    config.addinivalue_line("markers", "smoke: smoke test suite")
    config.addinivalue_line("markers", "sanity: sanity test suite")
    config.addinivalue_line("markers", "regression: regression test suite")
