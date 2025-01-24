---
layout: page
title: All Notes
id: all-notes
permalink: /all-notes
---

# All Notes by Date 📝

{% assign notes_by_year = site.notes | group_by_exp: "note", "note.date | date: '%Y'" %}
{% for year in notes_by_year %}
## {{ year.name }}
{% assign notes_by_month = year.items | group_by_exp: "note", "note.date | date: '%B'" %}
{% for month in notes_by_month %}
### {{ month.name }}
<ul>
  {% for note in month.items %}
    <li>
      {{ note.date | date: "%Y-%m-%d" }} — <a class="internal-link" href="{{ site.baseurl }}{{ note.url }}">{{ note.title }}</a>
    </li>
  {% endfor %}
</ul>
{% endfor %}
{% endfor %} 