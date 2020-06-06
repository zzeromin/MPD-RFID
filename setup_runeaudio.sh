sed -i 's/#dtparam=spi=on/dtparam=spi=on/g' /boot/config.txt
pip3 install mfrc522
pip3 install pi-rc522
cp /root/MPD-RFID/src/rfid.service /lib/systemd/system/
sed -i 's/home\/pi/root/g' /lib/systemd/system/rfid.service
systemctl daemon-reload
systemctl start rfid.service
systemctl enable rfid.service
chmod 755 /root/MPD-RFID/src/*.sh
echo "MPD-RFID Setup Complete. Reboot after 3 Seconds."
sleep 3
reboot
