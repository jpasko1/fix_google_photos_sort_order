#!/usr/bin/env python3

# Google photos Fix order script.
# Google photos orders photos by date and time of the exif data in images
# This is limited to second resolution. Game photos have many 4-5 frame per second bursts
# Given a directory with a batch of photos in it. Process the photos in NAME ORDER
# Take timestamp of first photo, add 1 second to the exif data for each subsequent photo

from datetime import datetime, timedelta
import piexif
import os
import sys

indir = sys.argv[1]
if not os.path.isdir(indir):
    print("%s is not a directory" % indir)

pics = os.listdir(indir)
pics.sort()

starttime = None
cnt = 0
for pic in pics:
    pic_fp = os.path.join(indir, pic)
    exif_dict = piexif.load(pic_fp)

    dstmp = exif_dict['Exif'][piexif.ExifIFD.DateTimeOriginal]  # gives bytes() of time string in 2020:10:31 09:59:39 format
    dstmp = dstmp.decode(encoding='UTF-8')                      # decode bytes() to str()
    date_obj = datetime.strptime(dstmp, '%Y:%m:%d %H:%M:%S')    # string to datetime object

    if cnt == 0:
        starttime = date_obj

    new_date = starttime + timedelta(seconds=cnt)
    print("Picture %s ORIG date %s new date %s" % (pic, dstmp, new_date))

    exif_dict['Exif'][piexif.ExifIFD.DateTimeOriginal] = new_date.strftime("%Y:%m:%d %H:%M:%S")

    exif_bytes = piexif.dump(exif_dict)
    piexif.insert(exif_bytes, pic_fp)
    cnt += 1
