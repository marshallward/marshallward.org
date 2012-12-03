CONTENT = content
OUTPUT  = output
CONFIG  = blogconf.py

blog:
	pelican -s $(CONFIG) -o $(OUTPUT) $(CONTENT)

clean:
	rm -rf $(OUTPUT)

.PHONY: blog clean
