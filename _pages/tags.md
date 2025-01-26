---
layout: page
title: Tags
permalink: /tags
---

# Notes by Tag

<div class="tag-list">
{% assign tags = site.notes | map: "tags" | uniq | sort %}
{% for tag in tags %}
  {% if tag != nil %}
    <a class="internal-link" href="#{{ tag | slugify }}">{{ tag }}</a>
  {% endif %}
{% endfor %}
</div>

{% for tag in tags %}
  {% if tag != nil %}
## <span id="{{ tag | slugify }}">{{ tag }}</span>
<ul>
  {% assign notes = site.notes | where_exp: "note", "note.tags contains tag" %}
  {% for note in notes %}
    <li>
      <a class="internal-link" href="{{ site.baseurl }}{{ note.url }}">{{ note.title }}</a>
    </li>
  {% endfor %}
</ul>
  {% endif %}
{% endfor %}

