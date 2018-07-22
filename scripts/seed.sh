#!/bin/bash

# script for seeding data to tables

echo "Enter mysql password for root user"
mysql -u root -p < ./scripts/sqlscripts/load_data.sql

