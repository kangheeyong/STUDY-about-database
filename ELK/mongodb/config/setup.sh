#!/bin/bash

sleep 10 | echo Sleeping

mongo mongodb://mongodb1:27017 replicaSet.js
