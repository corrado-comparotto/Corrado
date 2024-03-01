import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from lmfit.models import PseudoVoigtModel

def gaussian(x, A, mu, sigma):
    return A * np.exp(-(x - mu)**2 / (2 * sigma**2)) # mu = mean, sigma = standard deviation, A = amplitude

def lorentzian(x, A, x0, gamma):
    return A * (gamma / ((x - x0)**2 + gamma**2)) # x0 = peak position, gamma = HWHM, A = amplitude

raw_data = np.loadtxt('XRD_data.ASC', delimiter=' ')
x_all = np.array(raw_data[:,0]) # Full 2Theta range from the measurement
y_all = np.array(raw_data[:,1]) # Full 2Theta range from the measurement 
plt.plot(x_all, y_all, 'b.', label='XRD data') # Print the raw data to ease the selection of the range of interest
plt.xlabel('2$\\theta$')
plt.ylabel('Intensity')
plt.title('XRD Pattern')
plt.xticks(np.arange(np.min(x_all), np.max(x_all), 5))
plt.minorticks_on()
plt.show(block=False)

x_min = input("Input the minimum value for 2Theta (between 10 and 80°): ")
while x_min.replace(".", "").isnumeric() == False or float(x_min) < 10 or float(x_min) > 80:
    x_min = input("Please input a number between 10 and 80°: ")
else:
    x_min = float(x_min)
question = "Input the maximum value for 2Theta (between " + str(x_min) + " and 80°): "
x_max = input(question)
while x_max.replace(".", "").isnumeric() == False or float(x_max) <= x_min or float(x_max) > 80:
    question = "Please input a number between " + str(x_min) + " and 80: "
    x_max = input(question)
else:
    x_max = float(x_max)
plt.close()
x = x_all[np.argmax(x_all > x_min):np.argmax(x_all > x_max)] # Select the 2Theta range of interest
y = y_all[np.argmax(x_all > x_min):np.argmax(x_all > x_max)] # Select the 2Theta range of interest
max = np.max(y)
max_pos = float(x[np.where(y==max)]) # Position of the maximum value within the selected range

# Calculate the FWHM without fitting the raw data with a function, just by linear interpolation
x1_index = (np.argmax(y>max/2))
x0_index = x1_index - 1
x0 = x[x0_index]
x1 = x[x1_index]
y0 = y[x0_index]
y1 = y[x1_index]
x_left = ((max/2)*(x1-x0)/(y1-y0))*(x1-x0) + x0
x2_index = np.max(np.nonzero(y>max/2))
x3_index = x2_index + 1
x2 = x[x2_index]
x3 = x[x3_index]
y2 = y[x2_index]
y3 = y[x3_index]
x_right = ((max/2)*(x3-x2)/(y3-y2))*(x3-x2) + x3
fwhm = x_right-x_left
plt.figure()
plt.plot(x, y, 'b.', label='XRD data') 
plt.axvline(x=x_left, color='g', linestyle='--')
plt.axvline(x=x_right, color='g', linestyle='--')
plt.xlabel('2$\\theta$')
plt.ylabel('Intensity')
label = 'FWHM = ' + np.str_(np.round(fwhm, 2))
plt.scatter([], [], color="w", alpha=0, label=label)
plt.legend()
plt.title('Linear interpolation')
plt.show(block=False)

# Fit with a Gaussian distribution
sigma_guess = fwhm / (2 * np.sqrt(2 * np.log(2)))
popt_g, pcov_g = curve_fit(gaussian, x, y, p0=[max, max_pos, sigma_guess]) # max, max_pos, and sigma_guess are the initial guesses for the fit
A, mu, sigma = popt_g # Extract the optimized parameters
fwhm_g = 2 * np.sqrt(2 * np.log(2)) * sigma
half_max = A / 2
left = mu - fwhm_g / 2
right = mu + fwhm_g / 2
plt.figure()
plt.plot(x, y, 'b.', label='XRD data') 
plt.plot(x, gaussian(x, *popt_g), 'r-', label='Gaussian fit') 
plt.axvline(x=left, color='g', linestyle='--')
plt.axvline(x=right, color='g', linestyle='--')
plt.xlabel('2$\\theta$')
plt.ylabel('Intensity')
label_g = 'FWHM = ' + np.str_(np.round(fwhm_g, 2))
plt.scatter([], [], color="w", alpha=0, label=label_g)
plt.legend()
plt.title('Gaussian fit')
plt.show(block=False)

# Fit with a Lorentzian distribution
popt_l, pcov_l = curve_fit(lorentzian, x, y, p0=[max, max_pos, sigma_guess]) # max, max_pos, and sigma_guess are the initial guesses for the fit
A, x0, gamma = popt_l # Extract the optimized parameters
fwhm_l = 2 * gamma
half_max = A / 2
left = x0 - gamma
right = x0 + gamma
plt.figure()
plt.plot(x, y, 'b.', label='XRD data')
plt.plot(x, lorentzian(x, *popt_l), 'r-', label='Lorentzian fit') 
plt.axvline(x=left, color='g', linestyle='--')
plt.axvline(x=right, color='g', linestyle='--')
plt.xlabel('2$\\theta$')
plt.ylabel('Intensity')
label_l = 'FWHM = ' + np.str_(np.round(fwhm_l, 2))
plt.scatter([], [], color="w", alpha=0, label=label_l)
plt.legend()
plt.title('Lorentzian fit')
plt.show(block=False)

# Fit with a Pseudo-Voigt distribution
model = PseudoVoigtModel()
params = model.make_params(amplitude=max, center=max_pos, sigma=sigma_guess, fraction=0.5)
result = model.fit(y, params, x=x)
centre_PV = result.params['center'].value
fwhm_pv = result.params['fwhm'].value
left = centre_PV - fwhm_pv/2
right = centre_PV + fwhm_pv/2
plt.figure()
plt.plot(x, y, 'b.', label='XRD data')
plt.plot(x, result.best_fit, 'r-', label='Pseudo-Voigt fit')
plt.axvline(x=left, color='g', linestyle='--')
plt.axvline(x=right, color='g', linestyle='--')
plt.xlabel('2$\\theta$')
plt.ylabel('Intensity')
label_pv = 'FWHM = ' + np.str_(np.round(fwhm_pv, 2))
plt.scatter([], [], color="w", alpha=0, label=label_pv)
plt.legend()
plt.title('Pseudo-Voigt fit')
plt.show()