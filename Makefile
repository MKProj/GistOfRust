build: 



git: 
	git add -A
	git commit -m "${user} at $(date +'%D %T')"
	git push
tex: 
	cd tex && pdflatex main x 2
plan-tex:
	cd plan && pdflatex plan.tex x 2
	mv plan/plan.pdf docs/