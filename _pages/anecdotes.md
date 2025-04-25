---
layout: page
title: Anecdotes
permalink: /anecdotes/
---

The below are random personal anecdotes.

<div class="essays-list" style="font-size: 0.9em;">
{% assign notes_with_anecdotes = site.notes | where_exp: "note", "note.tags contains 'anecdotes'" | sort: "published" | reverse %}
{% for note in notes_with_anecdotes %}
  <article class="essay-item">
    <div style="display: flex; align-items: baseline; gap: 1em;">
      <time style="color: #666; white-space: nowrap;" datetime="{{ note.published | date_to_xmlschema }}">{{ note.published | date: "%d-%m-%Y" }}</time>
      <a class="internal-link" href="{{ site.baseurl }}{{ note.url }}" style="font-family: 'Futura', serif;">{{ note.title }}</a>
    </div>
  </article>
{% endfor %}
</div> 