CONTENT = content
OUTPUT  = output
CONFIG  = blogconf.py

blog: $(CONTENT)
	pelican -s $(CONFIG) -o $(OUTPUT) $(CONTENT)

clean:
	rm -rf $(OUTPUT) $(CONFIG:.py=.pyc)

.PHONY: blog clean
