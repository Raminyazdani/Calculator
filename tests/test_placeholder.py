import pytest

from calculator_cli.core import CalculationError, evaluate_expression
from calculator_cli.history import History
from calculator_cli.cli import main, parse_args


def test_evaluate_expression_simple():
    result = evaluate_expression("1 + 2 * 3")
    assert result.value == 7


def test_evaluate_expression_division_by_zero():
    with pytest.raises(CalculationError):
        evaluate_expression("1 / 0")


def test_evaluate_expression_invalid():
    with pytest.raises(CalculationError):
        evaluate_expression("import os")


def test_history_add_and_last():
    history = History()
    first = evaluate_expression("2 + 2")
    history.add(first)
    second = evaluate_expression("3 + 4")
    history.add(second)

    assert history.last(1)[0].value == 7
    assert [r.value for r in history.last(2)] == [4, 7]


def test_cli_single_expression(monkeypatch, capsys):
    exit_code = main(["1+2"])
    captured = capsys.readouterr()
    assert exit_code == 0
    assert "= 3" in captured.out


def test_cli_error(monkeypatch, capsys):
    exit_code = main(["1/0"])
    captured = capsys.readouterr()
    assert exit_code == 1
    assert "error" in captured.out


def test_parse_args_theme_and_expr():
    args = parse_args(["--theme", "bright_blue", "2+2"])
    assert args.theme == "bright_blue"
    assert args.expr == "2+2"
