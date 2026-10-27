# Hive-Box: Real World DevOps Project

Version: v0.0.1
[![CI/Tests](https://github.com/TusharPulakala/hive-box/actions/workflows/ci.yml/badge.svg)](https://github.com/TusharPulakala/hive-box/actions/workflows/ci.yml) [![OSSF](https://github.com/TusharPulakala/hive-box/actions/workflows/scorecard.yml/badge.svg)](https://github.com/TusharPulakala/hive-box/actions/workflows/scorecard.yml)
A Docker **containerised** REST api with two endpoints:-
1. /version - returns the current app version
2. /temperature - returns current average temperature based on real world senseBoxes reading within last 1 hour

### Features:
- Fetch real world temperature readings from around the world
- Uses Opensense data from community developed and maintained Senseboxes
- Containerised api for easy deployment

### Usage:
Prerequisites: Docker ([Docker Installation](https://docs.docker.com/engine/install/))

Clone this repository to your local system
```bash
git clone https://github.com/Tusharcoder18/hive-box.git
```
Rename .env.example to .env and update the box ids as required. These values can also be set as environment variables.
Build the docker image
```bash
docker build -t hive-box .
```
Run the docker image
```bash
docker run -d --name hive-box -p 127.0.0.1:8000:8000 hive-box
```
Access the API docs at: http://127.0.0.1:8000/docs

### Project Structure:

```text
/
├── Dockerfile
├── README.md
├── api/
├── pyproject.toml
├── tests/
└── uv.lock
```
