Write-Host "Checking Python and pip installation..."

if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Error "Python is not installed or not in PATH."
    exit 1
}

$pipCheck = python -m pip --version 2>$null
if (-not $pipCheck) {
    Write-Host "pip not found. Attempting to install pip..."
    python -m ensurepip --upgrade
}

Write-Host "Installing required packages: tweepy and python-dotenv..."

python -m pip install --upgrade pip
python -m pip install tweepy python-dotenv

Write-Host "Dependencies installed successfully."