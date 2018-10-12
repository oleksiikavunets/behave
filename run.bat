rd /s /q "allure-results"
behave --tags=~@50tests -f allure_behave.formatter:AllureFormatter -o allure-results --no-skipped
allure generate --clean -o allure-report allure-results