---
layout: page
title: Home
id: home
permalink: /
---

# Welcome!

> This website belongs to  [[about|me]], [Angadh](https://www.sems.qmul.ac.uk/staff/a.nanjangud). Sometimes I write digital notes
> and a small percentage of it gets published here. If you stumbled
> here as an internet stranger, you might wish to see what's top of my mind
> by exploring the most recently updated notes below. A [[all notes|complete archive]] is also available
> but I'd recommend surfing by Topics at the bottom of this page instead. Current undergraduate students at QMUL looking for teaching materials can go  straight to [[My teaching content]]. 

<h5>Recently updated notes</h5>

<ul>
  {% assign recent_notes = site.notes | sort: "last_modified_at_timestamp" | reverse %}
  {% for note in recent_notes limit: 5 %}
    <li>
      {{ note.last_modified_at | date: "%Y-%m-%d" }} — <a class="internal-link" href="{{ site.baseurl }}{{ note.url }}">{{ note.title }}</a>
    </li>
  {% endfor %}
</ul>

<h5>Topics</h5>

<div class="category-list">
{% assign tags = site.notes | map: "tags" | uniq | sort_natural %}
{% for tag in tags %}
  {% if tag != nil %}
    <a class="category-link" href="{{ site.baseurl }}/tags/{{ tag | slugify }}" rel="noopener">{{ tag }}</a>{% unless forloop.last %}, {% endunless %}
  {% endif %}
{% endfor %}
</div>
