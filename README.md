# fractal_dimension

<!-- brainlife-app:begin (generated from the App manifest; edit the manifest, not this block) -->

> **Computes the box-counting fractal dimension of each bundle mask in a tract-mask collection and outputs the values as a CSV table.**

For every NIfTI mask in the collection, counts the boxes needed to cover the mask at box sizes from 1 up to box_size_max and fits the log-log slope to get the fractal dimension, a measure of the irregularity of the bundle shape. Use it to compare the shape complexity of white matter bundles across subjects or methods.

| | |
|---|---|
| 📥 **Inputs** | `neuro/tractmasks` |
| 📤 **Outputs** | `neuro/tractmeasures` |
| 🐳 **Container** | `brainlife/dipy:0.16.0` |
| ⚙️ **Resources** | 4 CPUs · 0.08 h walltime |
| 🔗 **Run it** | [doi.org/10.25663/brainlife.app.442](https://doi.org/10.25663/brainlife.app.442) |

#### 📥 Inputs

| Input | Datatype | Required | Description |
|---|---|---|---|
| `0` | `neuro/tractmasks` | yes | Collection of bundle masks of which to compute the Fractal Dimension |

#### 📤 Outputs

| Output | Datatype | Description |
|---|---|---|
| `csv` | `neuro/tractmeasures` | csv file with the Fractal Dimension of each bundle mask of the collection |

<details>
<summary><b>⚙️ Parameters</b> (1)</summary>

| Parameter | Type | Default | Description |
|---|---|---|---|
| `box_size_max` | number | `7.5` | Maximum size of the box used by the box-counting method |

</details>

📚 **References used by this App:**
- Berto G, et al. Classifyber, a robust streamline-based linear classifier for white matter bundle segmentation. NeuroImage (2020). [doi:10.1016/j.neuroimage.2020.117402](https://doi.org/10.1016/j.neuroimage.2020.117402)

<!-- brainlife-app:end -->

Investigation on the fractal dimension of segmented white matter bundles.
