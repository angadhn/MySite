from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen

def create_favicon(font_path, color, output_path):
    # Load the font
    font = TTFont(font_path)
    
    # Get the glyph set
    glyph_set = font.getGlyphSet()
    
    # Find the glyph name for 'A'
    cmap = font['cmap'].getBestCmap()
    glyph_name = cmap[ord('A')]
    
    # Get the glyph
    glyph = glyph_set[glyph_name]
    
    # Create SVG pen
    pen = SVGPathPen(glyph_set)
    
    # Draw the glyph
    glyph.draw(pen)
    
    # Get the path data
    path_data = pen.getCommands()
    
    # Create SVG content with transform to scale vertically and rotate
    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 1000">
        <g transform="scale(1, -1) translate(0, -1000) rotate(0, 500, 500)">
            <path d="{path_data}" fill="{color}"/>
        </g>
    </svg>'''
    
    # Write to file
    with open(output_path, 'w') as f:
        f.write(svg_content)

# Generate both favicons
create_favicon('assets/aniron.ttf', 'black', 'assets/favicon-light.svg')
create_favicon('assets/aniron.ttf', 'white', 'assets/favicon-dark.svg')