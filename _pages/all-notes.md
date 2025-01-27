---
layout: page
title: All Notes
id: all-notes
permalink: /all-notes
---

# All Notes by Date 📝

{% assign sorted_notes = site.notes | sort: "published" | reverse %}
{% assign notes_by_year = sorted_notes | group_by_exp: "note", "note.published | date: '%Y'" %}
{% for year in notes_by_year %}
## {{ year.name }}
{% assign notes_by_month = year.items | group_by_exp: "note", "note.published | date: '%B'" %}
{% for month in notes_by_month %}
### {{ month.name }}
<ul>
  {% for note in month.items %}
    <li>
      {{ note.published | date: "%Y-%m-%d" }} — <a class="internal-link" href="{{ site.baseurl }}{{ note.url }}">{{ note.title }}</a>
    </li>
  {% endfor %}
</ul>
{% endfor %}
{% endfor %} 