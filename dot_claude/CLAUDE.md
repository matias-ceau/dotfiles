# CLAUDE.md — Global Preferences

## Context Awareness & Role
Before starting a task, use your bash capabilities to determine your context:
- **Project Mode:** If inside a Git repository (`git rev-parse --is-inside-work-tree`) or a directory with a `pyproject.toml`, apply all strict development, testing, and Git rules below.
- **System Helper Mode:** If modifying loose configuration files or dotfiles, do not enforce project-level validation unless applicable.

## Language & Communication
- Match the language of my prompt for explanations and conversations.
- Code, variables, identifiers, file names, and commit messages must always remain in English.

## Execution & Agent Capabilities
- You have full permissions to execute bash commands. Run commands directly to accomplish tasks.
- **Crucial:** If you are ever in a context where bash execution is disabled or fails, explicitly state that you cannot run the command and ask me to run it. NEVER hallucinate terminal outputs, test results, or command executions.

## Python Environment & Tooling
- Target the latest stable Python version managed exclusively via `uv`. Downgrade only if dependencies explicitly require it.
- **Project Initialization:** If starting a new project or if no `pyproject.toml` exists, run `uv init [arguments]`.
- **Dependencies & Environment:** Use `uv add <package>` (or `--dev`). `uv` automatically creates and manages the `.venv`. **Do not manually create or `source` virtual environments.** Always rely on `uv run <command>` for execution.
- Never use `pip install` directly; never install packages globally.
- **`uv` usage rule:** Use `uv help` and `uv help <command>` dynamically via bash. Avoid `tldr uv`.

## Code Style & Quality
- Prefer the standard library (stdlib) over third-party dependencies.
- Zero secondary Python subprocesses if possible (prefer native APIs).
- Type hints are required on all public signatures.
- **Linting & Formatting:** Use `uv run ruff check --fix` and `uv run ruff format`.
- **Type Checking:** Use `uv run pyright` (or `mypy` if configured).

## Advanced Autonomous Workflows (Delegated Engineering)

### 1. Feature Development (Spec-First & Parallel Fan-Out)
When asked to build a new feature, do not immediately write implementation code.
1. **Spec Phase:** Read the codebase and write a `SPEC.md` detailing user-visible behavior, CLI/API surface, edge cases, and non-goals. Ask clarifying questions if anything is ambiguous.
2. **Approval:** Wait for my approval on `SPEC.md`.
3. **Execution Tracks:** Break the work into distinct, logically separate tasks:
   - **Track A (Tests):** Write a failing test suite based *strictly* on `SPEC.md`. Do not read the implementation.
   - **Track B (Logic):** Write the implementation.
   - **Track C (Audit):** Update docs, README, type hints, and callers.
4. **Reconciliation:** Run the suite. Use `SPEC.md` as the tiebreaker for any test/implementation disagreements.

### 2. Refactoring (Autonomous Red-Green Loops)
When given a refactoring or performance goal, treat the existing test suite as an unbreakable contract.
- **Isolation:** Work in a fresh Git worktree (e.g., `branch refactor/<name>`) so failed experiments cost nothing.
- **Baseline:** Run the test suite before starting and record the baseline.
- **The Loop:** Make one focused change → run the suite → read failures → fix. Repeat until green.
- **Hard Rule:** You may NOT delete, skip, xfail, or weaken any existing test. If a test encodes wrong behavior, stop and ask me.
- **Commit States:** Commit after every green state with a descriptive message.
- **Stuck State:** If you fail to resolve the same test error after 3 attempts, stop. Write a `STUCK.md` explaining what you tried and what you suspect the root cause is. 

## Testing & Validation Workflow
- Framework: `pytest`. Main command: `uv run pytest tests/ -v`.
- **Validation Checklist before reporting work as done:**
  1. Run `ruff` checks and formatting.
  2. Run `pyright` to verify type hints.
  3. Run `pytest -q` and explicitly report the passing test count.
- **Network:** Mock `http.client` (or equivalent) for HTTP tests. No real outbound network requests.

## Git Rules
- Stable branch: `main` (for semver tagged releases: `vX.Y.Z -a`).
- Development: `dev/<feature>` → merge to `main` only when all tests pass.
- Never `git commit --amend`, `rebase`, or `force-push` a commit already pushed to a remote.
- Never commit an empty `README.md` or useless stub files.
