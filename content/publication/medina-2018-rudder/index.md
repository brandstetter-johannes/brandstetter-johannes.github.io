---
# Documentation: https://wowchemy.com/docs/managing-content/

title: RUDDER -- Return Decomposition for Delayed Rewards
subtitle: ''
summary: 'We propose RUDDER, a novel reinforcement learning approach for delayed rewards in finite Markov decision processes. Published at NeurIPS 2019.'
authors:
- José A. Arjona-Medina
- Michael Gillhofer
- Michael Widrich
- Thomas Unterthiner
- Johannes Brandstetter
- Sepp Hochreiter
tags: ['Reinforcement Learning', 'Delayed Rewards', 'Deep Learning']
categories: ['Reinforcement Learning']
date: 2018-06-20T12:55:17+02:00
lastmod: 2018-06-20T12:55:17+02:00
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: 'Reward redistribution for delayed rewards'
  focal_point: 'TopRight'
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
publishDate: '2018-06-20T12:55:17+02:00'
publication_types:
- '1'
abstract: 'We propose RUDDER, a novel reinforcement learning approach for delayed rewards in finite Markov decision processes (MDPs). In MDPs the Q-values are equal to the expected immediate reward plus the expected future rewards. The latter are related to bias problems in temporal difference (TD) learning and to high variance problems in Monte Carlo (MC) learning. Both problems are even more severe when rewards are delayed. RUDDER aims at making the expected future rewards zero, which simplifies Q-value estimation to computing the mean of the immediate reward. We propose the following two new concepts to push the expected future rewards toward zero. (i) Reward redistribution that leads to return-equivalent decision processes with the same optimal policies and, when optimal, zero expected future rewards. (ii) Return decomposition via contribution analysis which transforms the reinforcement learning task into a regression task at which deep learning excels. On artificial tasks with delayed rewards, RUDDER is significantly faster than MC and exponentially faster than Monte Carlo Tree Search (MCTS), TD(λ), and reward shaping approaches. At Atari games, RUDDER on top of a Proximal Policy Optimization (PPO) baseline improves the scores, which is most prominent at games with delayed rewards.'
publication: '*Thirty-second Conference on Neural Information Processing Systems (NeurIPS), 2019*'
url_pdf: https://arxiv.org/abs/1806.078575
url_code: https://github.com/ml-jku/rudder
url_poster: https://brandstetter-johannes.github.io/media/RUDDER_poster.pdf
links:
- name: Blog post
  url: https://ml-jku.github.io/rudder/
---
