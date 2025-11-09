# Repository Guidelines

## Project Structure & Module Organization
- `examples/`: 6 stand-alone Python scripts (3 t-tests, 3 chi-square) that print results when run. Use them as the canonical reference for statistical workflows.
- `README.md`: public-facing overview used as the GitHub landing page; keep it synchronized with any new scripts or setup notes.
- `AGENTS.md`: internal contributor guide (this file). Add new internal policies here rather than cluttering the README.

## Build, Test, and Development Commands
```bash
uv venv .venv && source .venv/bin/activate
uv pip install --upgrade numpy scipy
uv run python examples/t_test_one_sample.py  # swap for any script to validate behavior
```
- Scripts are deterministic; running them is the primary verification step today. Add `pytest` entry points under `tests/` if automated checks become necessary. `uv run pytest` keeps dependency resolution consistent.

## Coding Style & Naming Conventions
- Python 3.10+ with 4-space indentation, UTF-8 source.
- Prefer descriptive variable names (`observed_sales`, `population_mean`).
- Keep inline comments bilingual only when it clarifies concepts for Japanese readers; default to English docstrings and Japanese explanatory comments as seen in existing files.
- Use SciPy/NumPy idioms (`np.array`, `stats.ttest_ind`). Avoid pandas unless the repo structure changes.

## Testing Guidelines
- No formal framework yet. When adding tests, place them under `tests/` mirroring the `examples/` structure (e.g., `tests/test_t_tests.py`).
- Name test functions `test_<behavior>` and ensure they can run via `pytest` without network access.
- For manual checks, run each impacted script and capture stdout in the PR description.

## Commit & Pull Request Guidelines
- Use concise, descriptive commit messages (e.g., `add welch t-test example`, `doc: update chi-square guide`).
- Each PR should: summarize changes, list verification commands, and link related issues. Include screenshots only when output formatting changes.
- Avoid bundling unrelated statistical techniques in one PR; separate by test type or documentation change for easier reviews.

## Security & Configuration Tips
- No secrets belong in this repo. Sample data is synthetic—keep it that way.
- When documenting dependency commands, prefer `uv pip install <package>==<version>` snippets so Codespaces/CI environments can reproduce the lock-free setup consistently.
