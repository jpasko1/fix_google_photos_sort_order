## Fix google photos sort order

Google photos orders album photos by date and time of the exif data in images.

This seems limited to single second resolution(11/2020).

Action photos have many bursts of 4-5 frame per second.

Given a directory with a batch of photos in it:
- Process the photos in NAME ORDER(image_001, image_002)
- Take timestamp of first photo, add 1 second to the exif data for each subsequent photo and re-write the exif data.

When complete, upload directory of photos to Google Photos

Written in python 3

### Install python 3 prereqs
```
pip3 install -r requirements.txt
```

### Usage:
```
fix_google_photos_sort_order.py directory_with_pictures_to_fix
```
## Recommendation

Make a backup copy of the directory to re-adjust the timestamps and experiment there.

```
cp -r my_dir_with_photos my_dir_with_photos_see_if_this_works
fix_google_photos_sort_order.py  my_dir_with_photos_see_if_this_works
```

### Todo

Error handling in many forms
