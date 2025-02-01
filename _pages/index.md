---
layout: page
title: Home
id: home
permalink: /
---

# Welcome!

> [[This site]] belongs to  [[about|me]], [Angadh](https://www.sems.qmul.ac.uk/staff/a.nanjangud). It is an attempt to construct an aesthetic home for displaying my written wares. Like most homes, the most frequent visitor of this place will likely be me and it’s for this reader’s consumption that this place is being crafted. That said, the occasional visitor from the web may pop in- much like a house guest does. Here, I share a bunch of my digital notes, some of them worked into essay opining on things. Internet stumblers might want to start by exploring what's top of mind or looking at one my recently updated notes below. A [[all notes|complete archive]] of [[this site]]'s content is also available though you may be better served filtering by topic- this can be found below. I also maintain another [site](angadhn.com), which was my first attempt at making a personal static site. It was my first experiment at making an aesthetic site but working with overloaded templates was too painful to sustain. So here we are and I have to admit that first iteration was far from my taste. That said, it will continue to exist (and maybe even evolve) as the domain is links to my online teaching materials for the university, a list of which can also be found on this [[My teaching content|site]]. I genuinely like the novelty of having secured this domain, which is my “first name dot com”.
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
