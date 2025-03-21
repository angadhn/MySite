module Jekyll
  class PythonPreprocessor < Generator
    safe true
    priority :high

    def generate(site)
      # Only run in development environment or if forced
      return if ENV['JEKYLL_ENV'] == 'production' && !ENV['FORCE_PYTHON']

      # Get all Python files in _code directory
      Dir.glob("_code/*.py").each do |python_file|
        puts "Processing Python file: #{python_file}"
        system("python3 #{python_file}")
        if $?.exitstatus != 0
          Jekyll.logger.error "Python Processing:", "Error running #{python_file}"
          raise "Python processing failed"
        end
      end
    end
  end
end 