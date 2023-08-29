$VENV_NAME = ".venv"
python -m venv $VENV_NAME

$activateScript = Join-Path $VENV_NAME "Scripts\Activate.ps1"
if (Test-Path $activateScript) {
    & $activateScript
} else {
    Write-Host "Activate script not found in $($activateScript)"
    exit 1
}

pip install -r requirements.txt
pip install -r requirements_dev.txt
