git:
	@git fetch origin \
		&& git add . \
		&& git commit -m "Making a new test." \
		&& git pull --no-rebase origin \
		&& git push origin

teste:
	@ python3 bin/generate_glossary.py