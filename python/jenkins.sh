#!/usr/bin/env bash

echo "run jenkins"

jenkins_file="/Users/$USER/Library/Jenkins/jenkins.war"
jenkins_file_temp="/Users/$USER/Library/Jenkins/jenkins.war"

if [ ! -f jenkins_file ]; then
  echo "ERROR: jenkins file not exists, try to download..."
  curl "http://mirrors.jenkins.io/war-stable/latest/jenkins.war" --output jenkins_file_temp
  mv jenkins_file_temp jenkins_file
fi

java -jar jenkins --httpPort=8080.

echo "start jenkind on http://localhost:8080"
