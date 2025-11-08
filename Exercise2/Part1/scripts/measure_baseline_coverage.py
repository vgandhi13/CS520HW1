"""
Measure baseline coverage for all problems using pytest-cov.
Handles all variants (4 per problem: COT and SCOT for both models).
"""
import json
import subprocess
import sys
import xml.etree.ElementTree as ET
import ast
import re
from pathlib import Path
from collections import defaultdict


def run_coverage_measurement():
    """Run pytest with coverage and collect results."""
    
    base_dir = Path(__file__).parent.parent
    tests_dir = base_dir / "tests_baseline"
    solutions_dir = base_dir / "solutions"
    reports_dir = base_dir / "coverage_reports"
    reports_dir.mkdir(exist_ok=True)
    
    # Load solutions info
    solutions_info_path = base_dir / "solutions_info.json"
    with open(solutions_info_path, 'r') as f:
        solutions_info = json.load(f)
    
    # Load problems
    problems_path = base_dir.parent / "Part 1" / "problems.json"
    with open(problems_path, 'r') as f:
        problems = json.load(f)
    
    problem_info = {p['id']: p for p in problems}
    
    print("Running baseline coverage measurement for all variants...")
    print(f"{'='*70}")
    
    # Run pytest with coverage for each variant
    coverage_results = {}
    
    for problem_id, variants in solutions_info.items():
        problem_num = problem_id.split('_')[-1]
        entry_point = problem_info[problem_id]['entry_point']
        
        for variant in variants:
            variant_id = variant['variant_id']
            solution_file = Path(variant['file'])
            module_name = solution_file.stem  # e.g., "problem_0_Llama_cot"
            
            # Run pytest with coverage for this specific variant
            test_file = tests_dir / f"test_problem_{problem_num}_{variant_id}.py"
            
            if not test_file.exists():
                print(f"⚠️  Test file not found: {test_file}")
                continue
            
            result_key = f"{problem_id}_{variant_id}"
            status_icon = "✅" if variant.get('passed', False) else "❌"
            print(f"\n📊 {status_icon} {problem_id} [{variant_id}] ({entry_point})...")
            
            # Extract test case count from the problem's test code
            # This gives us the total number of test cases
            test_case_total = 0
            try:
                # Load the problem's test code directly from problems.json
                problem = problem_info[problem_id]
                test_code = problem['test']
                # Parse the test code to find inputs list
                tree = ast.parse(test_code)
                for node in ast.walk(tree):
                    if isinstance(node, ast.Assign):
                        for target in node.targets:
                            if isinstance(target, ast.Name) and target.id == 'inputs':
                                # Found inputs assignment - count list elements
                                if isinstance(node.value, ast.List):
                                    test_case_total = len(node.value.elts)
                                    break
                # Fallback: try executing the test code
                if test_case_total == 0:
                    exec_ns = {}
                    exec(test_code, exec_ns)
                    # Check if inputs is in the namespace (might be in check function's scope)
                    if 'inputs' in exec_ns:
                        test_case_total = len(exec_ns['inputs'])
            except Exception as e:
                # If we can't extract, we'll fall back to pytest's count
                pass
            
            # Run pytest with coverage - use module path with dots
            cmd = [
                sys.executable, "-m", "pytest",
                str(test_file),
                f"--cov=solutions.{module_name}",
                "--cov-branch",  # Enable branch coverage
                "--cov-report=term",
                "--cov-report=xml",
                f"--cov-report=html:{reports_dir}/{module_name}",
                "-v"
            ]
            
            try:
                result = subprocess.run(
                    cmd,
                    cwd=str(base_dir),
                    capture_output=True,
                    text=True,
                    timeout=30
                )
                
                # Parse coverage from stdout (term report)
                output = result.stdout + result.stderr
                line_cov = 0.0
                branch_cov = 0.0
                tests_passed = 0
                tests_failed = 0
                tests_total = 0
                
                # Parse test results from pytest output
                # Look for patterns like "X passed", "X failed", "X passed, Y failed in Zs"
                passed_match = re.search(r'(\d+)\s+passed', output)
                failed_match = re.search(r'(\d+)\s+failed', output)
                error_match = re.search(r'(\d+)\s+error', output)
                
                # Also look for test case count in output
                # Format: "TEST_CASES: X/Y passed" or "TEST_CASES: Only X/Y test cases passed"
                test_case_match = re.search(r'TEST_CASES:\s*(?:Only\s+)?(\d+)/(\d+)\s+(?:test\s+cases\s+)?passed', output)
                
                if test_case_match:
                    # Extract from test case count message
                    tests_passed = int(test_case_match.group(1))
                    tests_total = int(test_case_match.group(2))
                    tests_failed = tests_total - tests_passed
                elif test_case_total > 0:
                    # We extracted total from test file, now determine passed/failed
                    # If pytest says 1 passed, all test cases passed
                    # If pytest says 1 failed, some test cases failed
                    if passed_match and int(passed_match.group(1)) > 0:
                        # Test function passed, so all test cases passed
                        tests_passed = test_case_total
                        tests_total = test_case_total
                        tests_failed = 0
                    elif failed_match or error_match:
                        # Test function failed, need to parse how many test cases passed
                        # Try to extract from error message or use 0
                        tests_total = test_case_total
                        tests_passed = 0  # Default to 0 if we can't determine
                        tests_failed = test_case_total
                    else:
                        tests_total = test_case_total
                        tests_passed = 0
                        tests_failed = 0
                elif passed_match:
                    # Fallback to pytest's count (this is test functions, not test cases)
                    tests_passed = int(passed_match.group(1))
                    if failed_match:
                        tests_failed = int(failed_match.group(1))
                    else:
                        tests_failed = 0
                    if error_match:
                        tests_failed += int(error_match.group(1))  # Errors count as failures
                    tests_total = tests_passed + tests_failed
                else:
                    # No test results found
                    tests_total = 0
                
                # Look for coverage percentage in the output
                # Format with branch coverage: "solutions/problem_X_variant.py     10      0     5      1   100%   80%"
                lines = output.split('\n')
                for i, line in enumerate(lines):
                    # Look for lines with the module name and percentage
                    if module_name in line or f"solutions/{module_name}" in line:
                        parts = line.split()
                        percentages = []
                        for part in parts:
                            if "%" in part:
                                try:
                                    pct = float(part.replace('%', ''))
                                    percentages.append(pct)
                                except:
                                    pass
                        if len(percentages) >= 1:
                            line_cov = percentages[0]
                        if len(percentages) >= 2:
                            branch_cov = percentages[1]
                    
                    # Also check for TOTAL line which has coverage
                    if "TOTAL" in line and ("Cover" in lines[i-1] if i > 0 else False):
                        parts = line.split()
                        percentages = []
                        for part in parts:
                            if "%" in part:
                                try:
                                    pct = float(part.replace('%', ''))
                                    percentages.append(pct)
                                except:
                                    pass
                        if len(percentages) >= 1 and line_cov == 0.0:
                            line_cov = percentages[0]
                        if len(percentages) >= 2 and branch_cov == 0.0:
                            branch_cov = percentages[1]
                
                # Try parsing XML if available
                xml_file = base_dir / "coverage.xml"
                if xml_file.exists() and (line_cov == 0.0 or branch_cov == 0.0):
                    try:
                        tree = ET.parse(xml_file)
                        root = tree.getroot()
                        
                        # Get overall coverage from root
                        if line_cov == 0.0:
                            line_rate = float(root.get('line-rate', 0)) * 100
                            line_cov = line_rate
                        if branch_cov == 0.0:
                            branch_rate = float(root.get('branch-rate', 0)) * 100
                            branch_cov = branch_rate
                        
                        # Try to get from packages
                        packages = root.findall('.//package')
                        for package in packages:
                            classes = package.findall('.//class')
                            for cls in classes:
                                if line_cov == 0.0:
                                    line_rate = float(cls.get('line-rate', 0)) * 100
                                    line_cov = line_rate
                                if branch_cov == 0.0:
                                    branch_rate = float(cls.get('branch-rate', 0)) * 100
                                    branch_cov = branch_rate
                                if line_cov > 0 and branch_cov > 0:
                                    break
                    except Exception as e:
                        pass
                    
                    # Clean up XML file
                    xml_file.unlink()
                
                if line_cov > 0 or result.returncode == 0 or tests_total > 0:
                    coverage_results[result_key] = {
                        'problem_id': problem_id,
                        'variant_id': variant_id,
                        'model': variant.get('model_short', 'unknown'),
                        'strategy': variant.get('strategy', 'unknown'),
                        'line_coverage': round(line_cov, 2),
                        'branch_coverage': round(branch_cov, 2),
                        'entry_point': entry_point,
                        'tests_passed': tests_passed,
                        'tests_failed': tests_failed,
                        'tests_total': tests_total,
                        'passed': variant.get('passed', False) and result.returncode == 0
                    }
                    
                    if line_cov > 0:
                        print(f"   Line coverage: {line_cov:.2f}%")
                        if branch_cov > 0:
                            print(f"   Branch coverage: {branch_cov:.2f}%")
                    else:
                        print(f"   ⚠️  Could not extract coverage metrics")
                
                # Check if tests passed
                if tests_total > 0:
                    print(f"   Tests: {tests_passed}/{tests_total} passed", end="")
                    if tests_failed > 0:
                        print(f" ({tests_failed} failed)")
                    else:
                        print()
                elif result.returncode == 0:
                    print(f"   ✅ Tests passed")
                else:
                    print(f"   ⚠️  Tests failed or had issues")
                    if result.stderr:
                        print(f"   Error output: {result.stderr[:200]}")
            
            except subprocess.TimeoutExpired:
                print(f"   ⚠️  Timeout while measuring coverage")
                coverage_results[result_key] = {
                    'problem_id': problem_id,
                    'variant_id': variant_id,
                    'line_coverage': 0.0,
                    'branch_coverage': 0.0,
                    'entry_point': entry_point,
                    'tests_passed': 0,
                    'tests_failed': 0,
                    'tests_total': 0,
                    'passed': False,
                    'error': 'Timeout'
                }
            except Exception as e:
                print(f"   ❌ Error: {str(e)}")
                coverage_results[result_key] = {
                    'problem_id': problem_id,
                    'variant_id': variant_id,
                    'line_coverage': 0.0,
                    'branch_coverage': 0.0,
                    'entry_point': entry_point,
                    'tests_passed': 0,
                    'tests_failed': 0,
                    'tests_total': 0,
                    'passed': False,
                    'error': str(e)
                }
    
    # Generate summary table - group by problem
    print(f"\n{'='*105}")
    print("BASELINE COVERAGE SUMMARY (All Variants)")
    print(f"{'='*105}")
    print(f"{'Variant':<20} {'Line %':>9} {'Branch %':>10} {'Test Cases':>16} {'Status':<8}")
    print(f"{'-'*105}")
    
    # Group by problem_id for better organization
    by_problem = {}
    for key, result in coverage_results.items():
        problem_id = result['problem_id']
        if problem_id not in by_problem:
            by_problem[problem_id] = []
        by_problem[problem_id].append(result)
    
    for problem_id in sorted(by_problem.keys(), key=lambda x: int(x.split('_')[-1])):
        variants = by_problem[problem_id]
        # Print problem name on its own line
        problem_short = problem_id.replace('humaneval_', '')
        entry_point = variants[0].get('entry_point', 'unknown') if variants else 'unknown'
        print(f"\n{problem_short} ({entry_point}):")
        for result in sorted(variants, key=lambda x: x.get('variant_id', '')):
            variant_id = result.get('variant_id', 'unknown')
            line_cov = result['line_coverage']
            branch_cov = result['branch_coverage']
            tests_passed = result.get('tests_passed', 0)
            tests_total = result.get('tests_total', 0)
            passed = result.get('passed', False)
            
            tests_str = f"{tests_passed}/{tests_total}" if tests_total > 0 else "N/A"
            status = "✅ PASS" if passed else "❌ FAIL"
            # Better alignment with consistent spacing - right-align numbers
            print(f"  {variant_id:<18} {line_cov:>8.2f}%  {branch_cov:>8.2f}%  {tests_str:>16}  {status}")
    
    # Also create a summary by problem (aggregate)
    print(f"\n{'='*70}")
    print("SUMMARY BY PROBLEM (Average across variants)")
    print(f"{'='*70}")
    print(f"{'Problem':<30} {'Entry Point':<25} {'Avg Line %':<12} {'Avg Branch %':<12} {'Passing':<10}")
    print(f"{'-'*80}")
    
    for problem_id in sorted(by_problem.keys(), key=lambda x: int(x.split('_')[-1])):
        variants = by_problem[problem_id]
        entry = variants[0]['entry_point'] if variants else 'unknown'
        avg_line = sum(r['line_coverage'] for r in variants) / len(variants) if variants else 0
        avg_branch = sum(r['branch_coverage'] for r in variants) / len(variants) if variants else 0
        passing = sum(1 for r in variants if r.get('passed', False))
        total = len(variants)
        print(f"{problem_id:<30} {entry:<25} {avg_line:>10.2f}%  {avg_branch:>10.2f}%  {passing}/{total}")
    
    # Save results
    results_path = base_dir / "baseline_coverage_results.json"
    with open(results_path, 'w') as f:
        json.dump(coverage_results, f, indent=2)
    
    print(f"{'='*70}")
    print(f"\n✅ Coverage results saved to: {results_path}")
    print(f"   HTML reports available in: {reports_dir}")
    
    return coverage_results


if __name__ == '__main__':
    run_coverage_measurement()
