#!/bin/bash

# script for dropping database and removing users to start from scratch

echo "Enter mysql password for root user"
mysql -u root -p < ./scripts/sqlscripts/cleanup.sql

