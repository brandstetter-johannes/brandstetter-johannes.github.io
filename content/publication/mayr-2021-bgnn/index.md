---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Boundary Graph Neural Networks for 3D Simulations
subtitle: ''
summary: 'We generalize graph neural network based simulations of Lagrangian dynamics to complex boundaries as encountered in daily life engineering setups. Published at AAAI 2023.'
authors:
- Andreas Mayr 
- Sebastian Lehner
- Arno Mayrhofer
- Christoph Kloss
- Sepp Hochreiter
- Johannes Brandstetter
tags: ['Learning2Simulate', 'Geometric Deep Learning', 'AI4Science', 'Graph Neural Networks', 'Lagrangian Fluid Mechanics', 'Deep Learning']
categories: ['Learning2Simulate']
date: 2021-06-21T12:55:17+02:00
lastmod: 2021-06-21T12:55:17+02:00
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: 'Effective interaction with boundary surface areas.'
  focal_point: 'TopRight'
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
publishDate: '2021-10-06T12:55:17+02:00'
publication_types:
- '1'
abstract: 'The abundance of data has given machine learning considerable momentum in natural sciences and engineering, though modeling of physical processes is often difficult. A particularly tough problem is the efficient representation of geometric boundaries. Triangularized geometric boundaries are well understood and ubiquitous in engineering applications. However, it is notoriously difficult to integrate them into machine learning approaches due to their heterogeneity with respect to size and orientation. In this work, we introduce an effective theory to model particle-boundary interactions, which leads to our new Boundary Graph Neural Networks (BGNNs) that dynamically modify graph structures to obey boundary conditions. The new BGNNs are tested on complex 3D granular flow processes of hoppers, rotating drums and mixers, which are all standard components of modern industrial machinery but still have complicated geometry. BGNNs are evaluated in terms of computational efficiency as well as prediction accuracy of particle flows and mixing entropies. BGNNs are able to accurately reproduce 3D granular flows within simulation uncertainties over hundreds of thousands of simulation timesteps. Most notably, in our experiments, particles stay within the geometric objects without using handcrafted conditions or restrictions.'
publication: '*37th AAAI Conference on Artificial Intelligence (AAAI), 2023*'
url_pdf: https://arxiv.org/abs/2106.11299
url_code: https://ml-jku.github.io/bgnn/
url_poster: https://brandstetter-johannes.github.io/media/BGNN_poster.pdf
links:
- name: Blog post
  url: https://ml-jku.github.io/bgnn/
---
