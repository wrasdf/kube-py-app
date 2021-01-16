#!/bin/bash

set -euo pipefail

docker-compose down
docker-compose build server
docker-compose run --service-ports -d --rm server
