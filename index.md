---
layout: home
title: 🏠 Home
nav_exclude: false
nav_order: 1
---

# {{ site.tagline }}

{: .mb-2 }
{{ site.description }}
{: .fs-6 .fw-300 }

{{ site.staffersnobio }}

[Jump to the current week](#week-9-modeling-in-practice){: .btn }

Click the 🎥 button to view the recording of a lecture/discussion.<br>Click the 📝 button to view lecture notebooks after they've been filled in during lecture.

{: .red }
**This is the website of a prior offering of DSC 80. The recordings for all lectures are publicly available and can be found below. To see the latest version of DSC 80, go to [dsc80.com](https://dsc80.com).**

{% for module in site.modules %}
{{ module }}
{% endfor %}