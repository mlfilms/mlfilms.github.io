# Enhancing Simulation Data for use in Machine Learning
## By Eric Minor


Although we are able to generate perfectly annotated simulation data, the simulation data doesn't necessarily represent the data we see in actual experiments. This causes issues when trying to train a darkflow model on the simulation data to detect defects in the experimental data. The model will not learn to deal with issues such as noise, low contrast, brightness changes, and blurring from the perfect images the simulation outputs. Thus, we need to process the simulation images to add in the various imperfections present in experimental data. The experimental images will also need to be processed to standardize the their appearance to a certain degree

## Image Data Standardization
The brightness and contrast of the experimental images can vary based on factors such as the illumination and film thickness. In order to make the image data look as similar as possible between runs, we standardize the mean and variances of the images. This is done by subtracting the mean pixel intensity of the image from each pixel, and then dividing that quantity by six times the standard deviation of the pixel intensity values. Adding 0.5 yields  pixel intensity values centered around 0.5. In equation form, 
$$ px = \frac{px - mean(I)}{6*std(I)}+0.5$$

A similar standardization is applied to the simulation data, to give the simulation and experimental data similar dynamic ranges. However, the simulation has the offset (mean) and standard devation slightly randomized in order to help the model learn to identify defects in a wider range of experimental data.

## Blurring and Lighting

