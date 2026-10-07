## Hive-Box: Real World DevOps Project

Version: v0.0.1

A simple **containerised** app with a basic functionality to print the _current version_ of the app.

### Features:
1. Prints the current app version

### Usage:
Prerequisites: Docker

Clone this repository to your local system
```bash
git clone https://github.com/Tusharcoder18/hive-box.git
```
Build the docker image
```bash
docker build -t hive-box .
```
Run the docker image
```bash
docker run --rm hive-box
```


### Project Structure:

```text
root/
├── Dockerfile
├── README.md
├── _version.py
└── main.py
```


