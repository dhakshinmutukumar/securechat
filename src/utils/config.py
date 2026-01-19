from pathlib import Path
import tomli


def _find_pyproject() -> Path:
    """
    Walk upwards from this file until pyproject.toml is found.
    This does NOT rely on environment variables.
    """
    current = Path(__file__).resolve()

    for parent in current.parents:
        candidate = parent / "pyproject.toml"
        if candidate.is_file():
            return candidate

    raise RuntimeError("pyproject.toml not found in parent directories")


# Locate pyproject.toml
_PYPROJECT_PATH = _find_pyproject()

# Load TOML
with _PYPROJECT_PATH.open("rb") as f:
    _config = tomli.load(f)

try:
    _app_cfg = _config["tool"]["chatapp"]
except KeyError as exc:
    raise RuntimeError("Missing [tool.chatapp] section in pyproject.toml") from exc


# Public configuration values
DB_NAME: str = _app_cfg["db_name"]
SENDER_EMAIL: str = _app_cfg["sender_email"]
SENDER_PASSWORD: str = _app_cfg["sender_password"]


# ---- Fail-fast validation (MANDATORY) ----
if not DB_NAME:
    raise RuntimeError("db_name is empty in pyproject.toml")

if not SENDER_EMAIL or not SENDER_PASSWORD:
    raise RuntimeError("Email credentials missing in pyproject.toml")
