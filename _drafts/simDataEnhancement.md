# Enhancing Simulation Data for use in Machine Learning
## By Eric Minor


Although we are able to generate perfectly annotated simulation data, the simulation data doesn't necessarily represent the data we see in actual experiments. This causes issues when trying to train a darkflow model on the simulation data to detect defects in the experimental data. The model will not learn to deal with issues such as noise, low contrast, brightness changes, and blurring from the perfect images the simulation outputs. Thus, we need to process the simulation images to add in the various imperfections present in experimental data. The experimental images will also need to be processed to standardize the their appearance to a certain degree

## Image Data Standardization
The brightness and contrast of the experimental images can vary based on factors such as the illumination and film thickness. In order to make the image data look as similar as possible between runs, we standardize the mean and variances of the images. This is done by subtracting the mean pixel intensity of the image from each pixel, and then dividing that quantity by six times the standard deviation of the pixel intensity values. Adding 0.5 yields  pixel intensity values centered around 0.5. In equation form, 

$$ px = \frac{px - mean(I)}{6*std(I)}+0.5$$

This standardization ensures a similar dynamic range and brightness regardless of the specific lighting in an experiment. A similar standardization is applied to the simulation data, to give the simulation and experimental data similar dynamic ranges. However, the simulation has the offset (mean) and standard devation slightly randomized in order to help the model learn to identify defects in a wider contrast  range.

## Accounting For Traditional Experimental Noise
Although it is important to make the experimental data as consistent as possible, it is equally important to make the training data as inconsistent as possible. If you train the model only with images containing distinct intensity levels and gradients, the model will learn to rely on those specifc patterns to identify defects. Instead, we wish to make the model as robust as possible by training it on images with a variety of different lighting levels, contrasts, and visual artifacts in order to force the model to recognize the more abstract pattern of a defect. This will result in a model that is able to identify a wider variety of defects in a much larger set of experimental conditions.

To this end, we add several abberations to the simulated data.

Gaussian blurring is a simple filter designed to lower the sharpness of an image. When a gaussian filter is applied, each pixel in an image has its value changed to a weighted mean of the pixels around it. Simulated defect images are very sharp as there is very little inaccuracy when generating the images. However, in experimental images there are several factors that can result in reduced sharpness. Simple camera inaccuracies are always a factor along with microscopes being slightly out of focus. Light can also be slightly distorted when passing through lenses or being reflected off a surface. The end result is that a machine learning model needs to be trained to identify objects in a variety of blurriness levels, which is why we appl a  gaussian filter with a randomized sigma parameter to the simulated images.

Although we attempt to standardize our experimental images based on the mean and standard deviation of the image data, the amount of light and dark regions can slightly skew the standardization process, leading to bright regions sometimes being slightly brighter or dimmer than intended. The presence of especially bright regions (which we call islands in our data) can significantly skew the standard deviation of the images, washing out the contrast in defect patterns. Thus, the model needs to recognize defects regardless of the particular contrast or brightness levels in an image. To this end, we randomize the standardization process for simulation images. Instead of giving the images a set mean of 0.5 and a dynamic range of 6 standard deviations, the images have their dynamic range and mean set randomly, allowing the model to adapt to a wider range of images.

When performing photomicroscopy, you often get the boundaries of the microscope apperature in the images, which appear as a sharp transition to dark. Furthermore, older cameras will have distinct brightness shifts partway through the image. These can be caused due to manufacturing inaccuracies or sensor degradation over time. Early version of the machine learning model would place detections along these boundaries, as it associated  areas of quick shifts from light to dark as defects. To help the model learn to ignore such boundaries, similar shifts were added to the simulation images. Each simulation image was broken into four randomized quadrants, with each quadrant having its brighness randomly increased or decreased. After training on this new simulated data, the model successfully learned not to recognize random boundaries as defects.

## Smart Noise
Many cameras also have low levels of period noise. Description of smart noise.



These extracted patterns were then applied to the simulated images. The strength and skew of the applied pattern was chosen randomly for each image in order for the trained model to be as versatile as possible.









