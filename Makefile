# USELESS
first:
	echo 'Please read the README.md'

# Run the script and the dashboard
run:
	cd vaccination_ue_analysis && ipython vaccination_charts_generator.ipynb && cd -
	cd pollution_analysis && ipython pollution_charts_generator.ipynb && cd -
	cd dashboard && ipython dashboard.ipynb 
