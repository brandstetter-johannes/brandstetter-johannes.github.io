---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Towards Multi-spatiotemporal-scale Generalized PDE Modeling
subtitle: ''
summary: 'We present PDEArena, a modern PyTorch Lightning-based deep learning framework for neural PDE modeling. Published at TMLR 07/2023.'
authors:
- Jayesh K. Gupta
- Johannes Brandstetter
tags: ['Partial Differential Equations', 'Learn2Simulate', 'AI4Science', 'Neural Surrogates', 'Neural Operators', 'Microsoft', 'Deep Learning']
categories: ['Learn2Simulate']
date: '2022-09-30'
lastmod: 2022-09-30T09:16:01+01:00
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: 'Spatiotemporal simulation'
  focal_point: 'TopRight'
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
publishDate: '2022-09-30T09:16:01.817577Z'
publication_types:
- '2'
abstract: 'Partial differential equations (PDEs) are central to describing complex physical system simulations. Their expensive solution techniques have led to an increased interest in deep neural network based surrogates. However, the practical utility of training such surrogates is contingent on their ability to model complex multi-scale spatio-temporal phenomena. Various neural network architectures have been proposed to target such phenomena, most notably Fourier Neural Operators (FNOs), which give a natural handle over local & global spatial information via parameterization of different Fourier modes, and U-Nets which treat local and global information via downsampling and upsampling paths. However, generalizing across different equation parameters or time-scales still remains a challenge. In this work, we make a comprehensive comparison between various FNO, ResNet, and U-Net like approaches to fluid mechanics problems in both vorticity-stream and velocity function form. For U-Nets, we transfer recent architectural improvements from computer vision, most notably from object segmentation and generative modeling. We further analyze the design considerations for using FNO layers to improve performance of U-Net architectures without major degradation of computational cost. Finally, we show promising results on generalization to different PDE parameters and time-scales with a single surrogate model'
publication: '*Transactions on Machine Learning (TMLR), 07/2023*'
url_pdf: https://openreview.net/forum?id=dPSTDbGtBY
url_code: https://microsoft.github.io/pdearena/
url_project: https://www.microsoft.com/en-us/research/group/autonomous-systems-group-robotics/articles/open-sourcing-pdearena-2/
---
