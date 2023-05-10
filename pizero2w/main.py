#!/usr/bin/env python3

import gpiozero as gz

cpu_temp = gz.CPUTemperature().temperature
cpu_temp = round(cpu_temp, 1)
print(cpu_temp)

