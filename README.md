[![Abcdspec-compliant](https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg)](https://github.com/brain-life/abcd-spec)
[![Run on Brainlife.io](https://img.shields.io/badge/Brainlife-bl.app.442-blue.svg)](https://doi.org/10.25663/brainlife.app.442)

# app-fractal-dimension
This App was designed to compute the Fractal Dimension (FD) of bundle masks. In general, the concept of fractal dimension (Mandelbrot et al., 1982) can be used to quantify the degree of irregularity of a 3D shape. This notion has already been applied to the shape of the brain white matter 
(Zhang et al., 2006) and to characterize multiple sclerosis (Esteban et al., 2007). The FD of a bundle mask can be computed via the box-counting dimension (Falconer et al., 2014). The box-counting dimension is based on the idea of covering a given shape with boxes of size σ and it quantifies how the number of boxes changes when σ changes, in double-log scale:

<img src="https://latex.codecogs.com/gif.latex?\text{FD}_{\text{box}}&space;=&space;-&space;\lim_{\sigma&space;\rightarrow&space;0}\frac{\log&space;\text{count}(\sigma)}{\log&space;\sigma}" title="\text{FD}_{\text{box}} = - \lim_{\sigma \rightarrow 0}\frac{\log \text{count}(\sigma)}{\log \sigma}" />

where count(σ) is the number of the necessary boxes. 

### Authors
- [Emanuele Olivetti](olivetti@fbk.eu)

### Funding Acknowledgement
brainlife.io is publicly funded and for the sustainability of the project it is helpful to Acknowledge the use of the platform. We kindly ask that you acknowledge the funding below in your publications and code reusing this code.

[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-1636893](https://img.shields.io/badge/NSF_BCS-1636893-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-ACI-1916518](https://img.shields.io/badge/NSF_ACI-1916518-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1916518)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NIH-NIBIB-R01EB029272](https://img.shields.io/badge/NIH_NIBIB-R01EB029272-green.svg)](https://grantome.com/grant/NIH/R01-EB029272-01)

### Reference
- [Fractal Dimension](https://en.wikipedia.org/wiki/Fractal_dimension)
- [Box-counting dimension](https://en.wikipedia.org/wiki/Minkowski-Bouligand_dimension)

### Citations
We kindly ask that you cite the following articles when publishing papers and code using this code. 

1. ["Classifyber, a robust streamline-based linear classifier for white matter bundle segmentation"](https://doi.org/10.1016/j.neuroimage.2020.117402), Bertò, G., Bullock, D., Astolfi, P., Hayashi, S., Zigiotto, L., Annicchiarico, L., Corsini, F., De Benedictis, A., Sarubbo, S., Pestilli, F., Avesani, P., Olivetti, E. NeuroImage (2020).

2. Mandelbrot, B. B., 1982. The fractal geometry of nature. W.H. Freeman, San Francisco. https://doi.org/10.1002/esp.3290080415

3. Falconer, K. J., 2014. Fractal geometry: mathematical foundations and applications, third edition Edition. John Wiley & Sons Inc, Hoboken.

4. Avesani, P., McPherson, B., Hayashi, S. et al. The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services. Sci Data 6, 69 (2019). [https://doi.org/10.1038/s41597-019-0073-y](https://doi.org/10.1038/s41597-019-0073-y)

### Running the App
### On [Brainlife.io](http://brainlife.io/) 
You can submit this App online at https://doi.org/10.25663/brainlife.app.442 via the “Execute” tab.

Inputs: \
The input is a collection of bundle masks (.nii.gz format).

Output: \
The App returns the FD of all the bundle masks given in input.

### Running Locally (on your machine)

1. git clone this repo.
2. Inside the cloned directory, create `config.json` with something like the following content with paths to your input files.

```json
{
        "masks": "./input/masks"
}
```

3. Launch the App by executing `main`

```bash
./main
```

### Output
The main output of this App is a file called `output_FiberStats.csv`, in which is reported the FD of all the bundle masks of the collection.

### Dependencies
This App only requires [singularity](https://sylabs.io/singularity/) to run. 

#### MIT Copyright (c) 2019 Emanuele Olivetti
