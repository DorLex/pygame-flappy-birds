## Реализация игры "Flappy Birds" на `pygame`.

## Установка зависимостей:

1. Создать окружение через `poetry`:
    ```shell
    poetry env use python3.12
    ```

2. Активировать окружение: *(можно и через `poetry shell`, но `shell` в последних версиях является плагином, и не
   предустановлен)*
    ```shell
    eval $(poetry env activate)
    ```

3. Установить основные зависимости, необходимые для запуска:
   ```shell
   poetry install --no-root --without dev
   ```

4. Установить все зависимости, включая dev/test (+linter, +pre-commit и т.д.):
    ```shell
    poetry install --no-root
    ```

### Предпросмотр:

![preview screenshot](preview.png)
