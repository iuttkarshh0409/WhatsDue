#!/bin/bash

# Navigate to the WhatsDue backend directory (handles spaces in path)
cd "/mnt/c/Users/dubey/Desktop/Personal Vault/Projects/WhatsDue/whatsdue-backend" || exit

# Run the reminders Python script with python3
/usr/bin/python3 run_reminders.py
