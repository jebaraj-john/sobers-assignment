
## Steps to run Tool in Docker ##

### prerequisite ###
 - Docker to be installed

### Steps to run tool ###
 - Build docker image
 - create a container to run tool

 ```sh
   docker build -t sobers .
   docker run -it --rm -v /out:/app/data/out/ sobers python cli.py
```
### Command to run the testcase ###
 ```sh
docker run -it --rm sobers python -m unittest
```
