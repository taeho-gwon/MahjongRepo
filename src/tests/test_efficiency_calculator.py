import pytest

from src.efficiency_calculator import calculate_efficiency
from src.hand_parser import get_hand_from_code, get_tile_from_code
from src.schema.count import HandCount
from src.schema.efficiency_data import EfficiencyData


@pytest.mark.parametrize(
    "test_input, expected",
    [
        (
            "58m23p189s234566z9p",
            [
                ("5m", ["1m", "9m", "1p", "1z", "7z"], 20),
                ("8m", ["1m", "9m", "1p", "1z", "7z"], 20),
                ("2p", ["1m", "9m", "1p", "1z", "7z"], 20),
                ("3p", ["1m", "9m", "1p", "1z", "7z"], 20),
                ("8s", ["1m", "9m", "1p", "1z", "7z"], 20),
            ],
        ),
        (
            "2569m348p3s122774z",
            [
                (
                    "1z",
                    [
                        "1m",
                        "2m",
                        "3m",
                        "4m",
                        "5m",
                        "6m",
                        "7m",
                        "8m",
                        "9m",
                        "2p",
                        "3p",
                        "4p",
                        "5p",
                        "6p",
                        "7p",
                        "8p",
                        "9p",
                        "1s",
                        "2s",
                        "3s",
                        "4s",
                        "5s",
                        "2z",
                        "4z",
                        "7z",
                    ],
                    87,
                ),
                (
                    "4z",
                    [
                        "1m",
                        "2m",
                        "3m",
                        "4m",
                        "5m",
                        "6m",
                        "7m",
                        "8m",
                        "9m",
                        "2p",
                        "3p",
                        "4p",
                        "5p",
                        "6p",
                        "7p",
                        "8p",
                        "9p",
                        "1s",
                        "2s",
                        "3s",
                        "4s",
                        "5s",
                        "1z",
                        "2z",
                        "7z",
                    ],
                    87,
                ),
                (
                    "9m",
                    [
                        "1m",
                        "2m",
                        "3m",
                        "4m",
                        "5m",
                        "6m",
                        "7m",
                        "2p",
                        "3p",
                        "4p",
                        "5p",
                        "6p",
                        "7p",
                        "8p",
                        "9p",
                        "1s",
                        "2s",
                        "3s",
                        "4s",
                        "5s",
                        "1z",
                        "2z",
                        "4z",
                        "7z",
                    ],
                    83,
                ),
                (
                    "2m",
                    [
                        "4m",
                        "5m",
                        "6m",
                        "7m",
                        "8m",
                        "9m",
                        "2p",
                        "3p",
                        "4p",
                        "5p",
                        "6p",
                        "7p",
                        "8p",
                        "9p",
                        "1s",
                        "2s",
                        "3s",
                        "4s",
                        "5s",
                        "1z",
                        "2z",
                        "4z",
                        "7z",
                    ],
                    79,
                ),
                (
                    "8p",
                    [
                        "1m",
                        "2m",
                        "3m",
                        "4m",
                        "5m",
                        "6m",
                        "7m",
                        "8m",
                        "9m",
                        "2p",
                        "3p",
                        "4p",
                        "5p",
                        "1s",
                        "2s",
                        "3s",
                        "4s",
                        "5s",
                        "1z",
                        "2z",
                        "4z",
                        "7z",
                    ],
                    75,
                ),
                (
                    "3s",
                    [
                        "1m",
                        "2m",
                        "3m",
                        "4m",
                        "5m",
                        "6m",
                        "7m",
                        "8m",
                        "9m",
                        "2p",
                        "3p",
                        "4p",
                        "5p",
                        "6p",
                        "7p",
                        "8p",
                        "9p",
                        "1z",
                        "2z",
                        "4z",
                        "7z",
                    ],
                    71,
                ),
                ("5m", ["2m", "6m", "9m", "3p", "4p", "8p", "3s", "1z", "4z"], 27),
                ("6m", ["2m", "5m", "9m", "3p", "4p", "8p", "3s", "1z", "4z"], 27),
                ("3p", ["2m", "5m", "6m", "9m", "4p", "8p", "3s", "1z", "4z"], 27),
                ("4p", ["2m", "5m", "6m", "9m", "3p", "8p", "3s", "1z", "4z"], 27),
            ],
        ),
        (
            "19m19p159s1234567z",
            [
                (
                    "5s",
                    [
                        "1m",
                        "9m",
                        "1p",
                        "9p",
                        "1s",
                        "9s",
                        "1z",
                        "2z",
                        "3z",
                        "4z",
                        "5z",
                        "6z",
                        "7z",
                    ],
                    39,
                ),
            ],
        ),
        (
            "69m5678p2789s344z7p",
            [
                (
                    "9m",
                    [
                        "4m",
                        "5m",
                        "6m",
                        "7m",
                        "8m",
                        "6p",
                        "9p",
                        "1s",
                        "2s",
                        "3s",
                        "4s",
                        "3z",
                        "4z",
                    ],
                    46,
                ),
                (
                    "3z",
                    [
                        "4m",
                        "5m",
                        "6m",
                        "7m",
                        "8m",
                        "9m",
                        "6p",
                        "9p",
                        "1s",
                        "2s",
                        "3s",
                        "4s",
                        "4z",
                    ],
                    46,
                ),
                (
                    "6m",
                    ["7m", "8m", "9m", "6p", "9p", "1s", "2s", "3s", "4s", "3z", "4z"],
                    38,
                ),
                (
                    "2s",
                    ["4m", "5m", "6m", "7m", "8m", "9m", "6p", "9p", "3z", "4z"],
                    34,
                ),
            ],
        ),
    ],
)
def test_calculate_efficiency(test_input, expected):
    hand_count = HandCount.create_from_hand(get_hand_from_code(test_input))
    expected_efficiency = [
        EfficiencyData(
            discard_tile=get_tile_from_code(discard_tile_code),
            ukeire=list(map(get_tile_from_code, ukeire_codes)),
            ukeire_count=ukeire_count,
        )
        for discard_tile_code, ukeire_codes, ukeire_count in expected
    ]

    assert calculate_efficiency(hand_count) == expected_efficiency
