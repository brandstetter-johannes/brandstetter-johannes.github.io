---
# Documentation: https://wowchemy.com/docs/managing-content/

title: We identify particle clustering originating from tensile instabilities as one of the primary pitfalls. Based on these insights, we enhance both training and rollout inference of GNN-based simulators with varying components from standard SPH solvers, including pressure, viscous, and external force components.
subtitle: ''
summary: ''
authors:
- Artur P. Toshev 
- Jonas A. Erbesdobler
- Nikolaus A. Adams
- Johannes Brandstetter
tags: ['Partial Differential Equations', 'Learn2Simulate', 'Geometric Deep Learning', 'AI4Science', 'Graph Neural Networks', 'Neural Surrogates', 'Lagrangian Fluid Mechanics', 'Smoothed Particle Hydrodynamics', 'Deep Learning']
categories: ['Learn2Simulate']
date: 2024-02-09T12:55:17+02:00
lastmod: 2024-02-09T12:55:17+02:00
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: 'Different components of Neural SPH'
  focal_point: 'TopRight'
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
publishDate: '2024-02-09T12:55:17+02:00'
publication_types:
- '1'
abstract: 'Smoothed particle hydrodynamics (SPH) is omnipresent in modern engineering and scientific disciplines. SPH is a class of Lagrangian schemes that discretize fluid dynamics via finite material points that are tracked through the evolving velocity field. Due to the particle-like nature of the simulation, graph neural networks (GNNs) have emerged as appealing and successful surrogates. However, the practical utility of such GNN-based simulators relies on their ability to faithfully model physics, providing accurate and stable predictions over long time horizons - which is a notoriously hard problem. In this work, we identify particle clustering originating from tensile instabilities as one of the primary pitfalls. Based on these insights, we enhance both training and rollout inference of state-of-the-art GNN-based simulators with varying components from standard SPH solvers, including pressure, viscous, and external force components. All neural SPH-enhanced simulators achieve better performance, often by orders of magnitude, than the baseline GNNs, allowing for significantly longer rollouts and significantly better physics modeling.'
publication: '*41th International Conference on Machine Learning (ICML), 2024*'
url_pdf: https://iclr.cc/media/iclr-2024/Slides/21337.pdf
url_code: https://github.com/tumaer/neuralsph
url_project: https://arturtoshev.github.io/neural-sph-blog
url_poster: https://brandstetter-johannes.github.io/media/CGAN-ICML-2023.pdf
---
