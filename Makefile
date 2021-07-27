build: 
	make mdbook
	make tex 
	make zip 
	make git
mdbook: 
	mdbook build
zip: 
	python3 zip_release.py
git: 
	git add -A
	git commit -m "updated content"
	git push
tex: 
	cd tex && pdflatex TheGistOfRust x 2
	mv tex/TheGistOfRust.pdf docs/
plan-tex:
	cd plan && pdflatex plan.tex x 2
	mv plan/plan.pdf docs/