#/bin/bash 
docker build . -f Dockerfile.centos -t dfalkner/azure-linux-training:centos
docker build . -f Dockerfile.ubuntu -t dfalkner/azure-linux-training:ubuntu
