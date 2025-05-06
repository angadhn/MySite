---
layout: page
title: Home
id: home
permalink: /
---

# Welcome!

_[[This site]] belongs to  [[about|me]], [Angadh](https://www.sems.qmul.ac.uk/staff/a.nanjangud). It is an attempt to construct an aesthetic home for displaying my written wares._

_As it’s with my physical home, I expect to be the most regular user of this space — and so it’s for this reader’s satisfaction that it is being tuned, over time._

_That said, the occasional visitor from the web might pop in, accidentally (or, more likely, upon my invitation). For this reader, I recommend going through the [[essays|essays]], which are more fully formed thinkpieces. However, you might also wish to pick out one of the items that is top of mind or a more recently updated notes from below. A [[all notes|full archive]] also contains other random notes that might be useful to me (or you?) at some point._

_I also maintain [another site](https://angadhn.com) — my first attempt at creating an aesthetic digital home. The overloaded [Academic Pages template site](https://academicpages.github.io/)  did not match my taste and desired writing-to-publication workflow. That site will, however, continue to exist as the primary link to my online teaching resources- this list of is also [[My teaching content|here]]._

<div class="notes-grid">
  <div class="notes-column">
    <h5>Top of Mind</h5>
    <ul>
      {% assign top_notes = site.notes | where: "top_of_mind", true | sort: "last_modified_at_timestamp" | reverse %}
      {% for note in top_notes limit: 5 %}
        <li>
          • <a class="internal-link" href="{{ site.baseurl }}{{ note.url }}" style="font-family: 'Futura', serif;">{{ note.title }}</a>
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
          • <a class="internal-link" href="{{ site.baseurl }}{{ note.url }}" style="font-family: 'Futura', serif;">{{ note.title }}</a>
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
