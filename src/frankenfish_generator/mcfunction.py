def fix_whitespace(function_src: str) -> str:
    lines = function_src.splitlines()
    fixed_lines = map(lambda line: str.join(" ", line.split()), lines)
    return str.join("\n", fixed_lines)
