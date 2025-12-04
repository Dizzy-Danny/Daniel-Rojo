To run this project you will need to have these modules imported:
tkinter
datetime
zoneinfo

I found that on my mac laptop I needed to pip download tzdata to get zoneinfo to properly work.
Seems to work on most computers I've checked.

ZoneInfo from zoneinfo uses the tz database, wikipedia has the list that I used.
If more buttons want to be added, the geometry will need to change.