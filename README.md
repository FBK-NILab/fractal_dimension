<h1 align="center">Fractal Dimension (FD) of bundle masks</h1>

<p align="center">
  Computes the box-counting fractal dimension of each bundle mask in a tract-mask collection and outputs the values as a CSV table.
</p>

<p align="center">
  <a href="https://github.com/brainlife/abcd-spec"><img src="https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg" alt="ABCD Spec v1.1"></a>
  <a href="https://doi.org/10.25663/brainlife.app.442"><img src="https://img.shields.io/badge/Brainlife-brainlife.app.442-blue.svg" alt="Run on brainlife.io"></a>
</p>

## At a glance

<!-- brainlife-app:begin (generated from the App manifest; edit the manifest, not this block) -->

> **Computes the box-counting fractal dimension of each bundle mask in a tract-mask collection and outputs the values as a CSV table.**

For every NIfTI mask in the collection, counts the boxes needed to cover the mask at box sizes from 1 up to box_size_max and fits the log-log slope to get the fractal dimension, a measure of the irregularity of the bundle shape. Use it to compare the shape complexity of white matter bundles across subjects or methods.

| | |
|---|---|
| **Inputs** | `neuro/tractmasks` |
| **Outputs** | `neuro/tractmeasures` |
| **Container** | `brainlife/dipy:0.16.0` |
| **Resources** | 4 CPUs · 0.08 h walltime |
| **Run it** | [doi.org/10.25663/brainlife.app.442](https://doi.org/10.25663/brainlife.app.442) |

#### Inputs

| Input | Datatype | Required | Description |
|---|---|---|---|
| `0` | `neuro/tractmasks` | yes | Collection of bundle masks of which to compute the Fractal Dimension |

#### Outputs

| Output | Datatype | Description |
|---|---|---|
| `csv` | `neuro/tractmeasures` | csv file with the Fractal Dimension of each bundle mask of the collection |

<details>
<summary><b>Parameters</b> (1)</summary>

| Parameter | Type | Default | Description |
|---|---|---|---|
| `box_size_max` | number | `7.5` | Maximum size of the box used by the box-counting method |

</details>

<!-- brainlife-app:end -->

## Running the App

### On brainlife.io

Open the App at [doi.org/10.25663/brainlife.app.442](https://doi.org/10.25663/brainlife.app.442), choose `neuro/tractmasks` from your project, set the parameters and press **Execute**. The results are saved to your project as `neuro/tractmeasures`.

### Locally

You need [Singularity/Apptainer](https://apptainer.org/) (the App runs in `brainlife/dipy:0.16.0`), [`jq`](https://jqlang.github.io/jq/).

1. Clone this repository.
2. Create `config.json` with the paths to your inputs and the parameters:

   ```json
   {
       "masks": "/path/to/0/masks",
       "box_size_max": 7.5
   }
   ```

3. Run `./main`.

## Troubleshooting

- **Computation failed.**: Check that the input contains NIfTI bundle masks.

## Citing

If you use this App, please cite it, the software it builds on and brainlife.io:

- Fractal Dimension (FD) of bundle masks. brainlife.io App. [doi:10.25663/brainlife.app.442](https://doi.org/10.25663/brainlife.app.442)
- Berto G, et al. Classifyber, a robust streamline-based linear classifier for white matter bundle segmentation. NeuroImage (2020). [doi:10.1016/j.neuroimage.2020.117402](https://doi.org/10.1016/j.neuroimage.2020.117402)
- Garyfallidis et al. Dipy, a library for the analysis of diffusion MRI data. *Frontiers in Neuroinformatics* 8 (2014). [doi:10.3389/fninf.2014.00008](https://doi.org/10.3389/fninf.2014.00008)
- Hayashi S, Caron BA, Heinsfeld AS, et al. brainlife.io: a decentralized and open-source cloud platform to support neuroscience research. *Nature Methods* 21:809–813 (2024). [doi:10.1038/s41592-024-02237-2](https://doi.org/10.1038/s41592-024-02237-2)
- Avesani P, McPherson B, Hayashi S, et al. The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services. *Scientific Data* 6:69 (2019). [doi:10.1038/s41597-019-0073-y](https://doi.org/10.1038/s41597-019-0073-y)

## Authors

Maintained by [@FBK-NILab](https://github.com/FBK-NILab).
