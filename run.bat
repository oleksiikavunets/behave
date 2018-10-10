behave -f allure_behave.formatter:AllureFormatter -o target/allure-results
allure generate --clean -o target/allure-report target/allure-results