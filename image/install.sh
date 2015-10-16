#!/bin/bash -ex
source /img_build/buildconfig

curl -s https://packagecloud.io/install/repositories/datawire/${DATAWIRE_REPOSITORY}/script.deb.sh | bash
apt-get install -y datawire-proton datawire-directory datawire-sherlock datawire-watson python-pip
yes | pip install docopt flask 
