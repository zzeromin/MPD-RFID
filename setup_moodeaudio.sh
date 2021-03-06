pip install --upgrade pip
echo "dtparam=spi=on" >> /boot/config.txt
pip3 install mfrc522
pip3 install pi-rc522
cp /home/pi/MPD-RFID/src/rfid.service /lib/systemd/system/
systemctl daemon-reload
systemctl start rfid.service
systemctl enable rfid.service
chmod 755 /home/pi/MPD-RFID/src/*.sh
echo "MPD-RFID Setup Complete. Reboot after 3 Seconds."
sleep 3
reboot
