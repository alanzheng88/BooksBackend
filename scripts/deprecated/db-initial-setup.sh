#!/bin/bash

echo "Enter mysql password for root user"
mysql -u root -p < './scripts/sqlscripts/init.sql'

