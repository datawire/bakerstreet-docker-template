# Baker Street Docker Container Template #

A reusable template for creating Baker Street enabled Docker containers for your microservices.

## Requirements ##

1. [Docker](https://docker.com) is installed.
2. The datawire-directory is running somewhere that is routable from a Docker container, for example, the Docker host 
machine.

## Getting Started ##

1. Clone or fork this repository.

The project is setup with the expectation that developers will modify or replace certain files within the project and
ultimately beyond experimentation will commit the project and subsequent changes to their own VCS repository.

2. Open the Makefile and edit the top-lines:

NAMESPACE = Your Docker namespace.
NAME = The name of the image in the namespace.
VERSION = 

NAME = <repository>/<name>
VERSION = <version>

3. Run `make build` or `docker build -t $(NAME):$(VERSION) .`

## Usage Theory / Purpose ##

For a single experimenting developer it should be sufficient to clone this project out and then replace a handful of
files so that they can push a Docker image with their service installed on the image alongside Watson and Sherlock.

For a team of developers that expect to use this template in production we expect the template will be stored in an
organization controlled Git repository. Configuration files will be placed in the appropriate places and versioned. A
Continuous Integration server such as Jenkins will then clone this project and copy necessary service files into the
appropriate locations before building the image with Docker.

## Container Information ##

The Docker image is assembled using the Phusion baseimage-docker project as a base template and therefore is based on
Ubuntu 14. We may eventually replace the Phusion baseimage or provide an alternative CentOS template.

## FAQ ##