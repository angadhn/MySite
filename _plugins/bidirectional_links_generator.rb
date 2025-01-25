# frozen_string_literal: true
class BidirectionalLinksGenerator < Jekyll::Generator
  def generate(site)
    graph_nodes = []
    graph_edges = []

    all_notes = site.collections['notes'].docs
    all_pages = site.pages
    all_docs = all_notes + all_pages
    link_extension = !!site.config["use_html_extension"] ? '.html' : ''

    # Convert all Wiki/Roam-style double-bracket link syntax to plain HTML
    # anchor tag elements (<a>) with "internal-link" CSS class
    all_docs.each do |current_note|
      all_docs.each do |note_potentially_linked_to|
        note_title_regexp_pattern = Regexp.escape(
          File.basename(
            note_potentially_linked_to.basename,
            File.extname(note_potentially_linked_to.basename)
          )
        ).gsub('\_', '[ _]').gsub('\-', '[ -]').capitalize

        title_from_data = note_potentially_linked_to.data['title']
        title_from_data = Regexp.escape(title_from_data) if title_from_data
        new_href = "#{site.baseurl}#{note_potentially_linked_to.url}#{link_extension}"
        anchor_tag = "<a class='internal-link' href='#{new_href}'>\\1</a>"

        # Handle links to headings with custom text [[note#heading|label]]
        current_note.content.gsub!(
          /\[\[#{note_title_regexp_pattern}#([^\]|]+)\|([^\]]+)\]\]/i
        ) do |match|
          heading = $1
          link_text = $2
          heading_id = heading.downcase.gsub(/\s+/, '-').gsub(/[^\w-]/, '')
          "<a class='internal-link' href='#{new_href}##{heading_id}'>#{link_text}</a>"
        end

        # Handle links to headings [[note#heading]]
        current_note.content.gsub!(
          /\[\[#{note_title_regexp_pattern}#([^\]]+)\]\]/i
        ) do |match|
          heading = $1
          heading_id = heading.downcase.gsub(/\s+/, '-').gsub(/[^\w-]/, '')
          "<a class='internal-link' href='#{new_href}##{heading_id}'>#{note_title_regexp_pattern} § #{heading}</a>"
        end

        # Replace double-bracketed links with label using note title
        current_note.content.gsub!(
          /\[\[#{note_title_regexp_pattern}\|(.+?)(?=\])\]\]/i,
          anchor_tag
        )

        # Replace double-bracketed links with label using note filename
        current_note.content.gsub!(
          /\[\[#{title_from_data}\|(.+?)(?=\])\]\]/i,
          anchor_tag
        )

        # Replace double-bracketed links using note title
        current_note.content.gsub!(
          /\[\[(#{title_from_data})\]\]/i,
          anchor_tag
        )

        # Replace double-bracketed links using note filename
        current_note.content.gsub!(
          /\[\[(#{note_title_regexp_pattern})\]\]/i,
          anchor_tag
        )
      end

      # Convert remaining double-bracket-wrapped words to invalid links
      current_note.content = current_note.content.gsub(
        /\[\[([^\]]+)\]\]/i,
        <<~HTML.delete("\n")
          <span title='There is no note that matches this link.' class='invalid-link'>
            <span class='invalid-link-brackets'>[[</span>
            \\1
            <span class='invalid-link-brackets'>]]</span></span>
        HTML
      )
    end

    # Build backlinks and graph data
    all_notes.each do |current_note|
      # Nodes: Jekyll
      notes_linking_to_current_note = all_notes.filter do |e|
        e.content.include?(current_note.url)
      end

      # Nodes: Graph
      unless current_note.path.include?('_notes/index.html')
        graph_nodes << {
          id: note_id_from_note(current_note),
          path: "#{site.baseurl}#{current_note.url}#{link_extension}",
          label: current_note.data['title'],
        }
      end

      # Edges: Jekyll
      current_note.data['backlinks'] = notes_linking_to_current_note

      # Edges: Graph
      notes_linking_to_current_note.each do |n|
        graph_edges << {
          source: note_id_from_note(n),
          target: note_id_from_note(current_note),
        }
      end
    end

    File.write('_includes/notes_graph.json', JSON.dump({
      edges: graph_edges,
      nodes: graph_nodes,
    }))
  end

  def note_id_from_note(note)
    note.data['title'].bytes.join
  end
end
