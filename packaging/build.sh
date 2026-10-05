#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

VERSION="1.0.0"
DESCRIPTION="John 3:16 terminal screensaver"
MAINTAINER="CHOP4NCHO <chopanchodev@gmail.com>"
STAGE="dist/staging"

rm -rf dist
mkdir -p "$STAGE/usr/bin" "$STAGE/usr/share/j316" "$STAGE/usr/share/doc/j316"

cp run.py screensaver.py custom_addstr.py config.yaml "$STAGE/usr/share/j316/"
cp -r ascii_files "$STAGE/usr/share/j316/"
cp README.md LICENSE "$STAGE/usr/share/doc/j316/"

cat > "$STAGE/usr/bin/j316" <<'EOF'
#!/bin/sh
exec python3 /usr/share/j316/run.py "$@"
EOF
chmod 755 "$STAGE/usr/bin/j316"

fpm -s dir -t rpm -n j316 -v "$VERSION" -a noarch \
  --license MIT \
  --url "https://github.com/CHOP4NCHO/j316.git" \
  --maintainer "$MAINTAINER" \
  --description "$DESCRIPTION" \
  --depends python3 --depends python3-pyyaml \
  -p dist/ --force \
  -C "$STAGE" usr

fpm -s dir -t deb -n j316 -v "$VERSION" -a all \
  --license MIT \
  --url "" \
  --maintainer "$MAINTAINER" \
  --description "$DESCRIPTION" \
  --depends python3 --depends python3-yaml \
  -p dist/ --force \
  -C "$STAGE" usr

echo
echo "Paquetes generados:"
ls -la dist/*.rpm dist/*.deb
