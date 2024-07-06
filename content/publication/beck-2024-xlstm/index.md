---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Vision-LSTM -- xLSTM as Generic Vision Backbone
subtitle: ''
summary: 'We introduce Vision-LSTM (ViL), an adaption of the xLSTM building blocks to computer vision.'
authors:
- Benedikt Alkin 
- Maximilian Beck
- Korbinian Poeppel
- Sepp Hochreiter
- Johannes Brandstetter
tags: ['Computer Vision', 'xLSTM', 'Pretraining', 'Deep Learning']
categories: ['Computer Vision']
date: 2024-06-06T12:55:17+02:00
lastmod: 2024-06-06T12:55:17+02:00
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: 'Vision-LSTM architecture'
  focal_point: 'TopRight'
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
publishDate: '2024-06-06T12:55:17+02:00'
publication_types:
- '1'
abstract: 'Transformers are widely used as generic backbones in computer vision, despite initially introduced for natural language processing. Recently, the Long Short-Term Memory (LSTM) has been extended to a scalable and performant architecture - the xLSTM - which overcomes long-standing LSTM limitations via exponential gating and parallelizable matrix memory structure. In this report, we introduce Vision-LSTM (ViL), an adaption of the xLSTM building blocks to computer vision. ViL comprises a stack of xLSTM blocks where odd blocks process the sequence of patch tokens from top to bottom while even blocks go from bottom to top. Experiments show that ViL holds promise to be further deployed as new generic backbone for computer vision architectures.'
publication: 'Preprint'
url_pdf: https://arxiv.org/abs/2406.04303
url_code: https://github.com/nx-ai/vision-lstm
url_project: https://nx-ai.github.io/vision-lstm/
---