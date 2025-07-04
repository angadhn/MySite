---
layout: page
title: Home
id: home
permalink: /
---

# Welcome!

_[[This site]] belongs to  [[about|me]], [Angadh](https://www.sems.qmul.ac.uk/staff/a.nanjangud). It is an attempt to construct an aesthetic home for displaying my written wares._

_As it’s with my physical home, I expect to be the most regular user of this space — and so it’s for this reader’s satisfaction that it is being tuned, over time. Yes—[Gwern](https://gwern.net), [Andy Matuschak](https://andymatuschak.org/), and [Michael Nielsen](https://michaelnotebook.com/) have all influenced me in some way._

_That said, the occasional visitor from the web might pop in, accidentally (or, more likely, upon my invitation). For this reader, I recommend going through the [[essays|essays]], which are more fully formed thinkpieces—recent ones are listed below. However, you might also wish to pick out one of the more recently updated posts or one that is top of mind, which is essentially some kind of draft idea I am working on—this last one is bound to be useless to anyone but me as it is a scrap-heap (mostly)._

_A [[all notes|complete archive of writing over here]] contains all essays, notes, etc. that might be useful to me (or you?) at some point._

_My [other site](https://angadhn.com) is the primary link to my teaching resources for students, which are also [[My teaching content|here]]._

<div class="notes-grid">
  <div class="notes-column">
    <h5>Recent Essays</h5>
    <ul>
      {% assign notes_with_essays = site.notes | where_exp: "note", "note.tags contains 'essays' and note.hideFromHomePage != true and note.hideFromHomePage != 'true'" | sort: "published" | reverse %}
      {% for note in notes_with_essays limit: 5 %}
        <li>
          • <a class="internal-link" href="{{ site.baseurl }}{{ note.url }}" style="font-family: 'Futura', serif;">{{ note.title }}</a>
        </li>
      {% endfor %}
    </ul>
  </div>

  <div class="notes-column">
    <h5>Updated</h5>
    <ul>
      {% assign recent_notes = site.notes | where_exp: "note", "note.hideFromHomePage != true and note.hideFromHomePage != 'true'" | sort: "last_modified_at_timestamp" | reverse %}
      {% assign count = 0 %}
      {% for note in recent_notes %}
        {% unless note.tags contains 'WiP' %}
          {% if count < 5 %}
            <li>
              • <a class="internal-link" href="{{ site.baseurl }}{{ note.url }}" style="font-family: 'Futura', serif;">{{ note.title }}</a>
            </li>
            {% assign count = count | plus: 1 %}
          {% endif %}
        {% endunless %}
        {% if count >= 5 %}
          {% break %}
        {% endif %}
      {% endfor %}
    </ul>
  </div>

  <div class="notes-column">
    <h5>In the Garage</h5>
    <ul>
      {% assign WiP_notes = site.notes | where_exp: "note", "note.tags contains 'WiP' and note.hideFromHomePage != true and note.hideFromHomePage != 'true'"  | sort: "last_modified_at_timestamp" | reverse %}
      {% for note in WiP_notes limit: 5 %}
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
