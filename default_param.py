# -*- coding: utf8 -*-
{
# Image
'N_X' : 256, # size of images
'N_Y' : 256, # size of images
'do_whitening'  : True, # = self.pe.do_whitening
'do_mask'  : True, # self.pe.do_mask
'seed': None, # a seed for the Random Number Generator (RNG) for picking images in databases, set to None or a given number to freeze the RNG
# Log-Gabor
#'base_levels' : 2.,
'base_levels' : 1.618,
'n_theta' : 24, # number of (unoriented) angles between 0. radians (included) and np.pi radians (excluded)
'B_sf' : 1.5, # 1.5 in Geisler
'B_theta' : 3.14159/8.,
'figpath' : 'figures/',
'edgefigpath' : 'figures/edges/',
'matpath' : 'mat/',
'edgematpath' : 'mat/edges/',
'datapath' : 'database/',
'ext' : '.pdf',
# EdgeFactory PARAMETERS
'd_width' : 45., # Geisler 1.23 deg (full image = 45deg)
'd_min' : .25, # Geisler 1.23 deg (full image = 45deg)
'd_max' : 2., # Geisler 1.23 deg (full image = 45deg)
'N_r' : 6, #
'N_Dtheta' : 24, # equal to n_theta : 24 to avoid artifacts
'N_phi' : 12, #
'N_scale' : 5, #
'loglevel_max': 7,
'N_image' : None, #use all images in the folder 200, #None
'noise' : 0.5, #
}
