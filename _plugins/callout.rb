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

    def convert_callouts(doc)
      # Convert Obsidian-style callouts to HTML
      doc.content.gsub!(/> \[!([^\]]+)\](.*?)(?=\n\n|\Z)/m) do |match|
        type = $1.strip
        content = $2.strip.gsub(/^>\s*/, '') # Remove leading '>' and any whitespace
        
        # Create HTML for the callout
        <<~HTML
          <div class="callout #{type.downcase}">
            <div class="callout-title">#{type}</div>
            <div class="callout-content">
              #{content}
            </div>
          </div>
        HTML
      end
    end
  end
end 