FILE=
SCENE=
FLAGS=--disable_caching
QUALITY=-qm
run:
	manim $(FILE) $(SCENE) -p $(QUALITY) $(FLAGS)
