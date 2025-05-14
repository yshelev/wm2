import pytest

from workers.workers import EmptyInputDataException


@pytest.mark.parametrize("input_args, expected", [
    (["file.csv"],                                      # input
     (["file.csv"], None)),                             # expected output
    (["file.csv", "file1.csv", "file2.csv"],
     (["file.csv", "file1.csv", "file2.csv"], None)),
    (["file1.csv", "-r", "payout"],
     (["file1.csv"], "payout")),
    (["file2.csv", "--report", "payout"],
     (["file2.csv"], "payout")),
])
def test_parser_args(arg_parser, monkeypatch, input_args, expected):
    monkeypatch.setattr("sys.argv", ["main.py"] + input_args)
    assert arg_parser.parse() == expected