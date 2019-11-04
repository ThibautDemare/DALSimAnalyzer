# First, we tell to gnuplot what it the output
# Here, it is a SVG file called "outfile", with a "times new roman" font
set terminal png size 1920,1080 enhanced font 'Times New Roman, 24' butt
set output outfile

# We define where to place the legend
set key outside bottom center

# Put a title to the x-axis
set xlabel xlab

set xrange [0:]
set yrange [0:]

# And a title to the y-axis
set ylabel ylab

# And the main title
set title mainTitle

# Tell gnuplot that CSV files use ";" as a separator
set datafile separator ";"

# ignore first line of data file (data of step 0 is not interesting since the simulation is not initialized at this point)
set key autotitle columnhead

# We check if we have defined colors in the arguments
if(!exists("color1")) {
	color1 = "#228B22"
}
if(!exists("color2")) {
	color2 = "#FF8C00"
}
if(!exists("color3")) {
	color3 = "#003B6F"
}
if(!exists("color4")) {
	color4 = "#CC0000"
}

# Eventually we plot the four curves
if (exists("curve4Label")) {
	plot  dataFile using 1:2 title curve1Label with linespoints lw 2 pi -100 pt 13 ps 1 lc rgb color1,\
	      dataFile using 1:3 title curve2Label with linespoints lw 2 pi -100 pt 9 ps 1 lc rgb color2,\
	      dataFile using 1:4 title curve3Label with linespoints lw 2 pi -100 pt 11 ps 1 lc rgb color3,\
	      dataFile using 1:5 title curve4Label with linespoints lw 2 pi -100 pt 7 ps 1 lc rgb color4
} else {
	if(exists("curve3Label")) {
		plot  dataFile using 1:2 title curve1Label with linespoints lw 2 pi -100 pt 13 ps 1 lc rgb color1,\
		      dataFile using 1:3 title curve2Label with linespoints lw 2 pi -100 pt 9 ps 1 lc rgb color2,\
		      dataFile using 1:4 title curve3Label with linespoints lw 2 pi -100 pt 11 ps 1 lc rgb color3
	} else {
		if(exists("curve2Label")) {
			plot  dataFile using 1:2 title curve1Label with linespoints lw 2 pi -100 pt 13 ps 1 lc rgb color1,\
			      dataFile using 1:3 title curve2Label with linespoints lw 2 pi -100 pt 9 ps 1 lc rgb color2
		} else {
			plot  dataFile using 1:2 title curve1Label with linespoints lw 2 pi -100 pt 13 ps 1 lc rgb color1
		}
	}
}
