from src.api_service import get_current_time


def test_get_current_time_returns_valid_datetime() -> None:
    current_time = get_current_time()

    assert current_time is not None
    assert isinstance(current_time, str)
    assert 'T' in current_time
