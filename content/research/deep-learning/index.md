---
title: General Deep Learning
summary: After switching from High Energy Physics to Deep Learning, I started working in Reinforcement Learning before pivoting towards Associative Memories and modern Transformer networks. Recent years have shown that scalable ideas, improving the datasets, and clever engineering are the ingredients for ever better Deep Learning models. This totally coincides with my experience, and -- needless to say -- I will continue working on general large-scale Deep Learning directions.
tags:
  - Deep Learning
  - Modern Hopfield Networks
  - Self-Attention
  - Transformer
  - Associative Memory
  - Reinforcement Learning
  - Delayed Rewards
date: '2018-07-01'

# Optional external URL for project (replaces project detail page).
external_link: ''

image:
  caption: Neural net completion for "artificial intelligence", as done by DALL-E mini
  focal_point: Smart

# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
# slides: example
---

After switching from High Energy Physics to Deep Learning, I started working in Reinforcement Learning before pivoting towards Associative Memories and modern Transformer networks. Recent years have shown that scalable ideas, improving the datasets, and clever engineering are the ingredients for ever better Deep Learning models. This totally coincides with my experience, and -- needless to say -- I will continue working on general large-scale Deep Learning directions.

In [Reinforcement Learning](https://brandstetter-johannes.github.io/tag/reinforcement-learning/), we introduce [RUDDER](https://brandstetter-johannes.github.io/publication/medina-2018-rudder/) a novel model-free RL approach to overcome delayed reward problems. RUDDER directly and efficiently assigns credit to reward-causing state-action pairs and thereby speeds up learning in model-free reinforcement learning with delayed rewards dramatically. I have written a lengthy [blogpost](https://ml-jku.github.io/rudder/) on the RUDDER idea. With [Align-RUDDER](https://brandstetter-johannes.github.io/publication/patil-2020-alignrudder/), we extended the RUDDER framework by assuming that episodes with high rewards are given as demonstrations. Finally, we [prove converge for actor-critic methods like RUDDER or PPO](https://brandstetter-johannes.github.io/publication/holzleitner-2020-convergence/).

In [Hopfield Networks is All You Need](https://brandstetter-johannes.github.io/publication/ramsauer-2020-hopfield/), we introduced a new energy function and a corresponding new update rule which is guaranteed to converge to a local minimum of the energy function. The new modern Hopfield Network with continuous states keeps the characteristics of its discrete counterparts, i.e., exponential storage capacity and fast convergence. Due to its continuous states this new modern Hopfield Network is differentiable and can be integrated into deep learning architectures. Typically patterns are retrieved after one update which is compatible with activating the layers of deep networks. Surprisingly, the new update rule is the attention mechanism of transformer networks introduced in [Attention Is All You Need](https://arxiv.org/abs/1706.03762). I have written a lenthy [blogpost](https://ml-jku.github.io/hopfield-layers/) on modern Hopfield Networks. One SOTA application of modern Hopfield Networks can be found in our paper [Modern Hopfield Networks and Attention for Immune Repertoire Classification](https://brandstetter-johannes.github.io/publication/widrich-2020-hopfield/). Here, the high storage capacity of modern Hopfield Networks is exploited to solve a challenging multiple instance learning (MIL) problem in computational biology called immune repertoire classification. Finally, we found out that linearized attention models, such as the [Performer idea](https://arxiv.org/abs/2009.14794) resemble the update rule of classical Hopfield Networks. [Our blogpost](https://ml-jku.github.io/blog-post-performer/) was published in the ICLR2022 blogpost track.

I will keep working on understanding large scale architectures. There are quite a few interesting projects I am involved in.

## Stay stuned for new work
