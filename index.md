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

[Jump to the current week](#week-5-http-midterm-exam-br-small-let-suraj-know-which-topics-old-exam-questions-you-want-him-to-take-up-in-tuesday-s-lecture-at-a-href-https-docs-google-com-forms-d-e-1faipqlscwbvzv9hbv-wx-itkhuvrnkpmmtfjzvferke9gs7-8dfcrbq-viewform-b-q-dsc80-com-b-a-small){: .btn } [Lab Solutions](https://edstem.org/us/courses/51951/discussion/4183397){: .btn .btn-green }

Click the 🎥 button to view the recording of a lecture/discussion.<br>Click the 📝 button to view lecture notebooks after they've been filled in during lecture.

{% for module in site.modules %}
{{ module }}
{% endfor %}