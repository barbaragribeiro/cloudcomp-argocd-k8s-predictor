#!/bin/bash
curl -X POST $1:5005/api/american --data "{\"text\":\"$2\"}"
