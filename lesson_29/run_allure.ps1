# Крок 1: Запустити тести у Docker
docker compose -f "docker-compose.yml" up --build --abort-on-container-exit

# Крок 2: Видалити попередні контейнери Allure (якщо є)
docker rm -f allure-viewer 2>$null
docker rm -f allure-ui 2>$null

# Крок 3: Запустити Allure Viewer
$projectPath = (Get-Location).Path.Replace("\\", "/")
docker run -d -p 5050:5050 `
  -v "$projectPath/allure-results:/app/allure-results" `
  -v "$projectPath/allure-report:/app/allure-report" `
  --name=allure-viewer frankescobar/allure-docker-service

# Крок 4: Запустити Allure UI
Start-Sleep -Seconds 3
docker run -d -p 5252:5252 `
  --name=allure-ui `
  -e ALLURE_DOCKER_PUBLIC_API_URL=http://localhost:5050 `
  frankescobar/allure-docker-service-ui

# Крок 5: Відкрити браузер
Start-Process "http://localhost:5252"
