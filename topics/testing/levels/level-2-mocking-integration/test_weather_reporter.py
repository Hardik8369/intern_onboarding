"""
Test suite for weather_reporter.py using unittest.mock.
"""
import pytest
from unittest.mock import patch, MagicMock
import requests
from weather_reporter import get_current_weather, get_weather_summary, format_weather_report


# ============================================
# FAKE DATA
# ============================================

FAKE_WEATHER_RESPONSE = {
    "name": "London",
    "main": {"temp": 15.5, "humidity": 72},
    "weather": [{"description": "clear sky"}],
    "wind": {"speed": 3.2}
}

FAKE_WEATHER_DICT = {
    "city": "London",
    "temp_c": 15.5,
    "description": "clear sky",
    "humidity": 72,
    "wind_speed": 3.2
}


# ============================================
# get_current_weather() tests
# ============================================

@patch("weather_reporter.requests.get")
def test_get_current_weather_success(mock_get):
    """Test successful weather fetch returns correct dict."""
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = FAKE_WEATHER_RESPONSE
    mock_get.return_value = mock_response

    result = get_current_weather("London")

    assert result["city"] == "London"
    assert result["temp_c"] == 15.5
    assert result["description"] == "clear sky"
    assert result["humidity"] == 72
    assert result["wind_speed"] == 3.2


@patch("weather_reporter.requests.get")
def test_get_current_weather_api_error(mock_get):
    """Test that API error (non-200 status) returns None."""
    mock_response = MagicMock()
    mock_response.status_code = 404
    mock_get.return_value = mock_response

    result = get_current_weather("UnknownCity")
    assert result is None


@patch("weather_reporter.requests.get")
def test_get_current_weather_api_called_once(mock_get):
    """Test that requests.get is called exactly once per city."""
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = FAKE_WEATHER_RESPONSE
    mock_get.return_value = mock_response

    get_current_weather("London")
    mock_get.assert_called_once()


def test_get_current_weather_empty_city():
    """Test that empty city raises ValueError."""
    with pytest.raises(ValueError):
        get_current_weather("")


def test_get_current_weather_whitespace_city():
    """Test that whitespace city raises ValueError."""
    with pytest.raises(ValueError):
        get_current_weather("   ")


# ============================================
# get_weather_summary() tests
# ============================================

@patch("weather_reporter.requests.get")
def test_get_weather_summary_multiple_cities(mock_get):
    """Test that get_weather_summary calls API once per city."""
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = FAKE_WEATHER_RESPONSE
    mock_get.return_value = mock_response

    cities = ["London", "Paris", "Berlin"]
    result = get_weather_summary(cities)

    assert mock_get.call_count == 3
    assert "London" in result
    assert "Paris" in result
    assert "Berlin" in result


@patch("weather_reporter.requests.get")
def test_get_weather_summary_mixed_success_failure(mock_get):
    """Test side_effect: mix of successful and failed city lookups."""
    success_response = MagicMock()
    success_response.status_code = 200
    success_response.json.return_value = FAKE_WEATHER_RESPONSE

    failure_response = MagicMock()
    failure_response.status_code = 404

    mock_get.side_effect = [success_response, failure_response]

    result = get_weather_summary(["London", "UnknownCity"])

    assert result["London"] is not None
    assert result["UnknownCity"] is None


@patch("weather_reporter.requests.get")
def test_get_weather_summary_network_timeout(mock_get):
    """Test side_effect: network timeout is handled gracefully."""
    mock_get.side_effect = requests.exceptions.Timeout

    result = get_weather_summary(["London"])
    assert result["London"] is None


# ============================================
# format_weather_report() tests
# ============================================

def test_format_weather_report_success():
    """Test that format_weather_report produces correct string."""
    result = format_weather_report("London", FAKE_WEATHER_DICT)
    assert "London" in result
    assert "15.5" in result
    assert "clear sky" in result
    assert "72" in result
    assert "3.2" in result


def test_format_weather_report_none_weather():
    """Test that None weather returns unavailable message."""
    result = format_weather_report("London", None)
    assert "unavailable" in result
    assert "London" in result


def test_format_weather_report_missing_key():
    """Test that missing key raises ValueError."""
    bad_weather = {"temp_c": 15.5}
    with pytest.raises(ValueError):
        format_weather_report("London", bad_weather)


# ============================================
# INTEGRATION TEST
# ============================================

@patch("weather_reporter.requests.get")
def test_integration_get_and_format(mock_get):
    """Integration test: get_current_weather + format_weather_report pipeline."""
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = FAKE_WEATHER_RESPONSE
    mock_get.return_value = mock_response

    weather = get_current_weather("London")
    report = format_weather_report("London", weather)

    assert "London" in report
    assert "15.5" in report
    assert "clear sky" in report
    assert "72" in report
    assert "3.2" in report
