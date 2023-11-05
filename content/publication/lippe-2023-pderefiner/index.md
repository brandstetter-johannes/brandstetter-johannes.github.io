---
# Documentation: https://wowchemy.com/docs/managing-content/

title: PDE-Refiner - Achieving Accurate Long Rollouts with Neural PDE Solvers
subtitle: ''
summary: 'PDE-Refiner is an iterative refinement process that enables neural operator training for accurate and stable predictions over long time horizons. Published at NeurIPS 2023 (**Spotlight**).'
authors:
- Phillip Lippe
- Bastiaan S. Veeling
- Paris Perdikaris
- Richard E. Turner
- Johannes Brandstetter
tags: ['Partial Differential Equations', 'AI4Science', 'Neural PDE Solvers', 'Microsoft', 'Deep Learning']
categories: ['AI4Science']
date: 2023-08-10T12:55:17+02:00
lastmod: 2023-08-10T12:55:17+02:00
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: 'PDE-Refiner'
  focal_point: 'Center'
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
publishDate: '2023-08-10T12:55:17+02:00'
publication_types:
- '1'
abstract: "Time-dependent partial differential equations (PDEs) are ubiquitous in science and engineering. Recently, mostly due to the high computational cost of traditional solution techniques, deep neural network based surrogates have gained increased interest. The practical utility of such neural PDE solvers relies on their ability to provide accurate, stable predictions over long time horizons, which is a notoriously hard problem. In this work, we present a large-scale analysis of common temporal rollout strategies, identifying the neglect of non-dominant spatial frequency information, often associated with high frequencies in PDE solutions, as the primary pitfall limiting stable, accurate rollout performance. Based on these insights, we draw inspiration from recent advances in diffusion models to introduce PDE-Refiner; a novel model class that enables more accurate modeling of all frequency components via a multi-step refinement process. We validate PDE-Refiner on challenging benchmarks of complex fluid dynamics, demonstrating stable and accurate rollouts that consistently outperform state-of-the-art models, including neural, numerical, and hybrid neural-numerical architectures. Finally, PDE-Refiner's connection to diffusion models enables an accurate and efficient assessment of the model's predictive uncertainty, allowing us to estimate when the surrogate becomes inaccurate."
publication: '*Thirty-seventh Conference on Neural Information Processing Systems (NeurIPS), 2023* (**Spotlight**)'
url_pdf: https://arxiv.org/abs/2308.05732
url_poster: https://phlippe.github.io/media/PDERefiner_F4LCD_Poster.pdf
url_code: https://microsoft.github.io/pdearena/
url_project: https://phlippe.github.io/PDERefiner/
url_slides: https://phlippe.github.io/media/PDERefiner_Slides.pdf
url_video: https://youtu.be/N4IGE6pH7v8
---
