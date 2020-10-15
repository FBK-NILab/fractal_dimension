import sys
import argparse
import csv
import numpy as np
import nibabel as nib
from fractal_dimension import compute_fractal_dimension


if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument('-masks', nargs='?', const=1, default='',
	                    help='Bundle mask(s)')
	parser.add_argument('-box_size_max', nargs='?',  const=1, default='',
	                    help='Maximum box size')                        
	args = parser.parse_args()

	box_size_max = np.asarray(args.box_size_max, dtype='float64')
	box_size = np.arange(1, box_size_max) 

	#Write results on a file
	results = 'csv/output_FiberStats.csv'
	metrics = ['FD']
	first_row = ['bundle_mask_name']
	first_row[1:len(metrics)] = metrics
	with open(results, 'a') as csvFile:
		writer = csv.writer(csvFile)
		writer.writerow(first_row)

	with open('mask_name_list.txt') as f:
		mask_name_list = f.read().splitlines()

	results_matrix = np.zeros((len(mask_name_list), len(metrics)))
	
	for t, mask_name in enumerate(mask_name_list):
		fname = '%s/%s' %(args.masks, mask_name)
		vol_mask = nib.load(fname).get_data()
		fractal_dimension, box_size, counts = compute_fractal_dimension(vol_mask,
                                                                    n_steps=None,
                                                                    box_size_max=None,
                                                                    box_size=box_size,
                                                                    verbose=False)
		print("Fractal dimension of %s = %s" %(mask_name, fractal_dimension))
		results_matrix[t] = [fractal_dimension] 
		row = [mask_name]
		row[1:len(metrics)] = np.float16(results_matrix[t])
		with open(results, 'a') as csvFile:
			writer = csv.writer(csvFile)
			writer.writerow(row)

	sys.exit()    
