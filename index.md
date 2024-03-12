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

[Jump to the current week](#week-9-modeling-in-practice){: .btn } [Lab Solutions](https://edstem.org/us/courses/51951/discussion/4183397){: .btn .btn-green }

Click the 🎥 button to view the recording of a lecture/discussion.<br>Click the 📝 button to view lecture notebooks after they've been filled in during lecture.

{: .green }
**If at least 80% of the class fills out both [SETs](https://academicaffairs.ucsd.edu/Modules/Evals) and the [End-of-Quarter Survey](https://docs.google.com/forms/d/e/1FAIpQLSe-ADKrha3WLbf1U6mrwxxy7hckSHCsMJfNjs53AoPP0LJABg/viewform) by SATURDAY AT 8AM, we'll add 1% of extra credit to everyone's overall grade!**

{% for module in site.modules %}
{{ module }}
{% endfor %}