# Reflection

The handout asks for reflection answers but does not include the four question texts. These responses address the lab's stated learning outcomes.

1. **What does static analysis contribute?**
   It finds likely bugs, risky patterns, and style problems without running the program. This catches issues early and gives reviewers a consistent baseline for code quality.

2. **How do the tools differ?**
   Pylint checks broader code quality and maintainability, Flake8 focuses on Python style and common errors, and Bandit looks for security risks in Python code.

3. **Which findings mattered most in this program?**
   The dynamically constructed SQL query could be manipulated through input, and MD5 is a weak hash choice. The shared mutable default could also leak totals between separate calls. Parameterized SQL, SHA-256, and a `None` default address these problems.

4. **What was learned from using the tools together?**
   Their reports overlap in places but provide different kinds of evidence. Fixing their findings improved safety and readability, and rerunning them confirmed the remaining code follows the selected checks.
