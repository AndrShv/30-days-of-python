import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from shared import average, parse_kv_record  # noqa: E402


def test_parse_kv_record_semicolon():
    result = parse_kv_record("  id:temp_01;val:23.5;status:active  ", ";")
    assert result == {"id": "temp_01", "val": "23.5", "status": "active"}


def test_parse_kv_record_underscore():
    result = parse_kv_record("ID:1042_Model:ResNet50_Accuracy:0.9482_Epochs:50", "_")
    assert result["Model"] == "ResNet50"
    assert float(result["Accuracy"]) == 0.9482


def test_parse_kv_record_keeps_extra_separators_in_value():
    assert parse_kv_record("time:12:30:00", ";") == {"time": "12:30:00"}


def test_average_basic():
    assert average([120, 450, 460]) == (120 + 450 + 460) / 3


def test_average_empty_returns_default():
    assert average([]) == 0.0
    assert average([], default=-1) == -1


def test_average_accepts_generator():
    assert average(x for x in [2, 4, 6]) == 4
