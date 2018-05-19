# Change-Mac-Linux
This is a command line tool in **python** to change mac address of any network interface in **linux only**
  
## Requirements
```macchanger``` tool

Debian install: ```sudo apt-get install macchanger```

Arch install: ```sudo pacman -S macchanger```

## Usage : 
```python changemac.py -i <interface> -m <mode>```

## Modes:
  1. Random > Sets mac address to a random value
  1. Show > Displays current mac address
  1. Old > Sets to original mac address
