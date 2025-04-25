module Jekyll
  class TotalWordCount < Generator
    safe true
    
    def generate(site)
      total_words = 0
      
      # Loop through all notes and sum up word counts
      site.collections['notes'].docs.each do |doc|
        # Count words in the document content
        content = doc.content.strip
        total_words += count_words(content)
      end
      
      # Store the total word count as a site variable
      site.config['total_word_count'] = total_words
    end
    
    private
    
    def count_words(content)
      # Strip HTML tags and count words
      content.gsub(/<\/?[^>]*>/, "").split(/\s+/).length
    end
  end
end 