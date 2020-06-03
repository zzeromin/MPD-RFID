sudo systemctl stop rfid.service
echo "Take your RFID card to the reader"
python3 read.py
sleep 1
sudo systemctl start rfid.service
echo "data write successfully!"
