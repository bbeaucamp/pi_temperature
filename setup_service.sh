#!/bin/bash
# Copy the service and timer files to systemd
sudo cp pi_temperature.service /etc/systemd/system
sudo cp pi_temperature.timer /etc/systemd/system

# Start the timer NOW
sudo systemctl enable --now pi_temperature.timer
