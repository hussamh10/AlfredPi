cpu=$(</sys/class/thermal/thermal_zone0/temp)
echo "$(date) @ $(hostname)"
echo "-------------------------------------------"
echo "GPU $(/opt/vc/bin/vcgencmd measure_temp)"
echo "CPU temp=$((cpu/1000))'C"
