import ast
import builtins
from pathlib import Path

BUILTINS = set(dir(builtins))
SOURCE_FILES = [p for p in Path(".").glob("*.py") if p.name != "setup.py"]


def get_assigned_names(filepath):
    source = filepath.read_text()
    tree = ast.parse(source)
    names = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id in BUILTINS:
                    names.append(target.id)
        elif isinstance(node, ast.AugAssign):
            if isinstance(node.target, ast.Name) and node.target.id in BUILTINS:
                names.append(node.target.id)
    return names


def test_no_builtin_shadowing():
    """Переменные не должны перекрывать встроенные имена Python (sum, max, min, list и т.д.)"""
    violations = {}
    for filepath in SOURCE_FILES:
        shadowed = get_assigned_names(filepath)
        if shadowed:
            violations[filepath.name] = shadowed
    assert not violations, (
        "Используются имена встроенных функций Python как переменные!\n"
        + "\n".join(
            f"  {f}: {', '.join(names)}" for f, names in violations.items()
        )
        + "\nПереименуй: sum → total, list → result, max → maximum и т.д."
    )
