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

<!-- {: .green }
**Come to the HDSI undergraduate social on Friday (2/23) from 3-5PM on the HDSI Patio – I'll be there, and so will free food! 🍕** -->

[Jump to the current week](#week-7-text-data-linear-regression){: .btn } [Lab Solutions](https://edstem.org/us/courses/51951/discussion/4183397){: .btn .btn-green }

Click the 🎥 button to view the recording of a lecture/discussion.<br>Click the 📝 button to view lecture notebooks after they've been filled in during lecture.

{% for module in site.modules %}
{{ module }}
{% endfor %}