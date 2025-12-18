from __future__ import annotations

import ast
from dataclasses import dataclass
from typing import Union

Number = Union[int, float]


class CalculationError(Exception):
    """Raised when an expression cannot be evaluated safely."""


@dataclass
class EvaluationResult:
    expression: str
    value: Number


class _SafeEvaluator(ast.NodeVisitor):
    allowed_binops = (ast.Add, ast.Sub, ast.Mult, ast.Div, ast.FloorDiv, ast.Mod, ast.Pow)
    allowed_unary = (ast.UAdd, ast.USub)

    def visit(self, node: ast.AST) -> Number:  # type: ignore[override]
        if isinstance(node, ast.Expression):
            return self.visit(node.body)
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            return node.value
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, self.allowed_unary):
            operand = self.visit(node.operand)
            return +operand if isinstance(node.op, ast.UAdd) else -operand
        if isinstance(node, ast.BinOp) and isinstance(node.op, self.allowed_binops):
            left = self.visit(node.left)
            right = self.visit(node.right)
            return self._apply_binop(node.op, left, right)
        raise CalculationError(f"Unsupported expression: {ast.dump(node, include_attributes=False)}")

    def _apply_binop(self, op: ast.AST, left: Number, right: Number) -> Number:
        try:
            if isinstance(op, ast.Add):
                return left + right
            if isinstance(op, ast.Sub):
                return left - right
            if isinstance(op, ast.Mult):
                return left * right
            if isinstance(op, ast.Div):
                return left / right
            if isinstance(op, ast.FloorDiv):
                return left // right
            if isinstance(op, ast.Mod):
                return left % right
            if isinstance(op, ast.Pow):
                return left ** right
        except ZeroDivisionError as exc:
            raise CalculationError("Division by zero") from exc
        raise CalculationError("Unknown binary operation")


def evaluate_expression(expression: str) -> EvaluationResult:
    parsed = _parse_expression(expression)
    value = _SafeEvaluator().visit(parsed)
    return EvaluationResult(expression=expression.strip(), value=value)


def _parse_expression(expression: str) -> ast.Expression:
    try:
        return ast.parse(expression, mode="eval")  # type: ignore[return-value]
    except SyntaxError as exc:
        raise CalculationError("Invalid expression") from exc

