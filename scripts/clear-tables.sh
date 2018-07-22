#!/bin/bash

# script for clearing all tables

mysql -u root -p < ./scripts/sqlscripts/clear_tables.sql
