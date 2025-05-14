import pytest

from tests.conftest import payout_data_generator2, payout_data_generator


@pytest.mark.parametrize("input_args, expected", [
    (payout_data_generator(), (
        1, "Marketing", "alice@example.com"
    )),
    (payout_data_generator2(), (
        2, "HR", "grace@example.com"
    )),
])
def test_payout_author(payout_author, input_args, expected):
    print(input_args)
    report = payout_author.create_report([input_args])
    assert len(report) == expected[0]
    assert report[0].department == expected[1]
    assert report[0].email == expected[2]