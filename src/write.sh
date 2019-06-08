sudo systemctl stop rfid.service
echo "type the following text \"art.bts\""
python write.py
sleep 1
python read.py
sleep 1
sudo systemctl start rfid.service
echo "data write successfully!"
