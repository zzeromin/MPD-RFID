sudo systemctl stop rfid.service
echo "type the following text \"art.bts\""
python3 /home/pi/MPD-RFID/src/write.py
sleep 1
python3 /home/pi/MPD-RFID/src/read.py
sleep 1
sudo systemctl start rfid.service
echo "data write successfully!"
