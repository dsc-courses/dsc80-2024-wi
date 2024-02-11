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

{: .green }
If at least 80% of the class fills out the [**Mid-Quarter Survey**](https://docs.google.com/forms/d/e/1FAIpQLScHz9WJMST7QLKCl2cR3Oc3r-DO7qn4rutM_dCN8R7gluy5MA/viewform) by Saturday 2/17 at 11:59PM, then everyone will receive an extra 2 points (out of 80) on the Midterm Exam!

[Jump to the current week](#week-6-web-data-text-data){: .btn } [Lab Solutions](https://edstem.org/us/courses/51951/discussion/4183397){: .btn .btn-green }

Click the 🎥 button to view the recording of a lecture/discussion.<br>Click the 📝 button to view lecture notebooks after they've been filled in during lecture.

{% for module in site.modules %}
{{ module }}
{% endfor %}