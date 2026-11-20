"""Plan a Git bisect session without changing repository state."""
from __future__ import annotations
import argparse
import math
import subprocess
from pathlib import Path


def run_git(repo: Path, *args: str) -> str:
    result = subprocess.run(["git", *args], cwd=repo, text=True,
                            capture_output=True, check=False)
    if result.returncode:
        raise ValueError(result.stderr.strip() or f"git {' '.join(args)} failed")
    return result.stdout.strip()


def estimated_steps(commit_distance: int) -> int:
    if commit_distance < 1:
        raise ValueError("commit distance must be positive")
    return math.ceil(math.log2(commit_distance + 1))


def plan(repo: Path, good: str, bad: str) -> tuple[str, str, int]:
    good_sha = run_git(repo, "rev-parse", "--verify", f"{good}^{{commit}}")
    bad_sha = run_git(repo, "rev-parse", "--verify", f"{bad}^{{commit}}")
    ancestor = subprocess.run(["git", "merge-base", "--is-ancestor", good_sha, bad_sha],
                              cwd=repo, capture_output=True, check=False)
    if ancestor.returncode != 0:
        raise ValueError("the good commit must be an ancestor of the bad commit")
    distance = int(run_git(repo, "rev-list", "--count", f"{good_sha}..{bad_sha}"))
    if distance < 1:
        raise ValueError("the bad commit must be later than the good commit")
    return good_sha, bad_sha, distance


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path("."))
    parser.add_argument("--good", required=True, help="Known-good commit or ref")
    parser.add_argument("--bad", required=True, help="Known-bad commit or ref")
    args = parser.parse_args(argv)
    try:
        good_sha, bad_sha, distance = plan(args.repo.resolve(), args.good, args.bad)
    except (ValueError, OSError) as exc:
        parser.error(str(exc))
    print("Read-only Git bisect plan")
    print(f"Good: {good_sha}")
    print(f"Bad:  {bad_sha}")
    print(f"Commits between endpoints: {distance}")
    print(f"Estimated binary-search checks: {estimated_steps(distance)}")
    print("\nReview and run these commands yourself:")
    repo_arg = '"' + str(args.repo).replace('"', '\\"') + '"'
    print(f"  git -C {repo_arg} bisect start {bad_sha} {good_sha}")
    print("  git bisect run <your-test-command>")
    print("  git bisect reset")
    print("\nNo Git bisect command was executed and no repository state was changed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
