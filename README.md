# Pi temperature

Log the CPU temperature of your Raspberry Pi to a file.
This repo contains a very simple python file to get the temperature of the CPU of your Raspberry Pi and uses a `systemd` service and timer to run this script every 10s.

## Requirements

You need a Raspberry Pi with `sudo` privileges.

## How to use this project

1. Clone this project in `/home/pi` (or change the locations in `pi_temperature.service`):

```bash
cd /home/pi
git clone https://github.com/bbeaucamp/pi_temperature.git
```

2. Enable the timer that will log the temperatures:

```bash
cd /home/pi/pi_temperature
sh setup_service.sh
```

The temperatures are now logged in `/home/pi/temperatures.csv` every 10s. 

You can change the frequency of the temperature readings by changing `OnUnitActiveSec` in `pi_temperature.timer`. Then, re-run `sh setup_service.sh`.

## Useful Commands

- Disable and stop the logging of temperatures:

```bash
sudo systemctl disable --now pi_temperature.timer
```

- Enable and start the logging of temperatures:

```bash
sudo systemctl enable --now pi_temperature.timer
```

- Check the status of the service:

```bash
sudo systemctl status pi_temperature.timer
```

- Watch the latest readings in `temperatures.csv` in real time (CTRL+C to stop):

```bash
tail -f /home/pi/pi_temperature/temperatures.csv
```

- Use the python script without logging to a file. The script will print the temperature to the screen every 2s (useful to monitor the CPU temperature just for a short while):

```bash
python3 temperature.py
```