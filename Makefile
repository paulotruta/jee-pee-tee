.DEFAULT_GOAL := release


BUILD_DIR=build


release: clean
	mkdir $(BUILD_DIR)
	zip -r $(BUILD_DIR)/jee-pee-tee.zip lambda -x lambda/\config.example.json -x lambda/\.venv/\*


clean:
	rm -rf $(BUILD_DIR)
