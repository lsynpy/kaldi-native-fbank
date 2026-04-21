#!/usr/bin/env bash
set -euo pipefail

echo "=== Configuring CMake ==="
cmake -B build -S . -DCMAKE_EXPORT_COMPILE_COMMANDS=ON

echo "=== Building project ==="
cmake --build build -j$(nproc)

echo "=== Setting up IntelliSense ==="
ln -sf build/compile_commands.json .
echo "compile_commands.json linked for C++ IntelliSense"

echo "=== Configuring fish shell ==="
FISH_CONFIG="/root/.config/fish/config.fish"

# Auto-activate global venv
echo "source /opt/venv/bin/activate.fish" >> "$FISH_CONFIG"

# Add Python extension to path
echo "set -x PYTHONPATH /workspaces/kaldi-native-fbank/build/lib:/workspaces/kaldi-native-fbank/kaldi-native-fbank/python" >> "$FISH_CONFIG"

# Add C++ test binaries to path
echo "set -x PATH /workspaces/kaldi-native-fbank/build/bin \$PATH" >> "$FISH_CONFIG"

echo ""
echo "✅ Dev container setup complete!"
echo "   - Project built successfully"
echo "   - Python deps pre-installed at /opt/venv (cached)"
echo "   - Fish shell configured with auto-activation"
