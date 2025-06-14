module Jekyll
  class CalloutConverter < Generator
    def generate(site)
      site.collections['notes'].docs.each do |doc|
        convert_callouts(doc)
      end
      
      site.pages.each do |page|
        next unless page.path.start_with?('_pages/')
        convert_callouts(page)
      end
    end

    private

    def icon_for_type(type)
      case type.downcase
      when "tip"
        '<i class="fa-solid fa-fire"></i>'
      when "note"
        '<i class="fa-solid fa-pen-to-square"></i>'
      when "challenge"
        '<i class="fa-solid fa-circle-info"></i>'
      when "warning"
        '<i class="fa-solid fa-triangle-exclamation"></i>'
      else
        ''
      end
    end

    def convert_callouts(doc)
      # Handle [!Type Title] and [!Type] Title syntaxes
      doc.content.gsub!(/^> \[!([A-Za-z]+)([^\]]*)\]\s*(.*?)(?=\n\n|\Z)/m) do |match|
        type = $1.strip.downcase
        bracket_title = $2.strip
        after_bracket = $3.strip

        # If bracket_title is present, use it as the title
        # Otherwise, use the first line after the bracket as the title (if present)
        if bracket_title != ''
          callout_title = "#{$1.strip} #{bracket_title}".strip
          callout_body = after_bracket
        else
          # Split after_bracket into first line (title) and the rest (body)
          lines = after_bracket.lines
          callout_title = lines.first ? lines.first.strip : $1.strip.capitalize
          callout_body = lines[1..-1] ? lines[1..-1].join.strip : ''
        end

        # Remove leading '>' from body lines
        callout_body = callout_body.gsub(/^>\s*/, '')

        icon_html = icon_for_type(type)

        <<~HTML
          <div class="callout #{type}">
            <div class="callout-title">#{icon_html} #{callout_title}</div>
            <div class="callout-content">
              #{callout_body}
            </div>
          </div>
        HTML
      end
    end
  end
end 