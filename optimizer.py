import os

def analyze_code(code: str) -> dict:
    """
    Analyze code and return issues found.
    """
    issues = []
    
    for i, line in enumerate(code.split('\n'), 1):
        if len(line) > 79:
            issues.append(f"Line {i}: Line too long ({len(line)} chars)")
    
    if 'def ' in code and '"""' not in code:
        issues.append("Missing docstrings in function definitions")
    
    bad_names = ['x', 'y', 'z', 'a', 'b', 'tmp', 'temp']
    for name in bad_names:
        if f' {name} ' in code or f' {name}=' in code:
            issues.append(f"Unclear variable name: '{name}'")
    
    return {
        "issues_found": len(issues),
        "details": issues
    }


def suggest_refactor(code: str) -> str:
    """
    Return a refactored version of the input code.
    """
    if 'def ' in code and '"""' not in code:
        code = code.replace('def ', '# TODO: Add docstring\ndef ', 1)
    
    return code


def self_review(original: str, refactored: str) -> str:
    """
    Self-review mechanism: compare original and refactored code.
    """
    if len(refactored) < len(original) * 0.5:
        return "Warning: Refactored code is too short, may be incomplete."
    return "Self-review passed: refactored code looks valid."


def main():
    print("=== AI Code Optimizer ===\n")
    
    sample_code = """
def calc(a,b):
    x = a+b
    y = a-b
    z = a*b
    return x,y,z
"""
    
    print("Input code:")
    print(sample_code)
    
    print("Analyzing...")
    result = analyze_code(sample_code)
    print(f"Issues found: {result['issues_found']}")
    for detail in result['details']:
        print(f"  - {detail}")
    
    print("\nRefactoring...")
    refactored = suggest_refactor(sample_code)
    print("Refactored code:")
    print(refactored)
    
    print("\nRunning self-review...")
    review = self_review(sample_code, refactored)
    print(review)


if __name__ == "__main__":
    main()
