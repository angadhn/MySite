module Jekyll
  module ReadingTimeFilter
    def word_count(input)
      input.split.length
    end

    def reading_time(input)
      words_per_minute = 100
      minutes = (input.split.length / words_per_minute.to_f).ceil
      minutes
    end
  end
end

Liquid::Template.register_filter(Jekyll::ReadingTimeFilter) 