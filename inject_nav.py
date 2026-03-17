import os
import glob
import re

nav_template = """  <nav class="global-nav">
    <a href="{prefix}index.html">Home</a>
    <a href="{prefix}Lab_02/profile.html">Profile</a>
    <a href="{prefix}Lab_02/schedule.html">Schedule</a>
    <a href="{prefix}Lab_02/registration.html">Register</a>
    <div class="dropdown">
      <a href="#" class="dropbtn">Exercises ▾</a>
      <div class="dropdown-content">
        <a href="{prefix}exercises/selectors.html">Selectors</a>
        <a href="{prefix}exercises/typography.html">Typography</a>
        <a href="{prefix}exercises/backgrounds.html">Backgrounds</a>
        <a href="{prefix}exercises/images.html">Images</a>
        <a href="{prefix}exercises/cards.html">Cards</a>
        <a href="{prefix}exercises/transforms.html">Transforms</a>
        <a href="{prefix}exercises/dark-mode.html">Dark Mode</a>
        <a href="{prefix}exercises/advanced.html">Advanced</a>
      </div>
    </div>
    <div class="dropdown">
      <a href="#" class="dropbtn">Layouts ▾</a>
      <div class="dropdown-content">
        <a href="{prefix}layouts/display-exercises.html">Display</a>
        <a href="{prefix}layouts/flexbox-exercises.html">Flexbox</a>
        <a href="{prefix}layouts/grid-exercises.html">Grid</a>
        <a href="{prefix}layouts/position-exercises.html">Position</a>
        <a href="{prefix}layouts/holy-grail-comparison.html">Holy Grail</a>
        <a href="{prefix}layouts/landing-page.html">Landing Page</a>
        <a href="{prefix}layouts/dashboard-grid.html">Dashboard</a>
        <a href="{prefix}layouts/responsive-demo.html">Responsive Demo</a>
      </div>
    </div>
  </nav>"""

base_dir = r"d:\UET Peshawar\4th Semester\Web Technologies (Sir Mohammad)\Lab\Assignments\WT_SP26"

html_files = glob.glob(os.path.join(base_dir, "**/*.html"), recursive=True)

for file in html_files:
    if "404.html" in file:
        continue
    
    # Calculate depth to figure out prefix
    rel_path = os.path.relpath(file, base_dir)
    depth = rel_path.count(os.sep)
    
    prefix = "../" * depth if depth > 0 else "./"
    
    new_nav = nav_template.format(prefix=prefix)
    
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We will try to replace `<nav>...</nav>` or `<nav class="...">...</nav>`. 
    # If the file doesn't have a nav, we inject it right after <body>
    nav_pattern = re.compile(r'<nav[^>]*>.*?</nav>', re.DOTALL)
    
    if nav_pattern.search(content):
        updated_content = nav_pattern.sub(new_nav, content)
    else:
        # insert after body
        body_pattern = re.compile(r'(<body[^>]*>)', re.IGNORECASE)
        updated_content = body_pattern.sub(r'\1\n' + new_nav, content)
        
    with open(file, 'w', encoding='utf-8') as f:
        f.write(updated_content)

print("Navigation injected into all files!")
