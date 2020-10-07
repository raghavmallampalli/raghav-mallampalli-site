#!/bin/bash
if ! command -v convert &> /dev/null
then
	echo "ImageMagick could not be found. Install and run script"
	exit
fi
echo "Converting $1.png to 16x16, 48x48 size and generating $1.ico file."
convert $1.png -resize 16x16 $1-16.png
convert $1.png -resize 32x32 $1-32.png
convert $1.png -resize 48x48 $1-48.png
convert $1.png -resize 196x196 $1-196.png

convert $1-16.png $1-32.png $1-48.png $1.ico
rm $1-32.png
