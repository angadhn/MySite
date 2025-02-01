---
layout: page
title: Home
id: home
permalink: /
---

# Welcome!

> [[This site]] belongs to  [[about|me]], [Angadh](https://www.sems.qmul.ac.uk/staff/a.nanjangud). It is my version of making a place that I consider aesthetic to display things I write. While these are on the web, the intended frequent audience is likely to be just one- myself. My intention is to work my digital notes into essays that opine on things. Now, if you are not me and you stumbled here as an internet stranger looking to explore, you might wish to see what's top of my mind or seeing my recently updated notes below. They may not always be the same. A [[all notes|complete archive]] of [[this site]]'s content is also available though I am not sure if it is as useful as filtering by topic, which can be found below. I do maintain another [online presence](angadhn.com), my first attempt at making a personal site that I thought was aesthetic but I have come to admit that it isn't. However, it will continue to exist (and maybe even evolve) as the domain is linked to into my online teaching materials. A list of thse can also be found on this [[My teaching content|site]]. 
<div class="notes-grid">
  <div class="notes-column">
    <h5>Top of Mind</h5>
    <ul>
      {% assign top_notes = site.notes | where: "top_of_mind", true | sort: "last_modified_at_timestamp" | reverse %}
      {% for note in top_notes limit: 5 %}
        <li>
          • <a class="internal-link" href="{{ site.baseurl }}{{ note.url }}">{{ note.title }}</a>
        </li>
      {% endfor %}
    </ul>
  </div>

  <div class="notes-column">
    <h5>Updated</h5>
    <ul>
      {% assign recent_notes = site.notes | sort: "last_modified_at_timestamp" | reverse %}
      {% for note in recent_notes limit: 5 %}
        <li>
          • <a class="internal-link" href="{{ site.baseurl }}{{ note.url }}">{{ note.title }}</a>
        </li>
      {% endfor %}
    </ul>
  </div>
</div>

<h5>Topics</h5>

<div class="category-list">
{% assign tags = site.notes | map: "tags" | uniq | sort_natural %}
{% for tag in tags %}
  {% if tag != nil %}
    <a class="category-link" href="{{ site.baseurl }}/tags/{{ tag | slugify }}" rel="noopener">{{ tag }}</a>{% unless forloop.last %}, {% endunless %}
  {% endif %}
{% endfor %}
</div>
