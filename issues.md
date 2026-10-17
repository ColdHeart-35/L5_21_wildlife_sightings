# Static Analysis Findings

| Issue | Type | Line(s) | Description | Fix Approach |
|-------|------|---------|-------------|--------------|
| SQL query built from input | Security, Bandit B608 (medium) | 9 | Species and zone values were inserted into SQL text, allowing malformed input to alter the query. | Use SQLite placeholders and pass values separately. |
| Weak MD5 hash | Security, Bandit B324 (high) | 15 | MD5 is unsuitable for security-sensitive hashing. | Use SHA-256 for the deterministic observer identifier. |
| Assert used for runtime check | Reliability, Bandit B101 (low) | 36 | Python can remove assertions when optimized, so they are not reliable runtime validation. | Remove the demo assertion; the returned totals are already used directly. |
| Mutable default argument | Correctness, Pylint W0102 | 8 | The default dictionary would be shared across calls that omit `extras`. | Default to `None` and initialize a fresh dictionary inside the function. |
| Poor naming and missing docstrings | Maintainability, Pylint C0103/C0114/C0116 | 1, 8, 14, 18, 26, 32 | Non-snake_case names and undocumented functions made the module harder to understand. | Use snake_case names and add concise module and function docstrings. |
| Long lines and ambiguous variable | Style, Flake8 E501/E741/E225 | 5, 9, 19, 27, 28 | Long SQL lines, a single-letter `l`, and missing spaces violated style rules. | Wrap SQL and expressions, use a descriptive name, and follow PEP 8 spacing. |

The line numbers refer to the original downloaded script. The corresponding baseline and final analyzer output is saved in the `before_*_report.txt` and `*_report.txt` files.
