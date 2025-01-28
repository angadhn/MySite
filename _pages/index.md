---
layout: page
title: Home
id: home
permalink: /
---

# Welcome!
<!-- 
<div class="welcome-block">
  • This website belongs to [[about|me]], <span class="external-link"><a href="https://www.sems.qmul.ac.uk/staff/a.nanjangud">Angadh</a></span><br>
  
  • If you are:
    - a current undergraduate student at QMUL, you might wish to start at <span class="internal-link">[[My teaching content]]</span>
    - interested in space engineering or building a collaboration, you may wish to explore <span class="internal-link">[[My research interests]]</span>
    - an internet stranger who stumbled here, you might wish to:
      - read what's top of my mind by exploring the most recently updated notes below
      - browse through <span class="internal-link">[[My longer form writing]]</span>
      - check out the <a class="internal-link" href="{{ site.baseurl }}/all-notes">complete archive of notes</a>
</div> -->

> This website belongs to [[about|me]], [Angadh](https://www.sems.qmul.ac.uk/staff/a.nanjangud). Sometimes I write digital notes
> and a small percentage of it gets published here. If you stumbled
> here as an internet stranger, you might wish to see what's top of my mind
> by exploring the most recently updated notes below. Or you may wish to
> browse through [[My longer form writing]]. A [[all-notes|complete archive]] is also available
> but I'd recommend surfing by Topics at the bottom of this page instead; you might also
> find these useful to filter through my writings on space tech. Current undergraduate
> students at QMUL looking for teaching materials can go  straight to [[My teaching content]]. 

**Recently updated notes**

<ul>
  {% assign recent_notes = site.notes | sort: "last_modified_at_timestamp" | reverse %}
  {% for note in recent_notes limit: 5 %}
    <li>
      {{ note.last_modified_at | date: "%Y-%m-%d" }} — <a class="internal-link" href="{{ site.baseurl }}{{ note.url }}">{{ note.title }}</a>
    </li>
  {% endfor %}
</ul>

<strong>Topics</strong>

<div class="category-list">
{% assign tags = site.notes | map: "tags" | uniq | sort_natural %}
{% for tag in tags %}
  {% if tag != nil %}
    <a class="category-link" href="{{ site.baseurl }}/tags/{{ tag | slugify }}" rel="noopener">{{ tag }}</a>{% unless forloop.last %}, {% endunless %}
  {% endif %}
{% endfor %}
</div>
