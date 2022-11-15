# snake-servo-pi
Control snake-like servo motors movement with Raspberry Pi

## How to run

```sh
# Install required packages
sudo apt update
sudo apt upgrade
sudo apt install python3-pip python3-dev gcc git

git clone https://github.com/bioerrorlog/snake-servo-pi.git
cd snake-servo-pi
sudo pip install -r requirements.txt

# Run script
sudo python3 servo_gpio/main.py
# You need to run as root to avoid the error:
# RuntimeError: No access to /dev/mem. Try running as root!
```
