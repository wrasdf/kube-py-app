#!/bin/bash

set -euo pipefail

if [ "$#" -lt 1 ]; then
  echo
  echo "usage: release.sh <ImageTag>"
  echo "  ie. release.sh ded3966d228"
  exit 255
fi

APP_IMAGE_TAG=${1}
APP_IMAGE_TAG=${APP_IMAGE_TAG} docker-compose build release
APP_IMAGE_TAG=${APP_IMAGE_TAG} docker-compose push release
