import json
import pytest

from csv_parser import parse_parts
from csv_parser import parse_inventory


def test_parse_parts():
    csv_filename = "test_parts_list.csv"
    result = parse_parts(csv_filename)
    expected_result = ["C102S", "C104S", "LC1-INJ1"]
    assert result == expected_result


@pytest.mark.focus
def test_parse_inventory():
    expected_result = [
        {"description": "Inventory", "availability": 0},
        {
            "description": "CAPS/KNOCKOFFS (WHEEL ACCESSORIES:  'Rocket Racing Wheels' Center Caps, Knockoffs...",
            "availability": 0,
        },
        {
            "description": "C102S (Polished 4x4  Push-Thru Closed Center Caps 4.25' diameter)",
            "availability": 84,
        },
        {
            "description": "C104S (Polished 4x4  Push-Thru Open Center Caps 4.25' diameter)",
            "availability": 77,
        },
    ]
    result = parse_inventory("qb_inventory_test_data.csv")
    assert result == expected_result
