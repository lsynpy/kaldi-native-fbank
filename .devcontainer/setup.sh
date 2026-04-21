#!/usr/bin/env bash
set -euo pipefail

echo "=== Cleaning stale build ==="
rm -rf build

echo "=== Configuring CMake ==="
cmake -B build -S . -DCMAKE_EXPORT_COMPILE_COMMANDS=ON

echo "=== Building project ==="
cmake --build build -j$(nproc)

echo "=== Creating uv virtual environment ==="
uv venv --clear

echo "=== Installing Python dependencies ==="
uv pip install numpy pytest cmake
uv pip install torch==2.4.0+cpu -f https://download.pytorch.org/whl/torch/
uv pip install kaldifeat==1.25.4.dev20240725+cpu.torch2.4.0 -f https://csukuangfj.github.io/kaldifeat/cpu.html

echo "=== Setting up IntelliSense ==="
ln -sf build/compile_commands.json .
echo "compile_commands.json linked for C++ IntelliSense"

echo "=== Configuring fish shell ==="
FISH_CONFIG="/root/.config/fish/config.fish"

# Auto-activate venv
echo "source /workspaces/kaldi-native-fbank/.venv/bin/activate.fish" >> "$FISH_CONFIG"

# Add Python extension to path
echo "set -x PYTHONPATH /workspaces/kaldi-native-fbank/build/lib:/workspaces/kaldi-native-fbank/kaldi-native-fbank/python" >> "$FISH_CONFIG"

# Add C++ test binaries to path
echo "set -x PATH /workspaces/kaldi-native-fbank/build/bin \$PATH" >> "$FISH_CONFIG"

echo ""
echo "✅ Dev container setup complete!"
echo "   - Project built successfully"
echo "   - uv venv created at .venv/"
echo "   - Fish shell configured with auto-activation"
