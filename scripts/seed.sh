#!/bin/bash

# script for seeding data to tables

echo "Enter mysql password for root user"
mysql < ./scripts/sqlscripts/load_data.sql

