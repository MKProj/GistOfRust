import os
import zipfile
    
def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file), 
                       os.path.relpath(os.path.join(root, file), 
                                       os.path.join(path, '..')))

# Different formats 
book = "TheGistOfRust"
all_ = f'{book}_all.zip'
web = f'{book}_web.zip'
pdf = f'{book}_pdf.zip'
cs = f'{book}_cs.zip'


# Paths to all zip formats
zip_all = zipfile.ZipFile(f'releases/{all_}', 'w', zipfile.ZIP_DEFLATED)
zip_web = zipfile.ZipFile(f'releases/{web}', 'w', zipfile.ZIP_DEFLATED)
zip_pdf = zipfile.ZipFile(f'releases/{pdf}', 'w', zipfile.ZIP_DEFLATED)
zip_cs = zipfile.ZipFile(f'releases/{cs}', 'w', zipfile.ZIP_DEFLATED)


# all directories for TheGistOfRust_all.zip
zipdir('docs/TheGistOfRust.pdf', zip_all)
zipdir('tex/', zip_all)
zipdir('book/', zip_all)
zipdir('src/', zip_all)
zipdir('book.toml', zip_all)
zipdir('cheatsheet/', zip_all)
zipdir('images/', zip_all)

# all directories for TheGistOfRust_web.zip
zipdir('src/', zip_web)
zipdir('book/', zip_web)
zipdir('book.toml', zip_web)
zipdir('images/', zip_web)

# all directories for TheGistOfRust_pdf.zip
zipdir('docs/TheGistOfRust.pdf', zip_pdf)
zipdir('tex/', zip_pdf)
zipdir('images/', zip_pdf)

# all directories for TheGistOfRust_cs.pdf
zipdir('cheatsheet/', zip_cs)

zip_all.close()
zip_web.close()
zip_pdf.close()
zip_cs.close()