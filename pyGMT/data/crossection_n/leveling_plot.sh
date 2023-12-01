#!/bin/csh -f

rm gmt.history gmt.conf

set out = crossection

gmt gmtset MAP_FRAME_PEN = 2p
gmt gmtset MAP_TICK_PEN_PRIMARY = 2p
gmt gmtset FONT_ANNOT_PRIMARY = 12p,1,black
gmt gmtset FONT_LABEL = 12p,1,black
gmt gmtset FONT_TITLE = 14p,1,black
gmt gmtset MAP_FRAME_WIDTH = 1p
gmt gmtset MAP_TITLE_OFFSET = 3p
gmt gmtset PS_MEDIA A1

gmt psbasemap -R-60/70/-36/0 -JX24/5 -Bx25+l"Distance(km)" -By10+l"Depth (km)" -BeSnW+t"Fault Geometries" -V -K > $out.ps
gmt psxy crossection.txt -R -J -W1p,67/52/27 -K -O -V >> $out.ps

gmt psxy -R -J -L -W1p,black -O -V -K << ! >> $out.ps
-130 0
90 0
!

gmt psxy -R -J -L -W2p,177/150/147 -O -V -K << ! >> $out.ps
-130 -30
90 -30
!

gmt pstext -R -J -F+f+a+j -O -V -K << ! >> $out.ps
-57 -27 12,1,black 0 ML Elastic Crust
-57 -33 12,1,black 0 ML Inviscid  Mantle
!


gmt psbasemap -R-60/70/-24/24 -JX24/4  -Bx25+l"Distance(km)" -By10+l"Rate(mm)" -BWSne+t"Long-term Vertical" -V -Y2.8i -O -K >> $out.ps
awk '{print $1,$2}' prediction.txt | gmt psxy -R -JX -W1p,red -Fcf -P -V -K -A -O >> $out.ps
awk '{print $10,$6,$9}' lt.txt | gmt psxy -R -JX -W1p,blue -Ey0.3c/0.3,blue -Fcf -P -V -K -A -O >> $out.ps
awk '{print $10,$6}' lt.txt | gmt psxy -R -JX -Sc0.1 -Gblue -P -V -K -A -O >> $out.ps

gmt pstext -R -J -F+f+a+j -O -V -K << ! >> $out.ps
-50 -20 10,1,black 0 ML Model Prediction
-50 -16 10,1,black 0 ML Data
!

gmt psxy -R -J -L -W1p,red -O -V -K << ! >> $out.ps
-58 -20
-52 -20
!

echo -55 -16 | gmt psxy -R -JX -Sc0.1 -Gblue -P -V -K -A -O >> $out.ps

gmt psbasemap -R-60/70/-24/24 -JX24/4  -Bx25+l"Distance(km)" -By10+l"Rate(mm)" -BWSne+t"Short term Vertical" -V -Y2.5i -O -K >> $out.ps
awk '{print $1,$3}' prediction.txt | gmt psxy -R -JX -W1p,red -Fcf -P -V -K -A -O >> $out.ps
awk '{print $10,$6,$9}' st.txt | gmt psxy -R -JX -W1p,blue -Ey0.3c/0.3,blue -Fcf -P -V -K -A -O >> $out.ps
awk '{print $10,$6}' st.txt | gmt psxy -R -JX -Sc0.1 -Gblue -P -V -K -A -O >> $out.ps


gmt psbasemap -R-60/70/-80/20 -JX24/4  -Bx25+l"Distance(km)" -By20+l"Rate(mm)" -BWSne+t"Short term East" -V -Y2.5i -O -K >> $out.ps
awk '{print $1,$4-13}' prediction.txt | gmt psxy -R -JX -W1p,red -Fcf -P -V -K -A -O >> $out.ps
awk '{print $10,$4,$7}' st.txt | gmt psxy -R -JX -W1p,blue -Ey0.3c/0.3,blue -Fcf -P -V -K -A -O >> $out.ps
awk '{print $10,$4}' st.txt | gmt psxy -R -JX -Sc0.1 -Gblue -P -V -K -A -O >> $out.ps

gmt psbasemap -R-60/70/-20/60 -JX24/4  -Bx25+l"Distance(km)" -By20+l"Rate(mm)" -BWSne+t"Short term North" -V -Y2.5i -O -K >> $out.ps
awk '{print $1,$5+10}' prediction.txt | gmt psxy -R -JX -W1p,red -Fcf -P -V -K -A -O >> $out.ps
awk '{print $10,$5,$8}' st.txt | gmt psxy -R -JX -W1p,blue -Ey0.3c/0.3,blue -Fcf -P -V -K -A -O >> $out.ps
awk '{print $10,$5}' st.txt | gmt psxy -R -JX -Sc0.1 -Gblue -P -V -K -A -O >> $out.ps


gmt pstext -R -J -F+f+a+j -O -V<< ! >> $out.ps
#300 -35 10,1,black 0 LM Leveling
#300 -39 10,1,black 0 LM PSI with standard deviation in 500m
!

##### convert to jpg
gmt psconvert $out.ps -E600 -A0.5c -P -Tj

