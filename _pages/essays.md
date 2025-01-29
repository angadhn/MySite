---
layout: page
title: Essays
permalink: /essays/
---

> The below are some passages I've written that are probably over 600 words. I am currently qualifying
> any writing of that length as an essay for now but is likely to be revisited in future.

<div class="essays-list" style="font-size: 0.9em;">
{% assign notes_with_essays = site.notes | where_exp: "note", "note.tags contains 'essays'" | sort: "published" | reverse %}
{% for note in notes_with_essays %}
  <article class="essay-item">
    <div style="display: flex; align-items: baseline; gap: 1em;">
      <time style="color: #666; white-space: nowrap;" datetime="{{ note.published | date_to_xmlschema }}">{{ note.published | date: "%Y-%m-%d" }}</time>
      <a class="internal-link" href="{{ site.baseurl }}{{ note.url }}" style="font-family: 'Aniron', serif;">{{ note.title }}</a>
    </div>
  </article>
{% endfor %}
</div> 