#!/bin/bash
envprjid=$(env |grep DEVSHELL_PROJECT_ID=) 
prjid=$(echo $envprjid | cut -d '=' -f 2)
gcloud projects describe $prjid |grep name