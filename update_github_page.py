import os
import sys
import subprocess
from glob import glob
import re


print("Updating CV...")
# os.system("rsync -av ../CV/Resume_Brandstetter.pdf static/media/Resume_Brandstetter.pdf")


print("Running hugo...")
os.system("hugo --minify --gc -F -b https://brandstetter-johannes.github.io/")

# Exchanging pictures with high-resolution versions
print("Exchanging pictures...")
img_paths = [
    ("public/authors/admin/avatar.jpg",
     "content/authors/admin/avatar.jpg")
]
for publ_img in sorted(glob("content/publication/*/featured.*")):
    path_pair = ("public/publication/%s/featured_*720*.*" % publ_img.split("/")[2],
                 publ_img)
    if len(glob(path_pair[0])) > 0:
        img_paths.append(path_pair)

for dest_path, orig_path in img_paths:
    dest_files = glob(dest_path)
    if len(dest_files) > 1:
        print("ERROR: For the image path to replace, multiple files were found: %s. Stopping the process..." % str(dest_files))
        sys.exit(1)
    elif len(dest_files) == 0:
        print("ERROR: File could not be found: %s." % dest_path)
        sys.exit(1)
    os.system("rsync -av %s %s" % (orig_path, dest_files[0]))

# Adding logos to experience
logo_paths = [
    "logos/NXAI-logo.png",
    "logos/JKU-Logo.jpg",
    "logos/logo-microsoft.svg",
    "logos/logo-microsoft.svg",
    "logos/logo-university-of-amsterdam.svg",
    "logos/JKU-Logo.jpg",
    "logos/JKU-Logo.jpg",
    "logos/cern-logo.jpg",
    "logos/hephy-logo.jpeg",
]
with open("public/experience/index.html", "r") as f:
    experience_text = "".join(f.readlines())
for l in logo_paths:
    if l == "":
        img_html = "<!-- -->" # Just commenting to prevent mixup
    else:
        img_html = '<div style="position: absolute; right: 10px;"><img src="%s" height="70" width="70"></div>' % l
    experience_text = experience_text.replace(
        '<div class=card-body>\n<div class="section-subheading',
        '<div class=card-body>%s<div class="section-subheading' % img_html,
        1)
experience_text = experience_text.replace('<div class="section-subheading card-title exp-company text-muted my-0">',
                                          '<div class="section-subheading card-title exp-company text-muted my-0" style="padding-right: 70px">')
experience_text = experience_text.replace('<div class="section-subheading card-title exp-title text-muted mt-0 mb-1">',
                                          '<div class="section-subheading card-title exp-title text-muted mt-0 mb-1" style="padding-right: 70px">')
with open("public/experience/index.html", "w") as f:
    f.write(experience_text)
    

print("Updating github.io repository...")
os.system("rsync -av public/ ../brandstetter-johannes.github.io/")


print("Git push...")
os.system("cd ../brandstetter-johannes.github.io/; git add --all; git commit -m \"Update from Hugo build\"; git push")
