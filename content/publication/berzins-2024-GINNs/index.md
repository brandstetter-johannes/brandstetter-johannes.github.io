---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Clifford Neural Layers for PDE Modeling
subtitle: ''
summary: 'We introduce neural network layers based on operations on composite objects of scalars, vectors, and higher order objects such as bivectors. Published at ICLR 2023.'
authors:
- Johannes Brandstetter 
- Rianne van den Berg
- Max Welling
- Jayesh Gupta
tags: ['Partial Differential Equations', 'Learn2Simulate', 'Clifford Algebras', 'Geometric Algebras', 'Geometric Deep Learning', 'AI4Science', 'Neural Surrogates', 'Neural Operators', 'Microsoft', 'Deep Learning']
categories: ['Geometric Deep Learning']
date: 2022-09-08T12:55:17+02:00
lastmod: 2022-09-08T12:55:17+02:00
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: 'Clifford Fourier Neural Operator'
  focal_point: 'TopRight'
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
publishDate: '2022-09-08T12:55:17+02:00'
publication_types:
- '1'
abstract: 'Partial differential equations (PDEs) see widespread use in sciences and engineering to describe simulation of physical processes as scalar and vector fields interacting and coevolving over time. Due to the computationally expensive nature of their standard solution methods, neural PDE surrogates have become an active research topic to accelerate these simulations. However, current methods do not explicitly take into account the relationship between different fields and their internal components, which are often correlated. Viewing the time evolution of such correlated fields through the lens of multivector fields allows us to overcome these limitations. Multivector fields consist of scalar, vector, as well as higher-order components, such as bivectors and trivectors. Their algebraic properties, such as multiplication, addition and other arithmetic operations can be described by Clifford algebras. To our knowledge, this paper presents the first usage of such multivector representations together with Clifford convolutions and Clifford Fourier transforms in the context of deep learning. The resulting Clifford neural layers are universally applicable and will find direct use in the areas of fluid dynamics, weather forecasting, and the modeling of physical systems in general. We empirically evaluate the benefit of Clifford neural layers by replacing convolution and Fourier operations in common neural PDE surrogates by their Clifford counterparts on 2D Navier-Stokes and weather modeling tasks, as well as 3D Maxwell equations. For similar parameter count, Clifford neural layers consistently improve generalization capabilities of the tested neural PDE surrogates.'
publication: '*11th International Conference on Learning Representations (ICLR), 2023*'
url_pdf: https://arxiv.org/abs/2209.04934
url_code: https://microsoft.github.io/cliffordlayers/
url_project: https://www.microsoft.com/en-us/research/lab/microsoft-research-ai4science/articles/introducing-cliffordlayers-neural-network-layers-inspired-by-clifford-geometric-algebras/
url_poster: https://brandstetter-johannes.github.io/media/Clifford-ICLR-2023-poster.pdf
url_slides: https://brandstetter-johannes.github.io/media/Clifford-ICLR-2023.pdf
links:
- name: Blog post
  url: https://davidruhe.github.io/2023/06/06/clifford-layers.html
---
