The project's structure is based on https://github.com/big-data-europe/docker-spark

Differences:
1. Base image changed to rappdw/docker-java-python
2. Cut off some unused parts.
3. Add flask support in "shared" image
4. Mounted "shared" directory for all images

The project provide necessary tools for drafting spark-based tasks. 
By default, it can by started with run.sh script.


Instruction:
1. If docker and docker-compose are not installed, run:
```bash
sudo apt-get update && sudo apt-get install docker docker-compose
```
2. Run script that creates db, builds images and starts the project.
```bash
sudo ./run.sh
```
