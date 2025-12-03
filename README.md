# Cross-Domain Spectral Compatibility and Unsupervised Land-Cover Classification of VIS–NIR UAV Imagery in Colombian Landscapes  
**Spectral domain alignment and unsupervised land-cover analysis using multispectral UAV imagery**

---

This repository contains the full development of a research project focused on evaluating **cross-domain spectral compatibility between VIS–NIR datasets** and implementing **unsupervised land-cover classification** using aerial imagery captured by UAVs.  
The study integrates physical principles of optical sensing, computer vision techniques, and machine learning methods applied to environmental scenarios in Colombia.

---

## Overview

### Objectives
- Evaluate VIS–NIR spectral compatibility across multiple datasets.  
- Measure NIR-band correlations for specific object classes.  
- Develop an unsupervised land-cover classification pipeline.  
- Analyze the impact of domain shift in multispectral UAV imagery.

### Main Contributions
- Cross-domain VIS–NIR spectral correlation matrices.  
- Identification of classes with transferable NIR signatures.  
- Reproducible clustering pipeline for land-cover mapping.  
- Scripts and notebooks generating all figures and metrics presented in the paper.

---

## Key Results

- Significant NIR-band correlations were found between VEDAI and QUEEN-BEE for classes such as *car* and *pickup truck* (ρ ≈ 0.62).  
- The Dubai (Kaggle) dataset achieved the highest unsupervised separability (Silhouette ≈ 0.57).  
- QUEEN-BEE and VEDAI showed moderate separability due to domain shift.  
- Results highlight the potential of NIR bands for class-specific spectral transferability.


---

## Methodology

### Preprocessing
- Radiometric normalization, band alignment, and min–max scaling.  
- Patch extraction with metadata preservation.  

### Cross-Domain Spectral Compatibility
- Pearson/Spearman correlation and mutual information.  
- Class-specific spectral transferability assessment.  
- Visualization through spectral curves and correlation matrices.

### Unsupervised Classification
- Implemented methods: K-Means, GMM, Spectral Clustering.  
- PCA for dimensionality reduction.  
- Pixel-level and patch-level evaluations.

### Evaluation
- Metrics: Silhouette, Davies–Bouldin, Calinski–Harabasz.  
- Cross-dataset comparison to measure cluster stability.  

---

## Datasets

VEDAI – RGB + NIR

QUEEN-BEE – VIS–NIR UAV imagery from Colombia

Dubai Multispectral (Kaggle)

Datasets are not included due to size and license restrictions

## Contact

Author: Juan Ángel Gamez Diaz - Physics Engineer/Data scientist
Email: gamezdiazjuanangel4@gmail.com
