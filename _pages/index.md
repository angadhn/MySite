---
layout: page
title: Home
id: home
permalink: /
---

# Welcome! 🌱

<div class="welcome-block">
  Hey, I am <span class="external-link"><a href="https://www.sems.qmul.ac.uk/staff/a.nanjangud">Angadh</a></span>. Depending on how you know [[about|me]], you might want to take a look at some of <span class="internal-link">[[My teaching content]]</span> or <span class="internal-link">[[My research interests]]</span>.
  
  If you just stumbled on here, you might wish to read <span class="internal-link">[[My longer form blogpost-y notes]]</span> or browse the <a class="internal-link" href="{{ site.baseurl }}/all-notes">complete archive of notes</a>, or just explore the most recently updated notes in the list below.
</div>

<strong>Recently updated notes</strong>

<ul>
  {% assign recent_notes = site.notes | sort: "last_modified_at_timestamp" | reverse %}
  {% for note in recent_notes limit: 5 %}
    <li>
      {{ note.last_modified_at | date: "%Y-%m-%d" }} — <a class="internal-link" href="{{ site.baseurl }}{{ note.url }}">{{ note.title }}</a>
    </li>
  {% endfor %}
</ul>
