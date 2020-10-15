---
title: Article template
layout: post
category: article
tags:  
---

{:refdef: style="text-align: center;"}
![My image](/assets/images/pic02.jpg)
{: refdef}

[Link to a post]({% link _drafts/2020-09-05-story_template.md %})

$$a_2^2 = 4$$

{% capture code %}{% raw %}# Testing testing
import numpy as np

Z = np.linspace(1,118,118)
rho = np.linspace(0,300,300*100)
print(f"This is z: {z}")
c=3
if (c==3):
    print(f"c is {c}"){% endraw %}{% endcapture %}
{% include code.html code=code lang="javascript" title="sample" %}
