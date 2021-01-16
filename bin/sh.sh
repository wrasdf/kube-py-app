#!/bin/bash

set -euo pipefail

docker-compose down
docker-compose build sh
docker-compose run --rm --service-ports sh
