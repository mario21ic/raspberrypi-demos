#!/bin/bash

sudo vcgencmd measure_temp | egrep -o '[0-9]*\.[0-9]*'

