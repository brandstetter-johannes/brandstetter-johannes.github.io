---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Geometric and Physical Quantities Improve E(3) Equivariant Message Passing
subtitle: ''
summary: 'We generalise steerable E(3) equivariant graph neural networks such that node and edge updates are able to leverage covariant information. Published at ICLR 2022 (Spotlight).'
authors:
- Johannes Brandstetter 
- Rob Hesselink
- Elise van der Pol
- Erik Bekkers
- Max Welling
tags: ['Learn2Simulate', 'Geometric Deep Learning', 'AI4Science', 'Graph Neural Networks', 'Equivariance', 'Deep Learning']
categories: ['Geometric Deep Learning']
date: 2021-10-06T12:55:17+02:00
lastmod: 2021-10-06T12:55:17+02:00
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: 'Node and edge updates transform covariantly'
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
abstract: 'Including covariant information, such as position, force, velocity or spin is important in many tasks in computational physics and chemistry. We introduce Steerable E(3) Equivariant Graph Neural Networks (SEGNNs) that generalise equivariant graph networks, such that node and edge attributes are not restricted to invariant scalars, but can contain covariant information, such as vectors or tensors. This model, composed of steerable MLPs, is able to incorporate geometric and physical information in both the message and update functions. Through the definition of steerable node attributes, the MLPs provide a new class of activation functions for general use with steerable feature fields. We discuss ours and related work through the lens of equivariant non-linear convolutions, which further allows us to pin-point the successful components of SEGNNs: non-linear message aggregation improves upon classic linear (steerable) point convolutions; steerable messages improve upon recent equivariant graph networks that send invariant messages. We demonstrate the effectiveness of our method on several tasks in computational physics and chemistry and provide extensive ablation studies.'
publication: '*10th International Conference on Learning Representations (ICLR), 2022* (**Spotlight**)'
url_pdf: https://arxiv.org/abs/2110.02905
url_code: https://github.com/RobDHess/Steerable-E3-GNN
url_poster: https://brandstetter-johannes.github.io/media/SEGNN_poster.png
url_slides: https://brandstetter-johannes.github.io/media/SEGNN_slides.pdf
links:
- name: Blog post
  url: https://robdhess.github.io/Steerable-E3-GNN/
---
