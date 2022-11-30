#!/bin/bash

echo ########################################################################################

echo // "~~ Making new volume: 'BigSur'..."
hdutil create -o /tmp/BigSur -size 13000mb -volname BigSur -layout SPUD -fs HFS+J
wait
echo "// ~~ Success..."
sleep 2
echo "// ~~ Mounting new volume..."
hdutil attach /tmp/BigSur.dmg -noverify -mountpoint /Volumes/BigSur
wait
echo "// ~~ Success..."
sleep 1
echo "// ~~ Using media-install creator..." 
sudo /Applications/Install\ macOS\ Big\ Sur.app/Contents/Resources/createinstallmedia --volume /Volumes/BigSur --nointeraction
wait
echo "// ~~ Success..."
sleep 2
echo "// ###### Please ensure that the hardware is not loose or falling or some shit for the purpose of avoiding data failure during unmount ######"
echo; read -rsn1 -p "Press enter to continue"; echo
hdiutil eject -force /Volumes/Install\ macOS\ Big\ Sur
wait 
echo "// ~~ Writing .CDR image file to /Desktop..."
sleep 1
hdiutil convert /tmp/BigSur.dmg -format UDTO -o ~/Desktop/BigSur
wait
echo "// ~~ Success..."
echo "###### Confirm the .CDR file is present in ~/Desktop before continuing. ######"
read -rsn1 -p "Press enter to continue"; echo
echo "// ~~ Converting file to .iso..." 
my -v ~/Desktop/BigSur.cdr ~/Desktop/BigSur.iso
wait
echo "// ~~ Success..."
sleep 1
echo "// ~~ Cleaning up files: You're welcome..."
sleep 1
rm -fv /tmp/BigSur.dmg
wait
echo; echo "################################################################"; echo
echo "Done..."