# frozen_string_literal: true
require 'nokogiri'

# This plugin handles PDF links in two formats:
# 1. Standard Markdown links pointing to PDFs: [text](path/to/file.pdf)
# 2. Wiki-style links to internal PDFs: [[assets/pdf/file.pdf|text]]
#
# Priority is set to :highest to ensure it runs before bidirectional_links_generator

module Jekyll
  class PDFLinkConverter < Generator
    priority :highest
    
    def generate(site)
      # Process all notes and pages
      site.collections['notes'].docs.each do |doc|
        process_pdf_links(doc, site)
      end
      
      site.pages.each do |page|
        # Only process pages in _pages directory
        next unless page.path.start_with?('_pages/')
        process_pdf_links(page, site)
      end
    end
    
    def process_pdf_links(doc, site)
      baseurl = site.config['baseurl'] || ''
      
      # Process standard markdown links to PDFs
      doc.content.gsub!(/\[([^\]]+)\]\(([^)]+\.pdf)([^)]*)\)/) do |match|
        link_text = $1
        pdf_path = $2
        query_params = $3 || ""
        
        # Create appropriate link based on whether it's internal or external
        if pdf_path.start_with?('http://', 'https://')
          # External PDF link
          "<a href='#{pdf_path}#{query_params}' target='_blank' class='pdf-link external-link'>#{link_text}</a>"
        else
          # Internal PDF link - make sure it has the site.baseurl
          internal_path = pdf_path.start_with?('/') ? "#{baseurl}#{pdf_path}" : "#{baseurl}/#{pdf_path}"
          "<a class='internal-link pdf-link' href='#{internal_path}#{query_params}'>#{link_text}</a>"
        end
      end
      
      # Process wiki-style links to PDFs
      doc.content.gsub!(/\[\[([^|\]]+\.pdf)\|([^\]]+)\]\]/) do |match|
        pdf_path = $1
        link_text = $2
        
        # Normalize path and add baseurl for internal PDFs
        internal_path = pdf_path.start_with?('/') ? "#{baseurl}#{pdf_path}" : "#{baseurl}/#{pdf_path}"
        "<a class='internal-link pdf-link' href='#{internal_path}'>#{link_text}</a>"
      end
    end
  end
end

# Optional: Add some nice styling for PDF links
Jekyll::Hooks.register :site, :post_render do |site|
  site.pages.each do |page|
    next unless page.output =~ /<\/head>/
    
    pdf_link_style = %{
<style>
  .pdf-link {
    text-decoration: none;
    border-bottom: 1px dashed;
    position: relative;
  }
  .pdf-link:after {
    content: " 📄";
    font-size: 0.8em;
    vertical-align: super;
    opacity: 0.7;
  }
  .pdf-link.external-link:after {
    content: " 📄↗";
  }
</style>}
    
    page.output.gsub!(/<\/head>/, "#{pdf_link_style}\n</head>")
  end
end 