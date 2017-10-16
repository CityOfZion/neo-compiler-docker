REPONAME = "coz/neoj-compiler"
ROOT = $(shell pwd)

build:
	@printf "Building ${REPONAME}... \n\n"
	@docker build -t ${REPONAME} .

publish-neoj:
	@printf "Publishing neo-compiler/neoj to neoj.dll...\n\n"
	@docker run -it --rm -v '${ROOT}/submodule-neo-compiler/neoj:/usr/src' -w '/usr/src' microsoft/dotnet:2.0.0-sdk dotnet publish -o out/
	@printf "\nComplete, location: ${ROOT}/submodule-neo-compiler/neoj/out/neoj.dll\n"

update-submodule:
	@git submodule update --recursive