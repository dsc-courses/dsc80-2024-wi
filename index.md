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

<!-- [Jump to the current week](#week-9-code-sklearn-code-pipelines-generalization-and-cross-validation){: .btn } -->

<!-- [Recordings](https://podcast.ucsd.edu/){: .btn .btn-blue } -->

{: .warning }
**This site is under construction and everything is subject to change.**

<!-- {: .note }
**Dec 6, 2023:** The Final Exam will take place on Mon., Dec 11,
from 3-6pm in WLH 2005 (our usual lecture room). If 85% of the class fills out
both the [Student Evaluations of Teaching][set] and the [End-of-Quarter
Survey][survey] before 11:59pm Dec 8, the entire class will get +1% on their
Final Exam grade.

[set]: https://academicaffairs.ucsd.edu/Modules/Evals
[survey]: https://forms.gle/AojdCsxqqeNJLMqz7 -->

<!-- To view the lecture recordings, click on the 🎥 button for each lecture. -->

<!-- **Some office hours on Wednesday 3/8, Thursday 3/9, and Tuesday 3/21 are being held in the SDSC Auditorium instead of the 2nd floor – look closely at the [calendar](calendar) for details.** Treat these office hours as study sessions – come to them to work on projects or study for the final exam! -->

{% for module in site.modules %}
{{ module }}
{% endfor %}

<!-- <center>
<iframe src="10-80-enrollment.html" scrolling="no" style="border:none;" seamless="seamless" height="480" width="100%">
</center> -->
