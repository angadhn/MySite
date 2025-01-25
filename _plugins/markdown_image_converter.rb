# frozen_string_literal: true

module Jekyll
  class MarkdownImageConverter < Generator
    priority :high
    
    def initialize(site)
      super
      @site = site
    end

    def generate(site)
      site.collections['notes'].docs.each do |document|
        document.content = convert(document.content)
      end
    end

    def convert(content)
      content.gsub(/!\[(.*?)\]\((.*?)\)/) do |match|
        caption = $1.empty? ? '' : $1
        image_path = $2.sub(/^\//, '') # Remove leading slash if present
        # Format without square brackets, just single quotes
        "{% maincolumn '#{image_path}' '#{caption}' %}"
      end
    end
  end
end

Jekyll::Hooks.register [:notes], :pre_render do |doc|
  convert_images(doc)
end

Jekyll::Hooks.register [:pages], :pre_render do |doc|
  # jekyll considers anything at the root as a page,
  # we only want to consider actual pages
  next unless doc.path.start_with?('_pages/')
  convert_images(doc)
end

def convert_images(doc)
  # Match standard Markdown image syntax
  # Using negative lookbehind to ensure it's not part of a wiki-link
  doc.content.gsub!(/(?<!\[)!\[(.*?)\]\((.*?)\)/) do |match|
    caption = $1.empty? ? 'Imagine a caption' : $1
    image_path = $2.sub(/^\//, '')
    "{% maincolumn '#{image_path}' '#{caption}' %}"
  end
end 