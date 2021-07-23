build: 

zip: 
	python3 zip_release.py
git: 
	git add -A
	git commit -m "updated content"
	git push
tex: 
	cd tex && pdflatex main x 2
plan-tex:
	cd plan && pdflatex plan.tex x 2
	mv plan/plan.pdf docs/