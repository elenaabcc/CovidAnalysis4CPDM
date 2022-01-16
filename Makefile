# USELESS
first:
	echo 'Please read the README.md'

# Convert notebook to python
convert: 
	jupyter nbconvert --execute charts_generator.ipynb --to script

# Run the script and the dashboard
run:
	ipython charts_generator.py
	ipython dashboard.ipynb
