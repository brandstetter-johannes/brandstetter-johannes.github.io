---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Align-RUDDER -- Learning From Few Demonstrations by Reward Redistribution
subtitle: ''
summary: 'We generalise steerable E(3) equivariant graph neural networks such that node and edge updates are able to leverage covariant information. Published at ICLR 2022 (Oral).'
authors:
- Vihang Patil 
- Markus Hofmarcher
- Marius-Constantin Dinu
- Matthias Dorfer
- Patrick Blies
- Johannes Brandstetter
- José A. Arjona-Medina
- Sepp Hochreiter
tags: ['Reinforcement Learning', 'Delayed Rewards', 'Sequence Alignment', 'Deep Learning']
categories: ['Reinforcement Learning', '']
date: 2020-09-29T12:55:17+02:00
lastmod: 2020-09-29T12:55:17+02:00
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: 'Sequence alignment in proteins and in RL sequences'
  focal_point: 'TopRight'
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
publishDate: '2020-09-29T12:55:17+02:00'
publication_types:
- '1'
abstract: 'Reinforcement learning algorithms require many samples when solving complex hierarchical tasks with sparse and delayed rewards. For such complex tasks, the recently proposed RUDDER uses reward redistribution to leverage steps in the Q-function that are associated with accomplishing sub-tasks. However, often only few episodes with high rewards are available as demonstrations since current exploration strategies cannot discover them in reasonable time. In this work, we introduce Align-RUDDER, which utilizes a profile model for reward redistribution that is obtained from multiple sequence alignment of demonstrations. Consequently, Align-RUDDER employs reward redistribution effectively and, thereby, drastically improves learning on few demonstrations. Align-RUDDER outperforms competitors on complex artificial tasks with delayed rewards and few demonstrations. On the Minecraft ObtainDiamond task, Align-RUDDER is able to mine a diamond, though not frequently.'
publication: '*39th International Conference on Machine Learning (ICML), 2022* (**Oral**)'
url_pdf: https://arxiv.org/abs/2009.14108
url_code: https://github.com/ml-jku/align-rudder
url_poster: https://brandstetter-johannes.github.io/media/Align-RUDDER_poster.png
url_slides: https://brandstetter-johannes.github.io/media/Align-RUDDER_slides.pdf
links:
- name: Blog post
  url: https://ml-jku.github.io/align-rudder/
---
