#!/bin/bash
# OpenGraph (ize) image: Resize (crop or extent) an image such that it has an optimal ratio and  size (1.91:1, 764 x 400) ftruor facebook shares and twitter cards
# Requires ImageMagick
# Installation: 
#   1 Save this file somewhere in your ${PATH}
#   2 Make executable (chmod u+x ogizeImage.sh)
# Usage from a commandline:
# ogizeImage Picture.png
# This will result in a resized image "Picture_og.png" in the current directory



grav='Center'
task="crop"

 help_ogizeImage()
 {
   echo "OpenGraph (ize) image: Resize (crop or extent) an image such that it has an optimal"
   echo "ratio and  size (1.91:1, 764 x 400) for facebook shares and twitter cards." 
   echo "Usage: $0 [OPTIONS] [FILE]"
   echo "Where OPTIONS are one or more of:"
   echo "-g GRAVITYPOS: crop/extent relative to the gravity center can be North, South, West, East, or Center(default)"
   echo "-x: extent image to match the aspect ratio by adding transparent space"
   echo "-c: crop the image to match the aspect ratio (default)"
   exit 1
 }
 #
 #Start main procedure
 #
 #
 #Set default value for variable

 
#process comand line arguments
while getopts cxg: opt
do	case "$opt" in
	g) grav=$OPTARG;;
	x) task="extent";;
        c) task="crop";;	
	[?]) help_ogizeImage;;
	esac
done

#get filename
shift `echo $OPTIND | awk '{print $1-1}'`


file1=$1


fin=$1
fout=`basename $fin | sed -r -e 's/\.\w+$/_og\0/'`

if  [ "$task" == "extent" ]; then

extent=`identify $fin | awk '{\
    split($3,dim,"x");\
    if(dim[1] > 2*dim[2]){\
        printf "0x%d\n",(dim[1]/1.91)\
    }else{\
        printf "%dx0\n",(dim[2]*1.91)}\
    }'`
    
else

extent=`identify $fin | awk '{\
    split($3,dim,"x");\
    if(dim[1] > 2*dim[2]){\
        printf "%dx0\n",(dim[2]*1.91)\
    }else{\
        printf "0x%d\n",(dim[1]/1.91)}\
    }'`    

fi

convert $fin -background transparent -gravity ${grav} -extent $extent -resize 764x400 $fout


