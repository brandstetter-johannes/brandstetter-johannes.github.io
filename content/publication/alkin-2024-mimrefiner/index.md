---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Mim-refiner -- A contrastive learning boost from intermediate pre-trained representations
subtitle: ''
summary: 'We introduce MIM (Masked Image Modeling)-Refiner, a contrastive learning boost for pre-trained MIM models..'
authors:
- Benedikt Alkin 
- Lukas Miklautz
- Sepp Hochreiter
- Johannes Brandstetter
tags: ['Computer Vision', 'Masked Image Modeling', 'Pretraining', 'Deep Learning']
categories: ['Computer Vision']
date: 2024-02-15T12:55:17+02:00
lastmod: 2024-02-15T12:55:17+02:00
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: 'Message Passing Neural PDE Solver'
  focal_point: 'TopRight'
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
publishDate: '2022-02-07T12:55:17+02:00'
publication_types:
- '1'
abstract: 'We introduce MIM (Masked Image Modeling)-Refiner, a contrastive learning boost for pre-trained MIM models. MIM-Refiner is motivated by the insight that strong representations within MIM models generally reside in intermediate layers. Accordingly, MIM-Refiner leverages multiple contrastive heads that are connected to different intermediate layers. In each head, a modified nearest neighbor objective constructs semantic clusters that capture semantic information which improves performance on downstream tasks, including off-the-shelf and fine-tuning settings.
The refinement process is short and simple - yet highly effective. Within a few epochs, we refine the features of MIM models from subpar to state-of-the-art, off-the-shelf features. Refining a ViT-H, pre-trained with data2vec 2.0 on ImageNet-1K, sets a new state-of-the-art in linear probing (84.7%) and low-shot classification among models that are pre-trained on ImageNet-1K. At ImageNet-1K 1-shot classification, MIM-Refiner advances the state-of-the-art to 64.2%, outperforming larger models that were trained on up to 2000 times more data such as DINOv2-g, OpenCLIP-G and MAWS-6.5B.'
publication: 'Preprint'
url_pdf: https://arxiv.org/abs/2402.10093
url_code: https://github.com/ml-jku/MIM-Refiner
url_project: https://ml-jku.github.io/MIM-Refiner/
---