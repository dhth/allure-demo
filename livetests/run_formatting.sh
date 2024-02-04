#!/bin/sh
set -e

GREEN='\033[0;32m'
ORANGE='\033[0;33m'
NC='\033[0m'
counter=1
total_steps=2

echo "Running linting and formatting"

echo "${ORANGE}[$counter/$total_steps] running 'ruff check'${NC}"
ruff check livetests
echo "${GREEN}[DONE]${NC} ✅"
counter=$((counter+1))

echo "${ORANGE}[$counter/$total_steps] running 'ruff format'${NC}"
ruff format livetests
echo "${GREEN}[DONE]${NC} ✅"
counter=$((counter+1))
