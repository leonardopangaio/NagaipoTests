git:
	@git fetch origin \
		&& git pull --no-rebase origin \
		&& git add . \
		&& git commit -m "Making a new test." \
		&& git push origin

teste:
	@ python3 bin/generate_glossary.py