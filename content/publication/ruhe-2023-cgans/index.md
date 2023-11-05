---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Geometric Clifford Algebra Networks
subtitle: ''
summary: 'We introduce Geometric Clifford Algebra Networks (GCANs) which parameterize combinations of learnable group actions. Published at ICML 2023.'
authors:
- David Ruhe
- Jayesh K. Gupta
- Steven de Keninck
- Max Welling
- Johannes Brandstetter
tags: ['Partial Differential Equations', 'Learning2Simulate', 'Clifford Algebras', 'Geometric Algebras', 'Geometric Deep Learning', 'AI4Science', 'Neural Solvers', 'Microsoft', 'Graph Neural Networks', 'Deep Learning']
categories: ['Geometric Deep Learning']
date: 2023-02-13T12:55:17+02:00
lastmod: 2023-02-13T12:55:17+02:00
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: 'CGAN layers'
  focal_point: 'TopRight'
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
publishDate: '2023-02-13T12:55:17+02:00'
publication_types:
- '1'
abstract: 'We propose Geometric Clifford Algebra Networks (GCANs) for modeling dynamical systems. GCANs are based on symmetry group transformations using geometric (Clifford) algebras. We first review the quintessence of modern (plane-based) geometric algebra, which builds on isometries encoded as elements of the Pin(p,q,r) group. We then propose the concept of group action layers, which linearly combine object transformations using pre-specified group actions. Together with a new activation and normalization scheme, these layers serve as adjustable geometric templates that can be refined via gradient descent. Theoretical advantages are strongly reflected in the modeling of three-dimensional rigid body transformations as well as large-scale fluid dynamics simulations, showing significantly improved performance over traditional methods.'
publication: '*40th International Conference on Machine Learning (ICML), 2023*'
url_pdf: https://arxiv.org/abs/2302.06594
url_code: https://microsoft.github.io/cliffordlayers/
url_project: https://www.microsoft.com/en-us/research/lab/microsoft-research-ai4science/articles/introducing-cliffordlayers-neural-network-layers-inspired-by-clifford-geometric-algebras/
url_poster: https://brandstetter-johannes.github.io/media/CGAN-ICML-2023.pdf
links:
- name: Blog post
  url: https://davidruhe.github.io/2023/06/06/ga-layers.html
---
