#!/usr/bin/env bash
set -euo pipefail

echo "==> Installing Python 3..."

if command -v python3 >/dev/null 2>&1; then
    echo "Python 3 is already installed: $(python3 --version)"
else
    if command -v apt-get >/dev/null 2>&1; then
        sudo apt-get update
        sudo apt-get install -y python3 python3-pip python3-venv
    elif command -v dnf >/dev/null 2>&1; then
        sudo dnf install -y python3 python3-pip
    elif command -v yum >/dev/null 2>&1; then
        sudo yum install -y python3 python3-pip
    elif command -v pacman >/dev/null 2>&1; then
        sudo pacman -Sy --noconfirm python python-pip
    elif command -v brew >/dev/null 2>&1; then
        brew install python3
    else
        echo "Error: could not detect a supported package manager (apt, dnf, yum, pacman, brew)." >&2
        echo "Please install Python 3 manually and re-run this script." >&2
        exit 1
    fi
fi

echo "==> Ensuring pip is available..."
if ! python3 -m pip --version >/dev/null 2>&1; then
    if command -v apt-get >/dev/null 2>&1; then
        sudo apt-get install -y python3-pip
    else
        python3 -m ensurepip --upgrade
    fi
fi

echo "==> Installing colorama>=0.4.6..."
python3 -m pip install --upgrade pip
python3 -m pip install "colorama>=0.4.6"

echo "==> Verifying installation..."
python3 -c "import colorama; print('colorama version:', colorama.__version__)"

echo "==> Done."