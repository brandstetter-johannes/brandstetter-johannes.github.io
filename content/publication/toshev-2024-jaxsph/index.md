---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Learning Lagrangian Fluid Mechanics with E(3)-Equivariant Graph Neural Networks
subtitle: ''
summary: 'We introduce E(3)-equivariant GNNs to two well-studied fluid-flow systems, namely 3D decaying Taylor-Green vortex and 3D reverse Poiseuille flow. Published at GSI 2023.'
authors:
- Artur P. Toshev 
- Gianluca Galletti
- Johannes Brandstetter
- Stefan Adami
- Nikolaus A. Adams
tags: ['Partial Differential Equations', 'Learn2Simulate', 'Geometric Deep Learning', 'AI4Science', 'Graph Neural Networks', 'Equivariance', 'Neural Surrogates', 'Lagrangian Fluid Mechanics', 'Deep Learning']
categories: ['Learn2Simulate']
date: 2023-05-24T12:55:17+02:00
lastmod: 2023-05-24T12:55:17+02:00
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: '3D reverse Poiseuille flow'
  focal_point: 'TopRight'
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
publishDate: '2023-05-24T12:55:17+02:00'
publication_types:
- '1'
abstract: 'We contribute to the vastly growing field of machine learning for engineering systems by demonstrating that equivariant graph neural networks have the potential to learn more accurate dynamic-interaction models than their non-equivariant counterparts. We benchmark two well-studied fluid-flow systems, namely 3D decaying Taylor-Green vortex and 3D reverse Poiseuille flow, and evaluate the models based on different performance measures, such as kinetic energy or Sinkhorn distance. In addition, we investigate different embedding methods of physical-information histories for equivariant models. We find that while currently being rather slow to train and evaluate, equivariant models with our proposed history embeddings learn more accurate physical interactions.'
publication: '*6th International Conference on Geometric Science of Information (GSI), 2023*'
url_pdf: https://arxiv.org/abs/2305.15603
url_code: https://github.com/tumaer/sph-hae
---
