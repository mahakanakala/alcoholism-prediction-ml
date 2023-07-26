
# Alcholism Prediction Using Machine Learning

## Overview
This research investigates the application of machine learning algorithms on a 3D array dataset to predict alcoholism in mice, integrating the benefits of machine learning as a powerful and analytical tool for data analysis. In the realm of biomedical engineering, where time plays a crucial role, this study highlights the importance of temporal information in alcoholism research. Leveraging Python-based techniques, the project aims to identify patterns within the 3D array data that can be interpreted by both computer languages and human operators, contributing to improved understanding and early detection of alcoholism-related behaviors in mice for medical and research applications.

## Project Structure
- `data/`: Directory containing the dataset(s).
- `model.ipynb`: Jupyter notebooks for various stages of the project.
- `README.md`: Project overview and instructions (this file).
- `requirements.txt`: Required Python packages and their versions.
- `.gitignore`: Specifies files and directories to ignore in version control.

### 3-D Array Dimensions
3-D array is difficult to visualze in a 2-D space, but it is represented as such:

| Sample Number | Time Step 1 | Time Step 2 | Time Step 3 | Features |
|--------------:|------------:|------------:|------------:|---------:|
| 1             | [0.1, 0.15] | [0.2, 0.25] | [0.3, 0.35] | 2        |
| 2             | [0.3, 0.35] | [0.4, 0.45] | [0.5, 0.55] | 2        |
| 3             | [0.5, 0.55] | [0.6, 0.65] | [0.7, 0.75] | 2        |
| 4             | [0.7, 0.75] | [0.8, 0.85] | [0.9, 0.95] | 2        |
| 5             | [0.9, 0.95] | [1.0, 1.5 ] | [1.2, 1.3 ] | 2        |

**Sample Number**: number of trials or samples in the experiment.

**Time step**: each consecutive time intereval that sample was measured at.

**Features**: number of individual measurable properties or attributes at each time step.
