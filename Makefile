PYTHON = python3
PAGER = less

.PHONY: build clean all

build:
	@chmod +x openhash.py closedhash.py trie.py dijkstra.py dijkstra2.py floyd.py dfs.py

clean:
	@-rm -rf *.pyc __pycache__

all: openhash closedhash trie dijkstra dijkstra2 floyd dfs

openhash: openhash.py
	-$(PYTHON) openhash.py

closedhash: closedhash.py
	-$(PYTHON) closedhash.py

trie: trie.py
	-$(PYTHON) trie.py

dijkstra: dijkstra.py
	-$(PYTHON) dijkstra.py

dijkstra2: dijkstra2.py
	-$(PYTHON) dijkstra2.py

floyd: floyd.py
	-$(PYTHON) floyd.py
	
dfs: dfs.py
	-$(PYTHON) dfs.py


