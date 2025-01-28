module Jekyll
  class TagPageGenerator < Generator
    safe true

    def generate(site)
      tags = site.documents.flat_map { |doc| doc.data['tags'] || [] }.uniq.sort
      
      tags.each do |tag|
        site.pages << TagPage.new(site, tag)
      end
    end
  end

  class TagPage < Page
    def initialize(site, tag)
      @site = site
      @base = site.source
      @dir = 'tags'
      @name = "#{tag.downcase.gsub(' ', '-')}.md"

      self.process(@name)
      self.read_yaml(File.join(@base, '_layouts'), 'tag.html')
      
      self.data['title'] = "#{tag}"
      self.data['tag'] = tag
    end
  end
end 