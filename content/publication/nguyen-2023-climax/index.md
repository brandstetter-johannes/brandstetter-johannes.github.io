---
# Documentation: https://wowchemy.com/docs/managing-content/

title: ClimaX -- A foundation model for weather and climate
subtitle: ''
summary: 'We develop and demonstrate ClimaX, a flexible and generalizable deep learning model for weather and climate science that can be trained using heterogeneous datasets spanning different variables, spatio-temporal coverage, and physical groundings. Published at ICML 2023 (Spotlight).'
authors:
- Tung Nguyen
- Johannes Brandstetter
- Ashish Kapoor
- Jayesh K. Gupta
- Aditya Grover
tags: ['Partial Differential Equations', 'Learn2Simulate', 'Weather&Climate', 'AI4Science', 'Neural Surrogates', 'Microsoft', 'Deep Learning']
categories: ['Learn2Simulate']
date: '2023-01-24'
lastmod: 2023-01-24T09:47:56+01:00
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: 'The ClimaX idea'
  focal_point: 'Center'
  preview_only: true

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
publishDate: '2023-01-24T08:47:56.212636Z'
publication_types:
- '2'
abstract: "Most state-of-the-art approaches for weather and climate modeling are based on physics-informed numerical models of the atmosphere. These approaches aim to model the non-linear dynamics and complex interactions between multiple variables, which are challenging to approximate. Additionally, many such numerical models are computationally intensive, especially when modeling the atmospheric phenomenon at a fine-grained spatial and temporal resolution. Recent data-driven approaches based on machine learning instead aim to directly solve a downstream forecasting or projection task by learning a data-driven functional mapping using deep neural networks. However, these networks are trained using curated and homogeneous climate datasets for specific spatiotemporal tasks, and thus lack the generality of numerical models. We develop and demonstrate ClimaX, a flexible and generalizable deep learning model for weather and climate science that can be trained using heterogeneous datasets spanning different variables, spatio-temporal coverage, and physical groundings. ClimaX extends the Transformer architecture with novel encoding and aggregation blocks that allow effective use of available compute while maintaining general utility. ClimaX is pre-trained with a self-supervised learning objective on climate datasets derived from CMIP6. The pre-trained ClimaX can then be fine-tuned to address a breadth of climate and weather tasks, including those that involve atmospheric variables and spatio-temporal scales unseen during pretraining. Compared to existing data-driven baselines, we show that this generality in ClimaX results in superior performance on benchmarks for weather forecasting and climate projections, even when pretrained at lower resolutions and compute budgets"
publication: '*40th International Conference on Machine Learning (ICML), 2023* (**Spotlight**)'
url_pdf: https://arxiv.org/abs/2301.10343
url_project: https://www.microsoft.com/en-us/research/group/autonomous-systems-group-robotics/articles/introducing-climax-the-first-foundation-model-for-weather-and-climate/
url_code: https://microsoft.github.io/ClimaX/
---
