rd /s /q "allure-results"
behave -f allure_behave.formatter:AllureFormatter -o allure-results
allure generate --clean -o allure-report allure-results