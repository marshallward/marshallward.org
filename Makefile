CONTENT = content
OUTPUT  = output
CONFIG  = blogconf.py

blog:
	pelican -s $(CONFIG) -o $(OUTPUT) $(CONTENT)

clean:
	rm -rf $(OUTPUT) $(CONFIG:.py=.pyc)

.PHONY: blog clean
