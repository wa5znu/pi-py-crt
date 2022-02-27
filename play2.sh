#!/bin/sh

(
  sleep 30
  echo "$0: Pi Py CRT"; \
  echo "Python code for BBP Pi from"; \
  echo "https://www.literateprograms.org/pi_with_the_bbp_formula__python_.html"; \
  echo ""; \
  echo ""; \
  echo ""; \
  sysvbanner "Pi Py CRT        "; \
  sysvbanner "by WA5ZNU           "; \
  echo ""; \
  cd Documents/src/pi-py-crt; \
  ./sequential_pi.py 
) | sudo tee /dev/console > /dev/null &

